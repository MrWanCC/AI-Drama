# data-agent artifacts 与 projection 边界

Deep 写作或修改流程可以让主线 LLM 生成以下三份 JSON 文件到 `.novel/tmp/`：

- `fulfillment_result.json`：本章目标完成度与证据；
- `disambiguation_result.json`：需要裁定的歧义及选择；
- `extraction_result.json`：本章新增人物、地点、物件、规则、事件等事实。

然后执行：

```bash
python -X utf8 "${SCRIPTS_DIR}/fiction.py" --project-root "${PROJECT_ROOT}" chapter-commit \
  --chapter {章号} --data-artifacts "${PROJECT_ROOT}/.novel/tmp"
python -X utf8 "${SCRIPTS_DIR}/fiction.py" --project-root "${PROJECT_ROOT}" projections retry \
  --chapter {章号}
```

`chapter-commit` 会把已成功读取的 JSON 原样记录在 commit 中，并标记
`complete`、`partial` 或 `missing`；缺失 artifact 不会被伪装成完整。
`projections retry` 只负责从已提交正文重建 `.story-system/summaries/` 并写入
`projection_log.jsonl`。index、memory、vector 等需要宿主服务的投影标为 `skipped`，
不能在没有实际实现时声称已刷新。
