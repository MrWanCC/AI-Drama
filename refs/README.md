# refs/ 视觉资产目录规范

第一批视觉资产的生产目录。**当前只建立目录规范，不生成任何图片。**

## 目录结构

```
refs/
├─ characters/
│  ├─ C01_shenchuan.png           # 沈川 —— 主参考图（正面半身基准）
│  └─ C06_laogongjiang.png        # 老工匠 —— 主参考图（半身主图）
├─ scenes/
│  ├─ S01_chaisang_shipyard.png        # 柴桑船坊 · 晨雾主视角
│  └─ S01_chaisang_shipyard_night.png  # 柴桑船坊 · 油灯夜（同一空间，换光照）
└─ props/
   ├─ P01_shipyard_ledger.png     # 修船账册
   ├─ P02_military_order.png      # 东吴军令
   └─ P03_identity_token.png      # 船坊小吏铜牌
```

## 命名规范

- **角色**：`{角色ID}_{拼音名}.png`，如 `C01_shenchuan.png`
- **场景**：`{场景ID}_{拼音名}.png`，光照变体加 `_night` 后缀
- **道具**：`{道具ID}_{英文名}.png`，如 `P01_shipyard_ledger.png`

## 画风统一约束（半写实厚涂）

所有资产生成提示词必须统一使用（来自 `pipeline/03_art` 的 realistic 预设）：

```
semi-realistic painterly cinematic illustration,
Three Kingdoms late Eastern Han aesthetic,
cinematic composition,
painterly rendering,
grounded anatomy,
weathered realistic materials,
visible fabric and wood texture,
dramatic but natural lighting
```

**禁止**：`live-action` / `photorealistic` / `3D game render` / `plastic CG`
**允许保留**：`cinematic` / `film composition` / `cinematic lighting`

## 文字/数字处理规则（硬性）

- 军令正文、铜牌文字、账册具体数字（350/300）、木板五字 —— **一律不要求 AI 绘制**
- 只生成**无可读正文的视觉载体**：
  - 军令 → `aged military order with vermilion seal`
  - 铜牌 → `weathered bronze identity token`
  - 账册 → `old ledger with suspicious overwritten ink`
- 具体汉字/数字走 **postOverlay**（后期叠加），记录在各镜头 `postOverlayText` 字段

## 场景一致性约束（硬性）

- `S01_chaisang_shipyard.png` 与 `S01_chaisang_shipyard_night.png` **必须保持同一空间结构**
- 夜景只是换光照（昏黄油灯），**不允许像换了一个船坊**：码头、木棚、料堆、待修战船阵列的位置和形态必须一致

## 使用方式（ComfyUI）

各镜头 `referenceImages` 字段按以下规则自动引用本目录：

| 引用类型 | 规则 |
|---|---|
| 角色 | 按 `characters` 字段列出对应角色主图 |
| 场景 | 按 `sceneId` + `lighting` 引用（夜戏用 `_night` 版本） |
| 道具 | 按 `props` 字段列出对应道具图 |

详见 `pipeline/06_assets/EP001-reference-assets.json`（基础资产生产清单）。
