# EP001 Pavo 生产操作清单

> 平台：**Pavo (app.pavo.al.cn)**　|　模型：**Agnes Video 2.1 Flash（图生视频） + Agnes Image 2.1 Flash（首帧）**　|　画风：**半写实厚涂、东汉末三国风格**　|　镜数：**51**

> 本清单为 Pavo 一站式平台生产清单。每镜手动上传 referenceImages.primary + referenceImages.style，按 pavoPrompt 粘贴。

---

## 操作流程（每镜重复 3 步）

1. 上传 **primary 主图**（必传，Pavo 图生视频首帧）
2. 上传 **style 场景基准图**（保持空间一致，强烈建议）
3. 复制下面 `pavoPrompt` 文本框整段，粘贴到 Pavo 输入框
4. 如有 **postOverlayText**，在 Pavo 视频生成后用剪辑工具叠加

> 前 5 镜的 `motionPrompt` 已精修，后 46 镜只翻译了运镜，生成后如不满意可单独重做。

## E01-S01　extreme-wide | 极远景 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a broken warship docked by a misty riverside, its hull pockmarked with holes and...

**参考图上传清单**：

- 主图（必传）：`refs/scenes/S01_chaisang_shipyard.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`

**运动指令**：
```
镜头完全静止。晨雾缓慢飘过破损战船，断桨和未装好的龙骨在河风中轻微晃动。
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、极远景。a broken warship docked by a misty riverside, its hull pockmarked with holes and a snapped oar, an unfinished keel jutting out, looming out of the morning fog like a collapsing wall。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S02　close | 近景特写 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**后期叠加字幕**：`军令`

**画面描述**：a weathered military order bearing a large vermilion seal slapped hard onto a wo...

**参考图上传清单**：

- 主图（必传）：`refs/props/P02_military_order.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 道具参考：`refs/props/P02_military_order.png`

**运动指令**：
```
镜头完全静止。雾气在木案上轻轻卷动，军令落在案上铺平，朱红官印在冷光中闪一下。
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a weathered military order bearing a large vermilion seal slapped hard onto a wooden desk, the red seal stain vivid against aged paper, wisps of fog curling over the wood。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S03　medium | 中景 | 难度=中

**时长**：2.9s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：an old craftsman with a hoarse scowl barking across the desk at a young clerk se...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`
- 道具参考：`refs/props/P02_military_order.png`

**运动指令**：
```
镜头完全静止。老工匠身子前倾、张口大吼，下颌绷紧、目光凌厉；对面青年小吏（沈川）被吼得微微一颤。
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。an old craftsman with a hoarse scowl barking across the desk at a young clerk seated on the far side, warped timber of the workshop behind them。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S04　medium | 中景 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk straightening from the desk, cold sweat beading his forehead, eyes...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P02_military_order.png`

**运动指令**：
```
镜头完全静止。沈川缓缓从案前直起，冷汗沿鬓角滑下，目光一行一行扫过手中军令。
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk straightening from the desk, cold sweat beading his forehead, eyes crawling line by line over the military order in his hands。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S05　medium | 中景 | 难度=低

**时长**：4.0s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**后期叠加字幕**：`三十艘 · 七日 · 军法处置`

**画面描述**：a young clerk reading a weathered military order aloud, his voice dry as if pron...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P02_military_order.png`

