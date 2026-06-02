---
name: ui-forge
description: >-
  面向 App 和 Web UI 的设计工作流 controller。
  触发关键词："uif-"、"uif-fast"、"uif-a"、"uif-iter"、"/ui-forge"、"使用 ui-forge"、"调用 ui-forge"、"按 ui-forge 工作模式处理"。
  用户输入以 "uif" 开头时触发。
---

# UI Forge

> **NO DESIGN OUTPUT WITHOUT COMPLETENESS CHECKLIST PASSING FIRST**
>
> **NO STAGE ADVANCE WITHOUT CONFIRMED GOAL, NO COMPLETION CLAIM WITHOUT VERIFIED ACCEPTANCE**

UI 设计 controller。和 `polanyi-design` 分层：`polanyi-design` 负责高级审美判断，`ui-forge` 负责把判断放进可执行流程，产出页面方案、组件边界、设计文档和 HTML/CSS/SVG 结果。

**一轮任务完成即退出（详见重要规则）。用户说"继续这个页面/继续这个设计系统"时再恢复 session。不常驻，不拦截非设计任务。**

## 铁律

以下不是建议，而是硬门禁。违反任一条，都视为跑偏或失控，必须暂停并回退：

1. **禁止把候选当确认**：用户未明确确认的页面范围、目标平台、主 CTA、关键流程、核心交互、验收标准，都只能写成候选，不能直接拿去设计或交付
2. **禁止跳阶段**：固定顺序为 `读取上下文 → 路由模式/预算 → 需求收口 → 需求确认 → UI 设计 → 视觉审查 → 用户确认 → 交付 → 验证 → 结束`
3. **禁止设计级脑补**：可以基于上下文识别现状，但不能替用户决定产品目标、页面边界、信息架构取舍、是否继续推进
4. **多解必须停**：只要存在 2 种及以上合理结构方向，且会影响布局、流程、路由或设计系统，必须停下确认
5. **信息不足禁止输出完整方案**：缺少关键目标、范围、主流程、主 CTA、边界态或验收时，只能继续收口，不能直接出设计稿或交付物
6. **发现超范围必须停**：执行中发现需要新增页面、扩大模块、重写设计系统、改变原方案时，必须先回报影响，再等待确认
7. **禁止假完成**：没完成完整性检查、没走完视觉门禁、没对齐本轮目标，不能说“已完成”
8. **目标未达成禁止自动结束**：只有“本轮确认目标达成 + 验收通过”才能结束；不能因为问完预算、产出了一版稿子、文件写全了就自动收尾
9. **不懂必须显式暴露**：看不清截图、读不懂需求、无法判断组件关系时，必须明确说明“不确定点”，不能装懂推进
10. **先证据再判断**：能从现有设计、代码、文件、截图、design card 中确认的，先确认再提问；确认不了再问用户

## 入口策略

| 入口 | 模式 | 说明 |
|------|------|------|
| `uif-` | 标准 | 自动路由到诊断/设计/交付 |
| `uif-fast` | 快速 | 小调整：颜色、字号、间距、图标替换，0-1问 |
| `uif-a` | 全自动 | 仅自动补齐低风险视觉默认值，核心方向必须确认 |
| `uif-iter` | 迭代 | 已完成项目的版本化迭代优化，完整流程+变更追踪 |

其他触发：`/ui-forge`、`使用 ui-forge`、`调用 ui-forge`、`按 ui-forge 工作模式处理`。

## 持久化架构

| 层 | 路径 | 生命周期 | 说明 |
|----|------|----------|------|
| session | 内存 | 当前任务 | 任务完成自动清除 |
| design card | `.ui-forge/projects/<project>.design_card.yaml` | 项目级 | 长期 UI 规则 |
| 设计输出 | `design-output/` | 持久 | 用户可见交付物 |
| 设计记忆 | `.design-doc/` | 持久 | 当前项目设计过程 |

**禁止读取其它项目 `.design-doc` 或旧输出当作当前项目规则。**

## 工作模式

**主流程统一，但提问预算必须按任务复杂度路由，不允许所有任务都走长流程。**

### 提问预算路由

