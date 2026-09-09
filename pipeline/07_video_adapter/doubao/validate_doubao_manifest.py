# -*- coding: utf-8 -*-
"""
豆包视频生成清单校验脚本
用法：
    python validate_doubao_manifest.py [manifest.json]
默认校验 pipeline/07_video_adapter/doubao/EP001-doubao-manifest.json
输出：PASS 或 FAIL（附错误明细）
"""
import json
import os
import sys

# 定位 manifest 路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MANIFEST = os.path.join(SCRIPT_DIR, "EP001-doubao-manifest.json")
# 项目根目录（pipeline/07_video_adapter/doubao -> 上溯 4 层）
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))


def resolve_path(p):
    """把 manifest 里的相对路径（refs/...）解析为项目根下的绝对路径"""
    if os.path.isabs(p):
        return p
    return os.path.normpath(os.path.join(ROOT_DIR, p))


def validate(manifest_path):
    errors = []
    warnings = []

    if not os.path.exists(manifest_path):
        return "FAIL", [f"manifest 文件不存在: {manifest_path}"], []

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as e:
        return "FAIL", [f"manifest JSON 解析失败: {e}"], []

    shots = manifest.get("shots", [])
    if not shots:
        return "FAIL", ["manifest 中没有 shots"], []

    shot_ids = set()
    total_refs_checked = 0

    for i, shot in enumerate(shots, 1):
        sid = shot.get("shotId", f"<第{i}镜缺 shotId>")

        # 1. shotId 存在且唯一
        if not shot.get("shotId"):
            errors.append(f"第{i}镜缺少 shotId")
        elif shot["shotId"] in shot_ids:
            errors.append(f"shotId 重复: {shot['shotId']}")
        else:
            shot_ids.add(shot["shotId"])

        # 2. duration 合法
        dur = shot.get("duration")
        if not isinstance(dur, (int, float)):
            errors.append(f"{sid}: duration 缺失或类型错误 ({dur})")
        elif dur <= 0 or dur > 120:
            errors.append(f"{sid}: duration 非法 ({dur})，应在 0~120 之间")

        # 3. prompt 非空
        prompt = shot.get("prompt", "")
        if not prompt or not str(prompt).strip():
            errors.append(f"{sid}: prompt 为空")

        # 4. negativePrompt 非空（可选但建议）
        if not shot.get("negativePrompt", "").strip():
            warnings.append(f"{sid}: negativePrompt 为空（建议填写）")

        # 5. referenceImages 文件存在
        refs = shot.get("referenceImages", [])
        if not isinstance(refs, list):
            errors.append(f"{sid}: referenceImages 不是数组")
            refs = []
        for ref in refs:
            abs_ref = resolve_path(ref)
            total_refs_checked += 1
            if not os.path.exists(abs_ref):
                errors.append(f"{sid}: referenceImages 文件不存在 -> {ref}")

        # 6. 空角色引用检查
        # 若 characters 元数据非空但 referenceImages 里没有对应角色图，说明映射缺失
        chars = shot.get("_characters", [])
        for c in chars:
            # 简单启发：检查 refs 里是否包含该角色主图文件名
            expected_kw = f"{c}_"
            if not any(expected_kw in r for r in refs):
                errors.append(f"{sid}: 角色 {c} 在 referenceImages 中缺少对应参考图")

    return ("PASS" if not errors else "FAIL"), errors, warnings


def main():
    manifest_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MANIFEST
    print(f"校验: {manifest_path}")
    print("-" * 60)
    status, errors, warnings = validate(manifest_path)
    if warnings:
        for w in warnings:
            print(f"[WARN] {w}")
    if errors:
        for e in errors:
            print(f"[FAIL] {e}")
        print("-" * 60)
        print(f"结果: FAIL  （{len(errors)} 个错误）")
        sys.exit(1)
    else:
        # 统计
        with open(manifest_path, "r", encoding="utf-8") as f:
            m = json.load(f)
        shots = m.get("shots", [])
        print(f"镜头总数: {len(shots)}")
        print(f"总时长: {sum(s.get('duration', 0) for s in shots)}s")
        print(f"平均时长: {sum(s.get('duration', 0) for s in shots)/len(shots):.1f}s")
        print("-" * 60)
        print("结果: PASS")
        sys.exit(0)


if __name__ == "__main__":
    main()
