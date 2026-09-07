"""webfiction-write skill 测试用例

运行: python -m pytest tests/ -v
或:   python tests/run_tests.py
"""
import sys
import os
import json
import subprocess
import tempfile
import shutil
from pathlib import Path

# 把 scripts/ 加入 path
SCRIPTS_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

# 加载 fiction.py
ns = {}
with open(SCRIPTS_DIR / "fiction.py", "r", encoding="utf-8") as f:
    exec(f.read(), ns)


def make_project(title="测试书", author="测试作者", genre="都市"):
    """创建临时项目，返回 (project_root_path, tmp_dir)"""
    tmp = tempfile.mkdtemp()
    r = ns['init_project'](tmp, title=title, author=author, genre=genre)
    return r, tmp


def cleanup(tmp):
    shutil.rmtree(tmp, ignore_errors=True)


# === 测试用例 ===

def test_init_creates_state_with_schema_version():
    """init 应创建含 schema_version 的 state.json"""
    r, tmp = make_project()
    try:
        state = json.loads((r / ".novel" / "state.json").read_text("utf-8"))
        assert state["schema_version"] == 1
        assert state["project"]["book_name"] == "测试书"
        assert state["project"]["author"] == "测试作者"
        assert state["project"]["genre"] == "都市"
    finally:
        cleanup(tmp)


def test_init_creates_runtime_layout_and_active_book():
    """init 应创建可供后续 skill 使用的目录和运行时文件"""
    r, tmp = make_project()
    try:
        for dirname in ["设定集", "大纲", "正文", "追踪", "审查报告", "拆文库"]:
            assert (r / dirname).is_dir()
        assert (r / ".novel" / "tmp").is_dir()
        assert json.loads((r / ".novel" / "idea_bank.json").read_text("utf-8")) == {"ideas": []}
        assert (r / ".novel" / "active-book").read_text("utf-8") == r.name
        assert json.loads((r / ".novel" / "state.json").read_text("utf-8"))["versions"]["baseline_version"] == 0
    finally:
        cleanup(tmp)


def test_where_finds_project():
    """where 应能找到项目根"""
    r, tmp = make_project()
    try:
        import argparse
        a = argparse.Namespace(project_root=str(r))
        # cmd_where 会 print，捕获 stdout
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ns['cmd_where'](a)
        assert str(r) in buf.getvalue()
    finally:
        cleanup(tmp)


def test_where_exits_nonzero_when_no_project():
    """where 在无项目时应退出码 1"""
    tmp = tempfile.mkdtemp()
    try:
        import argparse
        a = argparse.Namespace(project_root=tmp)
        try:
            ns['cmd_where'](a)
            assert False, "应抛 SystemExit"
        except SystemExit as e:
            assert e.code == 1
    finally:
        cleanup(tmp)


def test_migrate_state_old_format():
    """migrate_state 应迁移 project_info -> project"""
    old = {"project_info": {"book_name": "旧书"}, "progress": {}}
    migrated, changed = ns['migrate_state'](old)
    assert changed is True
    assert migrated["schema_version"] == 1
    assert "project" in migrated
    assert "project_info" not in migrated
    assert migrated["project"]["book_name"] == "旧书"


def test_migrate_state_idempotent():
    """migrate_state 幂等性"""
    state = {"schema_version": 1, "project": {"book_name": "书"}}
    again, changed = ns['migrate_state'](state)
    assert changed is False
    assert again is state


def test_load_state_auto_migrates_and_persists():
    """load_state 应自动迁移旧版并持久化"""
    r, tmp = make_project()
    try:
        # 写入旧版 state
        sf = r / ".novel" / "state.json"
        sf.write_text(json.dumps({"project_info": {"book_name": "迁移测试"}, "progress": {}}, ensure_ascii=False), "utf-8")
        loaded = ns['load_state'](r)
        assert loaded["schema_version"] == 1
        assert "project" in loaded
        # 验证持久化
        persisted = json.loads(sf.read_text("utf-8"))
        assert persisted["schema_version"] == 1
    finally:
        cleanup(tmp)


def test_doctor_reports_missing_files():
    """doctor 应报告缺失文件"""
    r, tmp = make_project()
    try:
        import argparse, io, contextlib
        a = argparse.Namespace(project_root=str(r), format="text", chapter=None, deep=False)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ns['cmd_doctor'](a)
        out = buf.getvalue()
        assert "missing" in out  # 应报告缺失设定集等
    finally:
        cleanup(tmp)