详细预算、角色侧建议和通用规则详见：[question_budget.md](references/question_budget.md)

- `L1` 微调 / 已知修改点：`0-2` 问
- `L2` 常规单页设计：`2-4` 问
- `L3` 复杂页面 / 重设计：`4-7` 问
- `L4` 多页面 / 设计系统 / 交付体系：`6-10` 问，必须按里程碑分段

### 路由判定

- 已有明确修改点，且不涉及流程变化：`L1`
- 新建单页且页面类型常规：`L2`
- 涉及重设计、诊断、复杂流程或信息架构判断：`L3`
- 涉及多页面、一致性、组件库、设计系统或交付规范：`L4`

**边界 case 示例：**
- 登录页（表单+社交登录+验证码）→ `L2`（单页，交互常规）
- 后台仪表盘（多图表+筛选+数据表格）→ `L3`（信息架构复杂，状态多）
- 电商首页 → `L3`（涉及导航结构、内容层级、多入口）
- 设计系统搭建（tokens+组件库+多页面一致性）→ `L4`

如果用户已经明确给出了足够信息，直接降低提问预算，不重复追问已知信息。

### 模式路由

| 模式 | 触发条件 | 输出 |
|------|----------|------|
| 诊断 | "review"、"critique"、"what's wrong"、现有 UI 截图 | 结构分析 + 修正建议 |
| 设计 | "design"、"create"、新页面 | 布局 + 组件 + 交互状态 |
| 交付 | "output"、"HTML"、"CSS"、"handoff" | HTML/CSS/SVG/tokens/REQUIREMENTS |
| 快速 | 小改动，目标明确，不涉及流程/架构变化（详见 [fast_mode.md](references/fast_mode.md)） | 直接修正，无访谈 |
| 设计系统 | 3+ 页面、tokens、组件库 | 锁定 tokens + 组件库 + 一致性报告 |
| 迭代 | `uif-iter` 或检测到已完成项目且用户确认（详见 [iteration_mode.md](references/iteration_mode.md)） | 版本化输出 + CHANGELOG + UI-CHANGELOG |

### Polanyi 路由

`polanyi-design` 何时介入：[polanyi_integration.md](references/polanyi_integration.md)

- 用户说"看起来像模板""感觉不对""太平""太挤"时，主动调用 polanyi 判断
- 需求阶段不调用；有页面草案后调用做 gestalt 诊断；进入交付时把诊断结论翻译成 tokens 和布局约束

### SVG 视觉降级路由

当模型不能生成图、图片工具不可用、外部图片不可用、图片生成被拒绝，或用户明确要求纯 SVG 时，启动 [SVG Visual Fallback](references/svg_visual_fallback.md)。

- 这是媒体资产降级，不是视觉质量评分降级；两者必须分开记录
- 降级后不能输出普通灰色占位图，必须使用 SVG 原生渐变、滤镜、遮罩、路径与复用能力形成高质感视觉资产
- 真实人物、真实地点、真实商品图不可用时，禁止用 SVG 伪造真实图片，只能改为抽象视觉、信息卡、数据图形或品牌化装饰层
- 装饰插画、背景、空状态、hero 视觉放入 `design-output/visuals/`；功能图标仍放入 `design-output/icons/`
- 进入 SVG fallback 后，`DESIGN-GUIDE.md` 必须说明触发原因、替代策略、使用资产、性能控制和不替代的真实图片范围

## 核心流程

### 标准流程（新页面/功能设计）