**运动指令**：
```
镜头缓缓推近沈川。沈川念出军令，眼眶微睁，喉头收紧，视线从纸面缓缓抬向远处的雾。
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk reading a weathered military order aloud, his voice dry as if pronouncing his own death sentence, the sealed paper held in both hands。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S06　wide | 远景 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk looking up toward a line of thirty broken warships fading into fog...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、远景。a young clerk looking up toward a line of thirty broken warships fading into fog along the dock, their hulls too damaged to count。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S07　close | 近景特写 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**后期叠加字幕**：`船坊小吏`

**画面描述**：a hand touching a weathered bronze identity token at the waist and turning it ov...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P03_identity_token.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a hand touching a weathered bronze identity token at the waist and turning it over, worn engraved marks on the bronze catching the cold light。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S08　close | 近景特写 | 难度=低

**时长**：2.0s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk's eyes tightening, his lips barely moving in an off-screen voiceov...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P03_identity_token.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a young clerk's eyes tightening, his lips barely moving in an off-screen voiceover, the bronze token still clutched in his fingers。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S09　medium | 中景 | 难度=低

**时长**：4.0s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：an old craftsman with arms folded and a cold stare, telling the young clerk the ...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。an old craftsman with arms folded and a cold stare, telling the young clerk the whole workshop is waiting on his word。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S10　medium | 中景 | 难度=中

**时长**：4.0s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Push In

**画面描述**：a young clerk leaning forward, firing questions in a strained steady voice, the ...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头缓缓推近
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk leaning forward, firing questions in a strained steady voice, the old craftsman blinking in surprise across from him。镜头运动：镜头缓缓推近。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S11　close | 近景特写 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：the old craftsman exchanging a glance with a nearby laborer, both baffled as if ...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。the old craftsman exchanging a glance with a nearby laborer, both baffled as if hearing such questions for the first time。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S12　medium | 中景 | 难度=低

**时长**：4.9s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：the old craftsman frowning, insisting seven days is seven days and the ship will...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。the old craftsman frowning, insisting seven days is seven days and the ship will be mended as it always has been。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S13　medium | 中景 | 难度=低

**时长**：3.3s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk answering back with a tight throat, refusing to be waved off

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk answering back with a tight throat, refusing to be waved off。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S14　medium | 中景 | 难度=高

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk pushing up from the desk, sweeping his eyes over blurred silhouett...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk pushing up from the desk, sweeping his eyes over blurred silhouettes of gathered craftsmen and the row of broken warships in the far fog。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S15　medium | 中景 | 难度=高

**时长**：5.1s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Push In

**画面描述**：a young clerk standing and addressing the gathered craftsmen, his voice low but ...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头缓缓推近
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk standing and addressing the gathered craftsmen, his voice low but holding the yard, the craftsmen a soft out-of-focus crowd behind him。镜头运动：镜头缓缓推近。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S16　wide | 远景 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Tracking Shot

**画面描述**：a young clerk walking along a warship, fingertips grazing its damaged hull, an o...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头跟拍
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、远景。a young clerk walking along a warship, fingertips grazing its damaged hull, an open ledger in his other hand as he scratches marks into the mud。镜头运动：镜头跟拍。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S17　medium | 中景 | 难度=低

**时长**：2.9s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk muttering a tally to himself, eyes still on the broken hull

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk muttering a tally to himself, eyes still on the broken hull。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S18　close | 近景特写 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a pair of hands crouching over scattered half-finished timbers, pressing two shi...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a pair of hands crouching over scattered half-finished timbers, pressing two ship planks together, a gap wide enough to fit a finger between them。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S19　medium | 中景 | 难度=低

**时长**：4.4s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：an old craftsman shrugging off the gap, saying they patch whichever ship is brok...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。an old craftsman shrugging off the gap, saying they patch whichever ship is broken and always have, as long as it fits。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S20　medium | 中景 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Pan Left

**画面描述**：a young clerk stepping to the timber pile, logs heaped at all angles, new and ol...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头缓缓左摇
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk stepping to the timber pile, logs heaped at all angles, new and old mixed together, several already split。镜头运动：镜头缓缓左摇。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S21　close | 近景特写 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk's fingers flipping a weathered ledger open, counting the timber ag...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a young clerk's fingers flipping a weathered ledger open, counting the timber against the marked entries, the yellowed pages catching the cold light。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S22　close | 近景特写 | 难度=低

**时长**：2.0s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk's brow knotting as the counted timber and the ledger entries refus...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a young clerk's brow knotting as the counted timber and the ledger entries refuse to match in the cold light。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S23　wide | 远景 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a few craftsmen squatting idle by a hull in the distance, tools resting on the g...

**参考图上传清单**：

- 主图（必传）：`refs/scenes/S01_chaisang_shipyard.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、远景。a few craftsmen squatting idle by a hull in the distance, tools resting on the ground, blurred and out of focus。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S24　medium | 中景 | 难度=低