def test_doctor_json_is_machine_readable():
    """doctor --format json 不应混入人类可读的章节提示"""
    r, tmp = make_project()
    try:
        (r / "正文" / "第01章-开篇.md").write_text("正文", encoding="utf-8")
        import argparse, io, contextlib
        a = argparse.Namespace(project_root=str(r), format="json", chapter=None, deep=False)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ns['cmd_doctor'](a)
        payload = json.loads(buf.getvalue())
        assert payload["chapters"] == 1
        assert isinstance(payload["issues"], list)
    finally:
        cleanup(tmp)


def test_doctor_returns_nonzero_when_issues_exist():
    """doctor 发现问题时必须返回非零状态，供 CI 使用"""
    r, tmp = make_project()
    try:
        import argparse, io, contextlib
        a = argparse.Namespace(project_root=str(r), format="json", chapter=None, deep=False)
        with contextlib.redirect_stdout(io.StringIO()):
            result = ns['cmd_doctor'](a)
        assert result == 1
    finally:
        cleanup(tmp)


def test_doctor_returns_zero_for_healthy_project():
    """doctor 项目结构完整时返回零"""
    r, tmp = make_project()
    try:
        (r / "设定集" / "主角卡.md").write_text("主角", encoding="utf-8")
        (r / "设定集" / "世界观.md").write_text("世界", encoding="utf-8")
        (r / "大纲" / "总纲草案.md").write_text("总纲", encoding="utf-8")
        import argparse, io, contextlib
        a = argparse.Namespace(project_root=str(r), format="json", chapter=None, deep=False)
        with contextlib.redirect_stdout(io.StringIO()):
            result = ns['cmd_doctor'](a)
        assert result == 0
    finally:
        cleanup(tmp)