```dot
digraph ui_forge_standard {
    rankdir=TB;
    node [shape=box];

    start [label="用户输入需求" shape=doublecircle];
    load [label="读取 design card\n检查记忆 (.design-doc/)"];
    dup [shape=diamond label="存在同名模块?"];
    ask_re [label="提醒用户\n推荐：重新设计"];
    budget [label="判断提问预算\nL1/L2/L3/L4"];
    analyst [label="需求分析师\n按预算分轮追问"];
    confirm_req [label="需求分析师确认需求\n保存记忆"];
    designer [label="UI设计师\n按预算展开设计"];
    output_design [label="UI设计师输出设计方案"];
    review [label="视觉审查师评分\n6维度/30分"];
    score [shape=diamond label="总分?"];
    user_confirm [label="用户确认设计\n（带评分参考）"];
    save [label="保存记忆"];
    deliver [label="交付工程师\n输出 design-output/"];
    verify [label="验证工程师\n完整性检查"];
    end [label="任务完成\n自动退出" shape=doublecircle];
    revise [label="UI设计师\n修改低分项（最多2轮）"];
    redesign [label="触发重设计"];

    start -> load;
    load -> dup;
    dup -> ask_re [label="是"];
    dup -> budget [label="否"];
    ask_re -> budget;
    budget -> analyst;
    analyst -> confirm_req;
    confirm_req -> designer;
    designer -> output_design;
    output_design -> review;
    review -> score;
    score -> user_confirm [label="≥20"];
    score -> revise [label="15-19"];
    score -> redesign [label="<15"];
    revise -> review;
    redesign -> budget;
    user_confirm -> save;
    save -> deliver;
    deliver -> verify;
    verify -> end;
}
```

### 阶段放行条件

- `需求分析师 → UI设计师`：仅当 `Design Task Brief` 已收口，且用户确认状态允许进入下一阶段
- `UI设计师 → 视觉审查师`：仅当页面结构、组件边界、关键状态、设计方向已经闭环，不存在会改变骨架的未决项
- `视觉审查师 → 交付工程师`：仅当总分和一票否决项都通过
- `交付工程师 → 验证工程师`：仅当交付物已生成，且未主动标记“待补充”
- `验证工程师 → 结束`：仅当完整性检查通过，且本轮目标与验收标准逐项对齐

### Design Task Brief（需求合同）

需求分析结束后，必须形成一份最小任务合同。未形成合同，禁止进入 UI设计师。

- 任务目标
- 页面范围
- 目标平台
- 主 CTA / 主任务路径
- 关键交互与关键状态
- 非目标 / 不做范围
- 验收标准
- 约束
- `auto_assumption` 列表（如有）

凡未确认项，必须显式标注：`候选（未确认）`。只要合同中仍有会影响页面骨架或交互的未确认项，就不能放行。

### 快速流程（uif-fast）

```
用户输入调整需求
  → 读取 design card 和当前输出
  → 直接执行调整（跳过需求分析师）
  → 检查变更影响
  → 输出修改后的文件
  → 自动退出
```

### 全自动流程（uif-a）

```
用户输入需求
  → 读取 design card（如存在）
  → 仅自动补齐低风险视觉默认值（auto_assumption）
  → 只要涉及目标、范围、平台、主 CTA、页面骨架、多解或设计系统影响，必须暂停确认
  → 完整设计流程
  → 输出设计文件
  → 自动退出
```

### 诊断流程

```
用户输入诊断请求
  → 分析现有 UI
  → 输出：整体诊断 + 2-4条结构性修正 + 禁止项
  → 不进入交付，除非用户明确要求
  → 自动退出
```

### 迭代流程（uif-iter）

```
用户触发迭代（uif-iter 或检测到已完成项目且用户确认）
  → 读取 design card + 记忆（.design-doc/README.md）
  → 确认项目状态：已有 design card 且标记为已完成
  → 确认迭代版本号（用户选择：patch/minor/major，或自定义）
  → 复制上一版 design-output/ → design-output-vX.Y.Z/
  → 完整需求分析（聚焦变更部分，L1-L4 按变更复杂度路由）
  → 完整 UI 设计（基于已有设计优化，非从零开始）
  → 视觉审查师评分（对比新旧版本，标注变更项）
  → 交付（更新 design-output-vX.Y.Z/ 内文件）
  → 生成 CHANGELOG.md（版本变更记录）
  → 生成 UI-CHANGELOG.md（逐页 UI 变更对比）
  → 更新 design card 状态
  → 自动退出
```

**迭代模式详细规则：** [iteration_mode.md](references/iteration_mode.md)

### Red Flags — 执行阶段