**时长**：4.9s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：an old craftsman stomping up behind, voice raised, demanding what use the counti...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。an old craftsman stomping up behind, voice raised, demanding what use the counting is when the ship will not mend itself。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S25　wide | 远景 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Pan Right

**画面描述**：a young clerk pointing toward the stern where two craftsmen pry off a plank they...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头缓缓右摇
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、远景。a young clerk pointing toward the stern where two craftsmen pry off a plank they had just fastened。镜头运动：镜头缓缓右摇。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S26　medium | 中景 | 难度=低

**时长**：3.1s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk asking why the plank is being taken down again, his finger still l...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk asking why the plank is being taken down again, his finger still leveled at the stern。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S27　medium | 中景 | 难度=低

**时长**：5.3s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：an old craftsman explaining the size was wrong and redoing it is a daily chore, ...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。an old craftsman explaining the size was wrong and redoing it is a daily chore, the loose plank dangling behind him。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S28　wide | 远景 | 难度=高

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk turning to scan the whole yard, blurred craftsmen idle in the far ...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、远景。a young clerk turning to scan the whole yard, blurred craftsmen idle in the far ground, some redoing finished work, the timber that does not add up, his eyes closing once。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S29　medium | 中景 | 难度=低

**时长**：4.0s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk with lips closed in silent inner thought, the realization settling...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk with lips closed in silent inner thought, the realization settling over his face。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S30　wide | 远景 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk walking to the dock edge and pointing back at the row of broken wa...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、远景。a young clerk walking to the dock edge and pointing back at the row of broken warships。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S31　wide | 远景 | 难度=高

**时长**：5.3s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Push In

**画面描述**：a young clerk at the dock edge pointing back at the row of broken warships, layi...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头缓缓推近
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、远景。a young clerk at the dock edge pointing back at the row of broken warships, laying out the flaws one by one to an out-of-focus crowd of craftsmen seen from behind, shoulders and backs。镜头运动：镜头缓缓推近。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S32　wide | 远景 | 难度=高

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：the yard falling still, a few craftsmen in the foreground as blurred silhouettes...

**参考图上传清单**：

