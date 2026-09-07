# 审查结果 Schema

reviewer 应返回一个非空 JSON 对象或数组。最推荐的对象格式是：

```json
{
  "status": "complete",
  "findings": [
    {
      "severity": "S2",
      "category": "consistency",
      "location": "正文/第05章-标题.md:42",
      "evidence": "可核对的原文或事实证据",
      "issue": "问题描述",
      "fix": "可执行的修复方向"
    }
  ],
  "notes": []
}
```

`status` 可为 `complete` 或 `incomplete`。`findings` 中每项必须包含
`severity`、`category`、`location`、`evidence`、`issue`、`fix`。允许使用数组根
格式兼容旧 reviewer；但不能把自然语言总结伪装成独立 reviewer 结果。

`review-pipeline` 只负责读取、落盘和展示，不替 reviewer 判断内容是否正确。
文件不存在、JSON 损坏、结果为空或 reviewer 未运行时，指标必须为
`unverified`。