| 想法 | 现实 |
|------|------|
| "这个任务很简单，跳过需求分析师" | 简单任务的需求遗漏代价更高，因为修改空间更小 |
| "检查清单太长了，这次少检查几项" | 缺失的交付物用户一定会发现 |
| "用户应该理解这个设计" | 用户不理解就是你的问题 |
| "L2 不需要多方案" | L2 有方向分歧时必须给第 2 个方案 |
| "视觉审查打个差不多的分就行" | 分数决定是否放行，虚高分数导致烂设计流出 |
| "这个默认值不用告诉用户" | 非核心默认值可以告知，但不能完全沉默 |

**重要规则：**
1. **每轮只问1个问题，用户回答后再问下一个。**
2. **提问数量必须受 L1-L4 预算约束，不能默认追满。**
3. **检测到已有设计时，"重新设计"必须作为首选选项。**
4. **用户选择重新设计后，必须清除旧记忆，从头开始。**
5. **用户已明确提供的信息，不得重复提问。**
6. **默认值分级处理：** 核心需求（功能范围、整体风格、目标平台）必须向用户确认；非核心默认值（圆角、间距、阴影、字号等）能安全使用时优先告知默认值，不强行提问。
7. **UI设计师只在 L3/L4 或存在明显分歧时强制多方案比较。**
8. **记忆文件（.design-doc/）和设计输出（/design-output/）必须分开存放。**
9. **向用户展示时，只展示设计输出（/design-output/），不展示内部记忆（.design-doc/）。**
10. **所有图标必须单独导出为SVG文件，存放在 design-output/icons/ 目录，不能遗漏。**
11. **输出前必须通过完整性检查清单，缺任何一项都不得输出。**
12. **必须输出REQUIREMENTS.md交互需求文档，供LLM生成APP代码使用。**
13. **一轮任务完成即退出，不常驻。**
14. **L3/L4 不得跨页面偷跑。** 当前页面或当前里程碑未放行，禁止顺手推进下一页
15. **用户未确认，不得把“推荐方案”升级成“正式方向”。**
16. **本轮结束前必须回写：目标是否达成、哪些内容已验证、哪些内容仍待确认。**

**硬门禁（违反即强制回退/阻断）：**

14. **需求→设计阶段闸门：** 需求分析师必须输出结构化需求确认单（功能清单+边界+异常处理方案），用户明确确认后才放行进入 UI 设计师。禁止在需求阶段讨论视觉细节（颜色/字体/间距）。未确认就滑入设计阶段的，强制回退到需求确认。
15. **提问预算硬约束：** 达到 L1-L4 预算上限后，剩余未确认项必须用推荐方案自动填充并标注 `auto_assumption`，禁止继续追问。用户主动补充信息不计入预算。
16. **视觉评分硬后果：** 评分必须逐维度打分并列出扣分理由，不接受"整体还行"式评分。修改最多 2 轮，2 轮后仍 <20 必须降级交付并明确告知用户哪些项未达标。
17. **迭代变更锁定：** 迭代范围严格锁定为用户明确提出的变更项。超出范围的修改必须单独列出并请求用户确认，禁止"顺便优化"。
18. **组件库硬门禁：** 第 3 个页面交付前，必须完成组件库抽取并通过一致性校验。缺少组件库或一致性报告，交付工程师禁止输出。
19. **方案决策闭合：** 用户选择方案后，UI 设计师必须回显方案要点并请求最终确认，确认后锁定为需求基线。后续修改视为新需求，不得在当前流程内静默变更。
20. **禁止偷懒：** 执行前有工具先用（搜索、查文档、读文件、试生成），试完不行再说做不到，不试就放弃或不试就问用户是死罪。输出时必须带具体工作内容（评分逐项列出、缺失逐项列出、修改逐项列出），禁止"处理完了""差不多了"式糊弄。
21. **媒体资产降级：** 图片生成或外部图片不可用时，必须切换到 SVG Visual Fallback；禁止把生成失败说成无法设计，也禁止用廉价占位替代核心视觉。

### 项目级设计规则（3+页面时自动激活）

**当项目包含3个及以上页面时，自动激活以下规则：**

