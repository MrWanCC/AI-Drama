# 豆包视频生成适配器（Doubao Video Adapter）

本目录是 **豆包（即梦）视频生成** 的适配层，让同一套 storyboard 额外产出豆包可用的生产清单。

## 设计原则

- **只新增，不改动**：不修改 `pipeline/04_script/*`、`pipeline/05_storyboard/*`、`refs/*`，只读它们并生成新的豆包清单。
- **同一套 storyboard，多平台复用**：storyboard 是唯一事实源，本适配器 + 之前的 Pavo/ComfyUI 适配器并列存在。

## 文件

| 文件 | 用途 |
|---|---|
| `EP001-doubao-manifest.json` | 51 镜豆包生产清单（结构化，程序可读） |
| `EP001-doubao-manifest.md` | 51 镜操作清单（人工复制粘贴用） |
| `validate_doubao_manifest.py` | 校验脚本，输出 PASS / FAIL |

## 生成清单字段

每镜输出：

```json
{
  "shotId": "E01-S01",
  "duration": 2,
  "referenceImages": ["refs/scenes/S01_chaisang_shipyard.png"],
  "prompt": "时代背景：……画面：……镜头：……画风：……",
  "camera": "Static Shot",
  "motion": "固定机位",
  "negativePrompt": "真人摄影，……"
}
```

另有带 `_` 前缀的追踪字段（`_sceneId`/`_sceneIndex`/`_lighting`/`_characters`/`_props`/`_postOverlay`），供校验和人工核对，不参与豆包生成。

## 参考图映射规则

| 类型 | 映射 |
|---|---|
| 角色 C01 | `refs/characters/C01_face.png` |
| 角色 C06 | `refs/characters/C06_laogongjiang.png` |
| 场景（白天） | `refs/scenes/S01_chaisang_shipyard.png` |
| 场景（夜戏） | `refs/scenes/S01_chaisang_shipyard_night.png` |
| 道具 P01 | `refs/props/P01_shipyard_ledger.png` |
| 道具 P02 | `refs/props/P02_military_order_style_ref.png` |
| 道具 P03 | `refs/props/P03_identity_token.png` |

## 画风统一

所有 prompt 末尾统一注入：

> 3D国漫半写实，电影感，高质量动画电影风格，历史氛围

负面词统一排除：真人摄影 / 现代元素 / 科幻元素 / 水印 / 清晰生成文字 等。

## 校验

```bash
python pipeline/07_video_adapter/doubao/validate_doubao_manifest.py
```

检查项：shotId 唯一、referenceImages 文件存在、duration 合法、prompt 非空、无空角色引用。

## 与其它适配器的关系

| 适配器 | 平台 | 位置 |
|---|---|---|
| Pavo | app.pavo.al.cn | `pipeline/05_storyboard/EP001-pavo-manifest.json` |
| ComfyUI | 本地部署 | `pipeline/05_storyboard/EP001-comfyui-manifest.json` |
| **豆包（本目录）** | 豆包/即梦 | `pipeline/07_video_adapter/doubao/` |

三者共享 `refs/` 目录的参考图资产。