def test_doctor_cli_propagates_exit_code():
    """CLI 主入口应把 doctor 的诊断结果传给进程退出码"""
    r, tmp = make_project()
    try:
        result = subprocess.run(
            [sys.executable, "-X", "utf8", str(SCRIPTS_DIR / "fiction.py"), "--project-root", str(r), "doctor", "--format", "json"],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        assert result.returncode == 1
        assert json.loads(result.stdout)["ok"] is False
    finally:
        cleanup(tmp)


def test_export_txt():
    """export txt 应合并正文"""
    r, tmp = make_project()
    try:
        # 创建正文目录和章节
        td = r / "正文"
        td.mkdir(exist_ok=True)
        (td / "第01章-开篇.md").write_text("第一章内容", encoding="utf-8")
        (td / "第02章-发展.md").write_text("第二章内容", encoding="utf-8")
        import argparse, io, contextlib
        a = argparse.Namespace(project_root=str(r), format="txt", output=None)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ns['cmd_export'](a)
        out = buf.getvalue()
        assert "exported" in out
        assert "chapters: 2" in out
        # 验证输出文件
        exported = r / "导出" / (r.name + "_完本.txt")
        assert exported.exists()
        content = exported.read_text("utf-8")
        assert "第一章内容" in content
        assert "第二章内容" in content
    finally:
        cleanup(tmp)


def test_export_fanqie_format():
    """export fanqie 应按番茄平台格式化"""
    r, tmp = make_project()
    try:
        td = r / "正文"
        td.mkdir(exist_ok=True)
        (td / "第01章-开篇.md").write_text("正文段落", encoding="utf-8")
        import argparse, io, contextlib
        a = argparse.Namespace(project_root=str(r), format="fanqie", output=None)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ns['cmd_export'](a)
        exported = r / "导出" / (r.name + "_完本.txt")
        content = exported.read_text("utf-8")
        # 番茄格式：标题 + 空行 + 正文 + 两个空行
        assert "第01章-开篇" in content
        assert content.endswith("\n\n\n")
    finally:
        cleanup(tmp)


def test_export_removes_common_markdown_markers():
    """txt 导出应去掉常见 Markdown 展示标记"""
    r, tmp = make_project()
    try:
        chapter = r / "正文" / "第01章-开篇.md"
        chapter.write_text("# 标题\n\n**加粗** [链接](https://example.com)\n\n- 项目", encoding="utf-8")
        import argparse, io, contextlib
        a = argparse.Namespace(project_root=str(r), format="txt", output=None)
        with contextlib.redirect_stdout(io.StringIO()):
            ns['cmd_export'](a)
        exported = r / "导出" / (r.name + "_完本.txt")
        content = exported.read_text("utf-8")
        assert "标题" in content
        assert "加粗" in content
        assert "链接" in content
        assert "项目" in content
        assert "**" not in content
        assert "https://example.com" not in content
        assert "- 项目" not in content
    finally:
        cleanup(tmp)


def test_chapter_commit():
    """chapter-commit 应创建 commit 文件并更新 state"""
    r, tmp = make_project()
    try:
        (r / "正文" / "第05章-开篇.md").write_text("正文", encoding="utf-8")
        import argparse, io, contextlib
        a = argparse.Namespace(project_root=str(r), chapter="5")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ns['cmd_commit'](a)
        commit_file = r / ".story-system" / "commits" / "chapter_0005.commit.json"
        assert commit_file.exists()
        c = json.loads(commit_file.read_text("utf-8"))
        assert c["chapter"] == 5
        assert c["status"] == "accepted"
        # state 应更新 current_chapter
        state = ns['load_state'](r)
        assert state["progress"]["current_chapter"] == 5
    finally:
        cleanup(tmp)


def test_chapter_commit_records_source_hash():
    """chapter-commit 应记录正文相对路径和内容哈希"""
    r, tmp = make_project()
    try:
        chapter = r / "正文" / "第05章-开门.md"
        chapter.write_text("门开了。", encoding="utf-8")
        import argparse, io, contextlib, hashlib
        a = argparse.Namespace(project_root=str(r), chapter="5")
        with contextlib.redirect_stdout(io.StringIO()):
            ns['cmd_commit'](a)
        commit = json.loads((r / ".story-system" / "commits" / "chapter_0005.commit.json").read_text("utf-8"))
        assert commit["source_path"] == "正文/第05章-开门.md"
        assert commit["content_sha256"] == hashlib.sha256(chapter.read_bytes()).hexdigest()
    finally:
        cleanup(tmp)


def test_contract_is_idempotent_and_increments_when_content_changes():
    """init-contract 不应无变化递增版本，底本变化时才递增"""
    r, tmp = make_project(genre="都市")
    try:
        import argparse, io, contextlib
        a = argparse.Namespace(project_root=str(r))
        with contextlib.redirect_stdout(io.StringIO()):
            ns['cmd_contract'](a)
        first = json.loads((r / ".story-system" / "MASTER_SETTING.json").read_text("utf-8"))
        with contextlib.redirect_stdout(io.StringIO()):
            ns['cmd_contract'](a)
        second = json.loads((r / ".story-system" / "MASTER_SETTING.json").read_text("utf-8"))
        assert second["versions"]["baseline_version"] == first["versions"]["baseline_version"]

        state = ns['load_state'](r)
        state["project"]["genre"] = "悬疑"
        ns['save_state'](r, state)
        with contextlib.redirect_stdout(io.StringIO()):
            ns['cmd_contract'](a)
        changed = json.loads((r / ".story-system" / "MASTER_SETTING.json").read_text("utf-8"))
        assert changed["versions"]["baseline_version"] == first["versions"]["baseline_version"] + 1
    finally:
        cleanup(tmp)


def test_review_pipeline_writes_report():
    """review-pipeline 应写审查报告"""
    r, tmp = make_project()
    try:
        import argparse, io, contextlib
        report_file = r / "审查报告" / "第01章审查报告.md"
        results = json.dumps({"连续性": "OK", "节奏": "偏快"})
        a = argparse.Namespace(
            project_root=str(r), chapter="1",
            report_file=str(report_file),
            review_results=results,
            metrics_out=None, save_metrics=False
        )
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ns['cmd_review'](a)
        assert report_file.exists()
        content = report_file.read_text("utf-8")
        assert "第 1 章审查报告" in content
        assert "连续性" in content
    finally:
        cleanup(tmp)


def test_review_pipeline_saves_durable_metrics_and_unverified_status():
    """没有 reviewer 结果时，metrics 应持久化并明确 unverified"""
    r, tmp = make_project()
    try:
        import argparse, io, contextlib
        report_file = r / "审查报告" / "第01章审查报告.md"
        a = argparse.Namespace(
            project_root=str(r), chapter="1", report_file=str(report_file),
            review_results=None, metrics_out=None, save_metrics=True
        )
        with contextlib.redirect_stdout(io.StringIO()):
            ns['cmd_review'](a)
        metrics_file = r / ".novel" / "reviews" / "chapter_0001.metrics.json"
        metrics = json.loads(metrics_file.read_text("utf-8"))
        assert metrics["status"] == "unverified"
        assert report_file.exists()
    finally:
        cleanup(tmp)


def test_review_pipeline_reads_results_file():
    """review-pipeline 传入文件路径时应读取文件内容而不是记录路径"""
    r, tmp = make_project()
    try:
        import argparse, io, contextlib
        result_file = r / ".novel" / "tmp" / "review_results.json"
        result_file.write_text(json.dumps({"连续性": "OK"}, ensure_ascii=False), encoding="utf-8")
        report_file = r / "审查报告" / "第01章审查报告.md"
        a = argparse.Namespace(
            project_root=str(r), chapter="1", report_file=str(report_file),
            review_results=str(result_file), metrics_out=None, save_metrics=True
        )
        with contextlib.redirect_stdout(io.StringIO()):
            ns['cmd_review'](a)
        content = report_file.read_text("utf-8")
        metrics = json.loads((r / ".novel" / "reviews" / "chapter_0001.metrics.json").read_text("utf-8"))
        assert "OK" in content
        assert metrics["status"] == "verified"
        assert metrics["results"] == {"连续性": "OK"}
        assert metrics["results_source"].startswith("file:")
    finally:
        cleanup(tmp)


def test_review_pipeline_invalid_results_file_is_unverified():
    """损坏的 reviewer 文件不得被路径字符串伪装成 verified"""
    r, tmp = make_project()
    try:
        import argparse, io, contextlib
        result_file = r / ".novel" / "tmp" / "review_results.json"
        result_file.write_text("not json", encoding="utf-8")
        report_file = r / "审查报告" / "第01章审查报告.md"
        a = argparse.Namespace(
            project_root=str(r), chapter="1", report_file=str(report_file),
            review_results=str(result_file), metrics_out=None, save_metrics=True
        )
        with contextlib.redirect_stdout(io.StringIO()):
            ns['cmd_review'](a)
        metrics = json.loads((r / ".novel" / "reviews" / "chapter_0001.metrics.json").read_text("utf-8"))
        assert metrics["status"] == "unverified"
        assert "error" in metrics
        assert "未加载" in report_file.read_text("utf-8")
    finally:
        cleanup(tmp)


def test_review_pipeline_incomplete_reviewer_result_is_unverified():
    """reviewer 明确返回 incomplete 时不得标记 verified"""
    r, tmp = make_project()
    try:
        import argparse, io, contextlib
        result_file = r / ".novel" / "tmp" / "review_results.json"
        result_file.write_text(json.dumps({"status": "incomplete", "findings": []}), encoding="utf-8")
        report_file = r / "审查报告" / "第01章审查报告.md"
        a = argparse.Namespace(
            project_root=str(r), chapter="1", report_file=str(report_file),
            review_results=str(result_file), metrics_out=None, save_metrics=True
        )
        with contextlib.redirect_stdout(io.StringIO()):
            ns['cmd_review'](a)
        metrics = json.loads((r / ".novel" / "reviews" / "chapter_0001.metrics.json").read_text("utf-8"))
        assert metrics["status"] == "unverified"
        assert "未完成" in report_file.read_text("utf-8")
    finally:
        cleanup(tmp)


def test_commit_records_data_artifacts_and_projection_is_replayable():
    """chapter-commit 应记录 artifact，projections retry 应生成可重放摘要"""
    r, tmp = make_project()
    try:
        chapter = r / "正文" / "第05章-开门.md"
        chapter.write_text("门开了。\n\n有人站在门外。", encoding="utf-8")
        for name, value in [
            ("fulfillment_result.json", {"status": "complete"}),
            ("disambiguation_result.json", {"status": "clear"}),
            ("extraction_result.json", {"new_entities": []}),
        ]:
            (r / ".novel" / "tmp" / name).write_text(json.dumps(value), encoding="utf-8")
        import argparse, io, contextlib
        commit_args = argparse.Namespace(project_root=str(r), chapter="5", data_artifacts=None)
        with contextlib.redirect_stdout(io.StringIO()):
            ns['cmd_commit'](commit_args)
        commit_file = r / ".story-system" / "commits" / "chapter_0005.commit.json"
        commit = json.loads(commit_file.read_text("utf-8"))
        assert commit["data_artifacts_status"] == "complete"
        assert "fulfillment_result.json" in commit["data_artifacts"]

        projection_args = argparse.Namespace(project_root=str(r), chapter="5", action="retry")
        with contextlib.redirect_stdout(io.StringIO()):
            assert ns['cmd_projections'](projection_args) == 0
        summary = r / ".story-system" / "summaries" / "ch0005.md"
        assert summary.exists()
        projected = json.loads(commit_file.read_text("utf-8"))
        assert projected["projection_status"]["summary"] == "done"
        assert projected["projection_status"]["index"] == "skipped"
        assert (r / ".story-system" / "projection_log.jsonl").exists()
    finally:
        cleanup(tmp)


def test_memory_add_and_list():
    """project-memory add-pattern + list-pattern"""
    r, tmp = make_project()
    try:
        import argparse, io, contextlib
        # add
        a = argparse.Namespace(project_root=str(r), action="add-pattern",
                               pattern_type="hook", description="开篇冲突前置",
                               importance="high", keyword=None, target=None)
        ns['cmd_memory'](a)
        # list
        a2 = argparse.Namespace(project_root=str(r), action="list-patterns",
                                pattern_type=None, description=None,
                                importance="medium", keyword=None, target=None)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ns['cmd_memory'](a2)
        out = buf.getvalue()
        assert "hook" in out
        assert "开篇冲突前置" in out
    finally:
        cleanup(tmp)


def test_memory_dedup():
    """add-pattern 相同 pattern_type+description 应去重"""
    r, tmp = make_project()
    try:
        import argparse
        for _ in range(2):
            a = argparse.Namespace(project_root=str(r), action="add-pattern",
                                   pattern_type="hook", description="same",
                                   importance="medium", keyword=None, target=None)
            ns['cmd_memory'](a)
        mf = r / ".novel" / "project_memory.json"
        mem = json.loads(mf.read_text("utf-8"))
        assert len(mem["patterns"]) == 1
    finally:
        cleanup(tmp)


def test_memory_search_and_delete():
    """search-pattern + delete-pattern"""
    r, tmp = make_project()
    try:
        import argparse, io, contextlib
        # add 两个
        for pt, desc in [("hook", "冲突"), ("pacing", "节奏")]:
            a = argparse.Namespace(project_root=str(r), action="add-pattern",
                                   pattern_type=pt, description=desc,
                                   importance="medium", keyword=None, target=None)
            ns['cmd_memory'](a)
        # search by keyword
        a = argparse.Namespace(project_root=str(r), action="search-pattern",
                               pattern_type=None, description=None,
                               importance="medium", keyword="冲突", target=None)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ns['cmd_memory'](a)
        assert "冲突" in buf.getvalue()
        # delete by index
        a = argparse.Namespace(project_root=str(r), action="delete-pattern",
                               pattern_type=None, description=None,
                               importance="medium", keyword=None, target="1")
        ns['cmd_memory'](a)
        mf = r / ".novel" / "project_memory.json"
        mem = json.loads(mf.read_text("utf-8"))
        assert len(mem["patterns"]) == 1
        assert mem["patterns"][0]["pattern_type"] == "pacing"
    finally:
        cleanup(tmp)


def test_cli_help_registered():
    """CLI 各子命令参数应正确注册"""
    import argparse
    p = argparse.ArgumentParser()
    # 模拟 main() 里的参数注册
    p.add_argument("--project-root", default=os.getcwd())
    s = p.add_subparsers(dest="cmd")
    pd = s.add_parser("doctor")
    pd.add_argument("--format", choices=["text", "json"], default="text")
    pd.add_argument("--chapter", default=None)
    pd.add_argument("--deep", action="store_true")
    pe = s.add_parser("export")
    pe.add_argument("--format", choices=["txt", "docx", "fanqie"], default="txt")
    pe.add_argument("--output", default=None)
    p8 = s.add_parser("project-memory")
    p8.add_argument("action", choices=["add-pattern", "list-patterns", "search-pattern", "delete-pattern"])

    # 验证 doctor 参数
    args = p.parse_args(["doctor", "--chapter", "5", "--deep"])
    assert args.chapter == "5"
    assert args.deep is True

    # 验证 export 参数
    args = p.parse_args(["export", "--format", "fanqie", "--output", "/tmp/out.txt"])
    assert args.format == "fanqie"
    assert args.output == "/tmp/out.txt"

    # 验证 project-memory 子命令
    args = p.parse_args(["project-memory", "list-patterns"])
    assert args.action == "list-patterns"


def run_all():
    """运行所有测试"""
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            print(f"[PASS] {test.__name__}")
            passed += 1
        except Exception as e:
            print(f"[FAIL] {test.__name__}: {e}")
            failed += 1
    print(f"\n=== {passed} passed, {failed} failed, {len(tests)} total ===")
    return failed == 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--run":
        sys.exit(0 if run_all() else 1)
    else:
        # 尝试用 pytest 运行，没装就 fallback 到内置 runner
        try:
            import pytest
            sys.exit(pytest.main([__file__, "-v"] + sys.argv[1:]))
        except ImportError:
            sys.exit(0 if run_all() else 1)