- 主图（必传）：`refs/scenes/S01_chaisang_shipyard.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、远景。the yard falling still, a few craftsmen in the foreground as blurred silhouettes and turned backs shuffling a half step closer。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S33　medium | 中景 | 难度=低

**时长**：3.8s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：an old craftsman's voice dropping as he asks, for the first time in earnest, whi...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。an old craftsman's voice dropping as he asks, for the first time in earnest, which task to tackle first。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S34　medium | 中景 | 难度=低

**时长**：4.7s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk answering flatly to count the hands first

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk answering flatly to count the hands first。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S35　medium | 中景 | 难度=低

**时长**：2.5s　|　**光照**：晨雾未散　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：the old craftsman staring two beats, then turning to wave the scattered craftsme...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。the old craftsman staring two beats, then turning to wave the scattered craftsmen over。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S36　medium | 中景 | 难度=低

**时长**：2.5s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk alone in a timber workshop at night, a single oil lamp pooling amb...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk alone in a timber workshop at night, a single oil lamp pooling amber light as he turns page after page of an old ledger。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S37　close | 近景特写 | 难度=低

**时长**：2.5s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**后期叠加字幕**：`船 · 人 · 料 · 序 · 账`

**画面描述**：a hand dipping a brush in ink and writing on a wooden board, then drawing a line...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a hand dipping a brush in ink and writing on a wooden board, then drawing a line beneath each mark。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S38　close | 近景特写 | 难度=低

**时长**：3.1s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk with lips closed in silent inner thought, the fresh ink marks on t...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a young clerk with lips closed in silent inner thought, the fresh ink marks on the wooden board catching the lamp glow。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S39　close | 近景特写 | 难度=低

**时长**：2.5s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**后期叠加字幕**：`三百`

**画面描述**：a finger stopping on a page where an entry has been smeared over with thick ink

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a finger stopping on a page where an entry has been smeared over with thick ink。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S40　close | 近景特写 | 难度=低

**时长**：2.5s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**后期叠加字幕**：`三百 · 三百五十`

**画面描述**：a young clerk leaning into the lamp, a thickly crossed-out entry on the ledger p...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a young clerk leaning into the lamp, a thickly crossed-out entry on the ledger page sitting against a different count on the prior page。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S41　close | 近景特写 | 难度=低

**时长**：3.6s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Push In

**画面描述**：a young clerk's face tightening as he reads the crossed-out entry against a diff...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头缓缓推近
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a young clerk's face tightening as he reads the crossed-out entry against a different count on the prior page。镜头运动：镜头缓缓推近。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S42　close | 近景特写 | 难度=低

**时长**：2.5s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：hands flipping forward and back through the ledger, the crossed-out entry nowher...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。hands flipping forward and back through the ledger, the crossed-out entry nowhere reconciled on any page。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S43　medium | 中景 | 难度=低

**时长**：2.5s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a faint sound from behind as an old craftsman appears at the doorway of the work...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a faint sound from behind as an old craftsman appears at the doorway of the workshop, holding half a lamp, face half in shadow。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S44　medium | 中景 | 难度=低

**时长**：4.0s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：an old craftsman with a tight voice warning the clerk it is late and not to look...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。an old craftsman with a tight voice warning the clerk it is late and not to look so closely at those accounts。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S45　medium | 中景 | 难度=中

**时长**：2.7s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk looking up and pinning the old man with a question

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。a young clerk looking up and pinning the old man with a question。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S46　medium | 中景 | 难度=低

**时长**：2.5s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：the old craftsman's face draining of color as he lurches to close the ledger

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。the old craftsman's face draining of color as he lurches to close the ledger。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S47　medium | 中景 | 难度=低

**时长**：3.8s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Push In

**画面描述**：an old craftsman hissing in a near-roar that this account will cost a life if it...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头缓缓推近
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、中景。an old craftsman hissing in a near-roar that this account will cost a life if it is followed。镜头运动：镜头缓缓推近。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S48　close | 近景特写 | 难度=低

**时长**：2.5s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：an old craftsman's hand hovering over the ledger then withdrawing as the lamp fl...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。an old craftsman's hand hovering over the ledger then withdrawing as the lamp flame gutters。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S49　close | 近景特写 | 难度=中

**时长**：2.0s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：a young clerk's lips moving in a single low word, his eyes fixed on the old craf...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C01_face.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C01_face.png`
- 角色参考：`refs/characters/C01_front.png`
- 角色参考：`refs/characters/C01_side.png`
- 角色参考：`refs/characters/C01_back.png`
- 角色参考：`refs/characters/C01_expressions.png`
- 角色参考：`refs/characters/C01_costume.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、近景特写。a young clerk's lips moving in a single low word, his eyes fixed on the old craftsman。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S50　wide | 远景 | 难度=低

**时长**：2.5s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：an old craftsman turning and vanishing into the dark outside the workshop, his t...

**参考图上传清单**：

- 主图（必传）：`refs/characters/C06_laogongjiang.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 角色参考：`refs/characters/C06_laogongjiang.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、远景。an old craftsman turning and vanishing into the dark outside the workshop, his throat working。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---

## E01-S51　wide | 远景 | 难度=低

**时长**：2.5s　|　**光照**：昏黄油灯夜　|　**场**：S01　|　**运镜**：Static Shot

**画面描述**：the wind surging through and nearly killing the lamp, the ledger open on the blo...

**参考图上传清单**：

- 主图（必传）：`refs/props/P01_shipyard_ledger.png`
- 场景基准：`refs/scenes/S01_chaisang_shipyard_night.png`
- 道具参考：`refs/props/P01_shipyard_ledger.png`

**运动指令**：
```
镜头完全静止
```

**Pavo 提示词（直接复制粘贴）**：
```
半写实厚涂、东汉末三国风格、画面有笔触、远景。the wind surging through and nearly killing the lamp, the ledger open on the blotted page like a black hole。镜头运动：镜头完全静止。不要水印、不要AI生成乱码文字、不要塑料感、布料和木料要有质感、面部要保留人物个性特征、不要对称脸。
```

---


## 难度分布

- 高（人群/多人调度）：**5** 镜（建议慢运镜，分段生成）
- 中（双人同框）：**4** 镜
- 低（单人物/空镜/道具）：**42** 镜