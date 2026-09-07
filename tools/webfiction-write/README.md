> **💡 项目说明**：本工具集的灵感来源于两套开源网文创作工具：
> [webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) 和
> [oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode)。
> 两个skill我都是用了，在我看来两者各有优势——一个强在工程化管理，一个强在情绪驱动方法论——
> 于是用 AI（Codex / Claude）将它们的设计精髓融合成了这套 fiction-* 工具集。
> 在此对原项目作者表示感谢。


> 我不懂编程，这个 skill 是用 Codex 写的。
>
# web-fiction - 网文创作工具集

用 AI 帮你写网文的工具包，从构思到完本一条龙。
面向番茄小说等免费阅读平台。核心思路：**先想好每章要让读者有什么感受，再动笔写**。

## v1.2.1 更新（2026-07-31）

- 新增 `scripts/check_prose.py`：对正文执行编码、占位符、拒答话术、控制字符和常见工程泄漏检查；风格信号只作 advisory，不冒充文学审查。
- `fiction.py` 初始化、状态、体检、底本契约、章节提交、artifact、摘要投影、审查指标和导出流程统一，旧 `project_info` 状态可迁移。
- 写作工作流增加日更停靠、单章默认、每轮最多三章、细纲不足阻断、写后证据等级和最小状态写回规则。
- 修复导入、学习、导出、审查等 skill 的命令参数和虚假能力声明；清理已发现的控制字符。
- 修复审查结果文件路径未读取、doctor 退出码误报、底本重复递增和 Markdown 标记混入导出的问题。

当前版本重点是“可核验地交付”：独立 reviewer 未调用或返回不完整时，结果必须标记为 `unverified`。

## 设计理念

- **先定情绪，再定故事**：动笔前先想好这一章要让读者感受到什么——爽？虐？甜？ suspense？
- **不用记流程**：该写大纲的时候系统会提醒你，该写正文的时候也知道
- **系统给出建议**：根据章节位置推荐普通或深度模式，但不代替用户确认
- **先报告再传播**：修改先扫描受影响范围，跨章/跨卷写回必须得到用户确认
- **证据分级**：确定性脚本、人工/模型审查、写回和 commit 分开记录，不把落盘当成通过

## 功能一览

| 技能 | 它能干什么 | 直接对 AI 说这句话就行 | 阶段 |
|------|------|------|------|
| **fiction** | 主入口，自动帮你找到对应的功能 | 「我想写小说」「帮我写书」「写网文」「开新书」 | 全局 |
| **fiction-conceive** | 和 AI 一起琢磨故事点子、设计角色、确定文风 | 「聊聊构思」「帮我设计角色」「我想写个什么样的故事」 | 准备 |
| **fiction-setup** | 自动建好写小说需要的文件夹结构 | 「建项目」「准备写书」「搭环境」「从零开始」 | 准备 |
| **fiction-start** | 正式开写前检查准备是否充分，锁定故事设定 | 「开书」「可以动笔了」「准备好了，开始吧」 | 锁定 |
| **fiction-scan** | 看看平台上现在什么类型最火 | 「扫榜」「最近流行什么」「什么火」「市场怎么样」 | 参考 |
| **fiction-analyze** | 分析热门小说是怎么写的，学人家的结构和技巧 | 「拆文」「分析这本书」「帮我拆一下」「学学这本书」 | 参考 |
| **fiction-plan** | 规划每一卷的节奏、时间线和每章的大纲 | 「规划」「做大纲」「后面怎么写」「帮我规划一下」 | 写作前 |
| **fiction-write** | 写正文 + 章节修改（写作 Normal/Deep 双模式 + 修改 Re-craft/Rewrite 两种内建模式） | 「写第X章」「续写」「接着写」「修改第X章」「重写」「回炉」 | 核心 |
| **fiction-review** | 帮你看写得怎么样（可以看一章、多章或整卷） | 「审查」「帮我看下写得怎么样」「审一下」 | 质量 |
| **fiction-polish** | 让文字更自然，去掉 AI 味 | 「润色」「去AI味」「这篇太AI了」「帮我顺一下文字」 | 质量 |
| **fiction-query** | 问系统角色叫什么、设定是什么、前面埋了什么伏笔 | 「查角色」「查设定」「什么状态」「那个角色叫啥来着」 | 全局 |
| **fiction-learn** | 把写得好的写法存下来，以后继续用 | 「记住这个写法」「这招存起来」「以后都这么写」 | 全局 |
| **fiction-doctor** | 检查项目有没有文件缺失、设定是否完整 | 「体检」「帮我看看项目有没有问题」「检查一下」 | 管理 |
| **fiction-export** | 写完后导出全文，归档保存 | 「导出」「完本」「导出txt」「我要完本了」 | 收尾 |
| **fiction-import** | 把以前写的小说导入到这套工具里 | 「导入」「我有现成的稿子」「把我的书导进来」 | 辅助 |

## 安装

把 `skills/` 文件夹安装到 Codex，推荐让 AI 帮你做：

### 方法一：让 AI 自动装（推荐）

把这个项目下载到电脑上，然后对 Codex 说：

> 「请把我项目里 skills/ 目录下的技能安装到 Codex」

AI 会自动完成安装。

### 方法二：自己手动装

本工具需要同时安装 skills/ 和 scripts/ 两个目录。
推荐用方法一（让 AI 帮你装），AI 会自动处理依赖关系。

手动安装命令（需要整个仓库目录）：

```bash
# macOS / Linux
cp -r skills/* ~/.codex/skills/
cp -r scripts/* ~/.codex/scripts/

# Windows (PowerShell)
Copy-Item -Path "skills/*" -Destination "$env:USERPROFILE\.codex\skills\" -Recurse -Force
Copy-Item -Path "scripts/*" -Destination "$env:USERPROFILE\.codex\scripts\" -Recurse -Force
```