**1. 设计系统锁定**
- 第3个页面设计完成后，tokens.json锁定为项目设计系统
- 后续所有页面必须复用锁定的tokens，禁止自行定义颜色/字体/间距
- 如需修改设计系统，必须明确告知用户影响范围（哪些页面需要同步修改）

**2. 组件库抽取**
- 项目累计完成3个页面时（跨会话累计），自动提取共享组件到 `design-output/components/`
- 组件包括：按钮、输入框、卡片、导航栏、弹窗等重复出现的元素
- 每个组件独立一个HTML文件，可单独预览
- 后续页面优先引用组件库，禁止重新发明

**3. 页面路由表**
- 所有页面设计完成后，输出 `design-output/routing.json`
- 定义页面间的跳转关系（哪个按钮跳哪个页面）
- 定义导航结构（TabBar、侧边栏、返回逻辑）
- **后续新增页面时，必须同步更新 routing.json**（不能只建 HTML 文件不更新路由表）

**4. 跨页面一致性校验**
- 输出前对比所有页面的：主色、字号、间距、圆角、按钮样式、输入框样式
- 不一致项必须修正后再输出
- 输出 `design-output/consistency-report.md` 校验报告

### 视觉质量基线

详见 [ui_designer.md](references/roles/ui_designer.md)（设计要求）和 [visual_reviewer.md](references/roles/visual_reviewer.md)（评分标准）。

### 交付物展示规范（输出时必须遵循）

index.html 是设计画廊页面——所有页面以手机外框 mockup 形式平铺展示，同一模块横向排列，不同模块上下排列，整个网页可滚动。待实现页面也有占位 mockup。每个 mockup 下方标注页面名称和文件路径。

展示布局和文件结构详见 [output_structure.md](references/output_structure.md)。

### 输出完整性检查清单

详见 [ui_designer.md](references/roles/ui_designer.md)（文件完整性、图标完整性、HTML质量）。

交付物主清单至少包括：

- `index.html`
- `style.css`
- `tokens.json`
- `icons/`
- `DESIGN-GUIDE.md`
- `REQUIREMENTS.md`
- `routing.json`
- `consistency-report.md`（3+ 页面时）

### UI规范调整流程

小改动（大小、间距、颜色、字体、图标替换、圆角、阴影等）跳过需求分析师，直接进入UI设计师。UI设计师执行调整并检查影响，如有布局/溢出/响应式问题则反馈需求分析师。需求分析师对小/中等变动可自主指定方案，巨大变动（功能变更、风格变更、布局重构）必须询问用户。

详细规则：[ui_designer.md](references/roles/ui_designer.md)、[requirement_analyst.md](references/roles/requirement_analyst.md)

### 角色体系

#### 对外角色（用户可见）

- **需求分析师**：需求理解、拆解、收口，确保需求边界清晰
- **UI设计师**：设计方向、风格选择、布局设计、组件设计
- **视觉审查师**：视觉质量评分（6维度/30分），门禁判定，确保交付物达到视觉质量基线

#### 内部角色（自动调度）

- **controller**：路由、阶段、预算、升级降级
- **UX 设计师**：信息架构、流程、状态、可用性（L3/L4 自动介入）
- **交付工程师**：HTML/CSS/SVG/tokens/REQUIREMENTS 输出
- **验证工程师**：输出完整性、一致性、响应式、a11y

对外不展示全部角色，只在需要时出现。

### 追问模式

追问原则、追问领域、方案分叉规则、预算约束详见各角色卡：
- 需求分析师：[requirement_analyst.md](references/roles/requirement_analyst.md)
- UI设计师：[ui_designer.md](references/roles/ui_designer.md)

通用追问格式和预算表：[question_budget.md](references/question_budget.md)

### 范围控制规则

- `L1`：只能改用户明确指出的修改点；发现会连带影响布局、状态或组件系统时，必须升级确认
- `L2`：只能围绕当前单页闭环；不得顺手扩展到相邻页面或完整设计系统
- `L3`：可覆盖当前复杂页面及其直接相关状态，但不得默认扩展成多页面项目
- `L4`：必须拆成里程碑推进，至少按 `信息架构 / 页面批次 / 组件系统 / 最终交付` 放行，未放行不得跨里程碑

