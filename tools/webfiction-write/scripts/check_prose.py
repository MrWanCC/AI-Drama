#!/usr/bin/env python3
"""Run deterministic safety checks on one or more Chinese prose files.

The checker is deliberately conservative: blocking findings are integrity or
generation failures; style signals are advisory and must not replace a human
read-through or an independent review.
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


SELF_REFERENCE_PATTERNS = (
    r"作为(?:一个)?AI",
    r"我无法(?:继续|完成|生成)",
    r"无法(?:为你)?续写",
    r"\(此处省略\)|（此处省略）",
    r"以下(?:是|为)写作建议",
)
PLACEHOLDER_PATTERNS = (
    r"\{[^{}]{1,80}\}",
    r"\[待(?:补充|填写|定)\]",
    r"TODO|TBD|PLACEHOLDER",
)
ENGINEERING_TERMS = (
    "细纲",
    "情节点",
    "reviewer",
    "chapter-commit",
    "下一章",
    "本章完成",
    "写作任务书",
)
AI_STYLE_TERMS = (
    "仿佛",
    "犹如",
    "宛若",
    "不禁",
    "缓缓",
    "微微",
    "一丝",
    "一抹",
    "与此同时",
    "显而易见",
)
ENDING_SUMMARY_RE = re.compile(
    r"(?:他|她|主角|这一刻).{0,18}(?:终于明白|终于意识到|注定|更大的风暴|一切都结束了)"
)


def finding(code, severity, message, line=None, count=None):
    item = {"code": code, "severity": severity, "message": message}
    if line is not None:
        item["line"] = line
    if count is not None:
        item["count"] = count
    return item


def inspect_file(path):
    findings = []
    try:
        raw = path.read_bytes()
    except OSError as exc:
        return [finding("read_error", "blocking", f"无法读取文件：{exc}")]

    if raw.startswith(b"\xef\xbb\xbf"):
        findings.append(finding("utf8_bom", "blocking", "文件含 UTF-8 BOM"))
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        return findings + [
            finding("invalid_utf8", "blocking", f"不是有效 UTF-8：字节位置 {exc.start}")
        ]

    if not text.strip():
        findings.append(finding("empty_prose", "blocking", "正文为空"))
        return findings
    if "\ufffd" in text:
        findings.append(finding("replacement_char", "blocking", "正文含 Unicode 替换字符（U+FFFD）"))

    controls = [
        (index + 1, ord(char))
        for index, char in enumerate(text)
        if ord(char) < 32 and char not in "\r\n\t"
    ]
    if controls:
        findings.append(
            finding(
                "control_character",
                "blocking",
                "正文含不可见控制字符：" + ", ".join(f"U+{code:04X}" for _, code in controls[:5]),
                count=len(controls),
            )
        )

    lines = text.splitlines()
    for pattern in SELF_REFERENCE_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            findings.append(
                finding(
                    "model_self_reference",
                    "blocking",
                    "正文含模型拒答或写作元话语",
                    line=text[: match.start()].count("\n") + 1,
                )
            )
            break

    for pattern in PLACEHOLDER_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            findings.append(
                finding(
                    "placeholder",
                    "blocking",
                    "正文含未替换占位符",
                    line=text[: match.start()].count("\n") + 1,
                )
            )
            break

    line_counts = Counter(line.strip() for line in lines if len(line.strip()) >= 10)
    repeated = [(line, count) for line, count in line_counts.items() if count >= 3]
    if repeated:
        findings.append(
            finding(
                "repeated_line",
                "blocking",
                "存在重复三次以上的完整正文行",
                count=max(count for _, count in repeated),
            )
        )

    prose_lines = [line for line in lines if not line.lstrip().startswith("#")]
    prose_text = "\n".join(prose_lines)
    engineering_count = sum(prose_text.count(term) for term in ENGINEERING_TERMS)
    if engineering_count >= 2:
        findings.append(
            finding(
                "engineering_leak",
                "advisory",
                "正文疑似泄漏写作工程词，需结合对话/真实叙事语境复核",
                count=engineering_count,
            )
        )

    for term in AI_STYLE_TERMS:
        count = prose_text.count(term)
        if count >= 4:
            findings.append(
                finding(
                    "ai_style_density",
                    "advisory",
                    f"“{term}”出现频率偏高，先检查是否有具体动作或语境支撑",
                    count=count,
                )
            )

    paragraphs = re.split(r"\n\s*\n", prose_text)
    long_paragraphs = [len(paragraph.strip()) for paragraph in paragraphs if len(paragraph.strip()) > 500]
    if long_paragraphs:
        findings.append(
            finding(
                "long_paragraph",
                "advisory",
                "存在超过 500 字的长段落，按动作/信息变化检查是否需要断段",
                count=len(long_paragraphs),
            )
        )

    tail = prose_text.strip()[-120:]
    if ENDING_SUMMARY_RE.search(tail):
        findings.append(
            finding(
                "summary_ending",
                "advisory",
                "章尾疑似使用总结/预告式收束，优先改为具体动作、物件、台词或即时危险",
            )
        )
    return findings


def main(argv=None):
    parser = argparse.ArgumentParser(description="检查正文完整性与常见 AI 生成退化信号")
    parser.add_argument("--check", nargs="+", required=True, metavar="FILE")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument(
        "--fail-on",
        choices=("blocking", "advisory"),
        default="blocking",
        help="遇到哪一档问题返回非零；默认只阻断完整性问题",
    )
    args = parser.parse_args(argv)

    reports = []
    failed = False
    for value in args.check:
        path = Path(value)
        findings = inspect_file(path)
        has_blocking = any(item["severity"] == "blocking" for item in findings)
        has_advisory = any(item["severity"] == "advisory" for item in findings)
        failed_for_policy = has_blocking or (args.fail_on == "advisory" and has_advisory)
        report = {
            "file": str(path),
            "ok": not failed_for_policy,
            "blocking": has_blocking,
            "advisory": has_advisory,
            "findings": findings,
        }
        reports.append(report)
        if failed_for_policy:
            failed = True

    if args.format == "json":
        print(json.dumps(reports, ensure_ascii=False, indent=2))
    else:
        for report in reports:
            if not report["findings"]:
                print(f"OK: {report['file']}")
                continue
            print(f"CHECK: {report['file']}")
            for item in report["findings"]:
                location = f" line {item['line']}" if "line" in item else ""
                suffix = f" (count={item['count']})" if "count" in item else ""
                print(f"  [{item['severity']}] {item['code']}{location}: {item['message']}{suffix}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