### 依赖

- Python 3.8+（`scripts/` 初始化、体检、导出、提交和检查功能需要）
- `.docx` 导出可选安装 `python-docx`；未安装时脚本会明确回退为 `.txt`
- 扫榜功能按平台可选使用 `browser-cdp`/Chrome；没有浏览器能力时只能使用脚本支持的平台或基于已有材料分析

安装后建议先验证：

```bash
python -X utf8 scripts/check_encoding.py .
python -X utf8 scripts/check_prose.py --check 正文/第01章-标题.md
```

### Windows 用户注意

SKILL.md 中的脚本使用 bash 语法（`export`、`$(...)`、`${VAR:-default}`），Windows 用户需要以下任一环境：

- **Git Bash**（推荐，安装 Git for Windows 时自带）
- **WSL**（Windows Subsystem for Linux）
- **MSYS2** 或 **Cygwin**

PowerShell 和 CMD 无法直接运行这些脚本。建议安装 [Git for Windows](https://git-scm.com/download/win) 后使用自带的 Git Bash。

### 环境变量兼容性

本工具同时兼容 **Codex** 和 **Claude Code** 两种环境。SKILL.md 中的脚本会按以下优先级查找环境变量：

- 项目根目录：先查 `CODEX_PROJECT_DIR`，没有则查 `CLAUDE_PROJECT_DIR`，都没有则用 `$PWD`
- 插件根目录：先查 `CODEX_PLUGIN_ROOT`，没有则查 `CLAUDE_PLUGIN_ROOT`

无论用哪种环境都能正常工作，无需额外配置。

## 快速上手

不需要记命令，直接跟 AI 聊天就行：

```
直接说「帮我建个项目」      → 自动创建项目文件夹
直接说「聊聊构思」          → 和 AI 聊你的小说点子
直接说「开书」              → 正式开写前的准备工作
直接说「规划一下」          → 规划第 1 卷怎么安排
直接说「写第一章」          → 开始写第一章（系统推荐模式并等待确认）
直接说「修改第5章」        → 进入修改模式（先判断润色/大改/重写）
```

### 完整写作流程

```
构思阶段：题材/主角/冲突/文风
     ↓  （可以穿插扫榜看什么火、拆文学写法）
conceive → 和 AI 一起打磨构思
     ↓
start    → 检查准备 → 锁定设定 → 建好故事底稿
     ↓
plan     → 卷的节奏安排 → 时间线 → 每章大纲
     ↓
write    → 开始写作（系统推荐模式、检查细纲并在章后停靠）
     ↓
write（修改模式） → 改动后报告后续影响，确认后才传播
     ↓
review   → 质量检查（可单章/多章/整卷）
polish   → 润色，去掉 AI 味
     ↓
export   → 写完导出全文
```

## 核心功能说明

### 普通模式 vs 深度模式

写每章时系统根据位置推荐方式，由用户确认：

| 什么时候用 | 用哪种模式 | 什么意思 |
|------|------|------|
| 第一章 / 每卷开头结尾 / 高潮情节 / 重要节点 | **深度模式** | 增加底本、审查产物和状态核对；实际写回按证据执行 |
| 普通推进剧情的章节 | **普通模式** | 标准写作、确定性检查和最小状态更新 |

### 系统自动提醒

写完第 1/5/10 章、每卷最后一章时，系统会主动弹出建议，不用自己记。

### 三种修改强度

| 修改方式 | 改剧情？ | 自动检查后续影响？ | 调用方式 | 适用场景 |
|------|---------|-----------|---------|------|
| 小修（润色） | ❌ | ❌ | `fiction-polish` | 只调文字、润色 |
| 大改（Re-craft） | ✅ | 先报告，再经确认传播 | `fiction-write`（内建） | 改剧情，检查后续是否需要同步 |
| 重写（Rewrite） | ✅ 全部 | 先报告，再经确认刷新 | `fiction-write`（内建） | 推翻重来，重新核对全链路 |

## 项目文件夹结构

```
项目/
├─ .novel/                # 系统文件（不用管）
│   ├─ state.json         # 记录写到哪了、当前模式
│   ├─ project_memory.json # 存着你觉得好的写法
│   └─ tmp/               # 临时文件
├─ .story-system/          # 执行 fiction-start 后的底本与提交记录
├─ 设定集/                 # 世界观、角色、能力体系
├─ 大纲/                   # 总纲、各卷节奏、章节大纲
├─ 正文/                   # 你写的每一章
├─ 追踪/                   # 伏笔、时间线、故事线索
└─ 审查报告/               # 系统审查后给你的建议
```

`fiction.py` 实际提供：`init`、`where`、`project-status`、`doctor`、`init-contract`、`export`、`chapter-commit`、`review-pipeline`、`projections` 和 `project-memory`。它不提供数据库 `index.db`、ZIP 归档、封面生成或独立 reviewer 服务；这些能力不能在完成报告中虚构。

## 许可证

MIT License — 自由使用、修改、分享。

## 鸣谢

本工具由 AI（Codex / Claude）辅助生成。

设计参考了以下开源项目：

### webnovel-writer
- 仓库: [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer)
- 贡献: 项目管理的工程化思路（统一状态管理、故事设定体系、审查流程等）

### oh-story-claudecode
- 仓库: [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode)
- 贡献: 情绪驱动写作方法论（先定情绪再定故事）、丰富的写作参考库、扫榜拆文流程、去 AI 味技巧

本项目融合了两者的设计精髓：以情绪驱动的方法论为核心，以工程化的数据模型为骨架。
