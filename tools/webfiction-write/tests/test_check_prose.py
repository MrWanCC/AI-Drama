"""scripts/check_prose.py 的确定性闸门测试。"""

import importlib.util
import json
from pathlib import Path


SCRIPT = Path(__file__).parent.parent / "scripts" / "check_prose.py"
SPEC = importlib.util.spec_from_file_location("check_prose", SCRIPT)
CHECK_PROSE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK_PROSE)


def write_sample(tmp_path, text):
    path = tmp_path / "chapter.md"
    path.write_text(text, encoding="utf-8")
    return path


def test_clean_prose_has_no_findings(tmp_path):
    path = write_sample(tmp_path, "雨停了。曹旭把伞靠在门边，伸手去摸桌上的钥匙。\n\n门外传来三下敲门声。")
    assert CHECK_PROSE.inspect_file(path) == []


def test_blocking_findings_cover_refusal_placeholder_and_control(tmp_path):
    path = write_sample(
        tmp_path,
        "作为一个AI，我无法继续。\n\n[待补充]\n\n这是一句需要重复的正文。\n这是一句需要重复的正文。\n这是一句需要重复的正文。\n" + chr(12),
    )
    findings = CHECK_PROSE.inspect_file(path)
    codes = {item["code"] for item in findings}
    assert {"model_self_reference", "placeholder", "repeated_line", "control_character"} <= codes
    assert all(item["severity"] == "blocking" for item in findings)


def test_advisory_does_not_fail_default_but_fails_advisory_policy(tmp_path, capsys):
    path = write_sample(tmp_path, "他仿佛看见了光。" * 5)
    assert CHECK_PROSE.main(["--check", str(path)]) == 0
    capsys.readouterr()
    assert CHECK_PROSE.main(["--check", str(path), "--fail-on", "advisory"]) == 1
    output = capsys.readouterr().out
    assert "ai_style_density" in output


def test_json_report_exposes_blocking_and_advisory(tmp_path, capsys):
    path = write_sample(tmp_path, "作为一个AI，我无法继续。")
    assert CHECK_PROSE.main(["--check", str(path), "--format", "json"]) == 1
    report = json.loads(capsys.readouterr().out)[0]
    assert report["blocking"] is True
    assert report["ok"] is False