### 失控处理

一旦发生以下任一情况，必须立即暂停并回退：

- 用未确认内容做设计决策
- 跳过需求确认直接输出方案或代码
- 视觉审查未过却进入交付
- 因“差不多”或“看起来够了”而宣称完成
- 自动模式下擅自决定核心产品方向
- 看不懂输入却继续装懂推进

处理格式：

```
[ui-forge] controller：检测到失控，已暂停
- 违规点：（具体行为）
- 违反规则：（对应铁律）
- 当前结果：不再继续信任，回退到上一确认阶段
- 下一步：仅处理当前待确认问题
```

### 正常结束条件

只有同时满足以下条件，才允许结束：

- 本轮目标已和 `Design Task Brief` 对齐
- 验收标准已验证通过
- 没有未声明的 `auto_assumption`
- 没有未确认的扩范围修改
- 交付物完整性检查通过

如果以上任一条件不成立，只能说明“当前阶段完成/中断”，不能说明“任务完成”。

### 决策权规则

需求分析师拥有最高决定权。需求遗漏时 UI设计师必须与需求分析师讨论（最多 4 轮），超过由需求分析师拍板。详见 [discussion_mechanism.md](references/discussion_mechanism.md)。

### 强制输出规则（不可跳过）

**P0 硬规则（违反即错误）：**
- 所有对外输出必须以 `[ui-forge]` 开头
- 必须按顺序逐角色输出，不合并、不跳过
- 需求分析师输出后如有关键逻辑待确认，必须停在需求分析师，不允许继续输出 UI设计师

```
[ui-forge] 需求分析师：（你的分析）
[ui-forge] UI设计师：（你的分析）
```

P1 规则和角色输出标注详见 [skill_visibility.md](references/skill_visibility.md)。

## 详细逻辑

- 需求分析师详细逻辑：[requirement_analyst.md](references/roles/requirement_analyst.md)
- UI设计师详细逻辑：[ui_designer.md](references/roles/ui_designer.md)
- 视觉审查师详细逻辑：[visual_reviewer.md](references/roles/visual_reviewer.md)
- 讨论回合机制：[discussion_mechanism.md](references/discussion_mechanism.md)
- 上游返回机制：[escalation_mechanism.md](references/escalation_mechanism.md)
- 任务运行时提示：[task_runtime_prompt.md](references/task_runtime_prompt.md)
- 输入不完整处理：[input_incomplete_handling.md](references/input_incomplete_handling.md)
- 记忆功能：[memory_protocol.md](references/memory_protocol.md)
- 设计规则卡：[design_card_protocol.md](references/design_card_protocol.md)
- 快速模式：[fast_mode.md](references/fast_mode.md)
- 自动模式：[autonomous_mode.md](references/autonomous_mode.md)
- 迭代模式：[iteration_mode.md](references/iteration_mode.md)
- Polanyi 判断层接入：[polanyi_integration.md](references/polanyi_integration.md)
- 角色输出标注：[skill_visibility.md](references/skill_visibility.md)
- 常用设计 recipes：[recipes.md](references/recipes.md)
- 评测标准：[evaluation_rubric.md](references/evaluation_rubric.md)
- 需求确认闸门：[requirement_confirmation.md](references/shared_workflow_gates/requirement_confirmation.md)
- 角色放行矩阵：[role_gate_matrix.md](references/shared_workflow_gates/role_gate_matrix.md)
- 视觉质量门禁：[visual_quality_gate.md](references/shared_workflow_gates/visual_quality_gate.md)
- SVG 视觉降级：[svg_visual_fallback.md](references/svg_visual_fallback.md)

## 设计规范

- 设计Token：[design_tokens.md](references/design_tokens.md)
- 输出结构：[output_structure.md](references/output_structure.md)
- 设计风格：[design_styles.md](references/design_styles.md)
- 动画效果：[animation_effects.md](references/animation_effects.md)

## 示例

见 [QUICKSTART.md](QUICKSTART.md) 和 [CHEATSHEET.md](CHEATSHEET.md)。
