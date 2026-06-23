# A3 v0.2 回填封口版：N=8 默认模板下的区域分类与 D_eff 判定规程

工程缩编 / 冻结接口 / 显式回填位 / 三态纪律

| 项目 | 内容 |

| --- | --- |

| 版本 | A3 v0.2 |

| 状态 | 回填封口版 / 工程审稿稿 |

| 冻结范围 | 默认 N=8 模板、Xi_k(α,β) 定义、D_eff 默认算法、A2 工程阈值表、区域分类决策树、通过/未决/回退纪律 |

| v0.2 原则 | 只回填与封口，不重推 A2；未拿到具体数值处使用显式回填位；不得用猜测替代冻结值 |

| 标准状态优先级 | 回退 > 未决 > 通过 |



## A3.0 v0.2 更新目标

A3 v0.2 的目标是把 A3 v0.1 的缩编骨架推进为“回填封口版”：凡 A2 已冻结的信息，均在 A3 中以可审稿、可追踪、可替换的接口号出现；凡当前上下文没有给出具体数值或标签的位置，均以显式回填位标注，避免在 A3 中编造 A2 内容。

- 将 A2 冻结项拆成可引用接口：A2-N8、A2-XI、A2-DEFF、A2-TH、A2-REGION、A2-STATE。

- 把 A3 的判定流程改写为硬门控流程：任何强制回退条件优先于未决，任何未决项优先于通过。

- 加入 A2 回填矩阵，使阈值数值、区域标签、分支条件、异常条件都有固定落点。

- 加入冻结一致性审计与 A3 验收清单，便于封版前逐项勾核。

- 保留 A3 v0.1 的四元组输出，不扩大正式接口；审计轨迹并入解释项 E。



## A3.1 冻结接口映射

A3 v0.2 使用下表作为冻结接口映射。A3 不修改这些接口，只接收、压缩和执行。

| 接口号 | 冻结项 | A3 调用方式 | 落点 |

| --- | --- | --- | --- |

| A2-N8 | 默认 N=8 模板 | N = 8；K_8 沿用 A2 冻结索引约定 | A3.2, A3.5 |

| A2-XI | Xi_k(α,β) 冻结定义 | 公式、归一化、有效域、异常条件均由 A2 给定 | A3.3, A3.5 |

| A2-DEFF | D_eff 默认算法 | 只允许默认路径；异常路径和回退路径沿用 A2 | A3.4, A3.5 |

| A2-TH | A2 工程阈值表 | 只产生通过 / 未决 / 回退三态 | A3.6 |

| A2-REGION | 区域分类决策树 | 区域标签、分支条件、边界规则沿用 A2 | A3.7 |

| A2-STATE | 通过 / 未决 / 回退纪律 | 回退不得输出正式结论；未决不得伪装通过 | A3.8 |



## A3.2 默认 N=8 模板

默认工程模式固定：N = 8。模板索引集合记为 K_8。

```text
A2-N8.FIXED:
    N := 8
    K := K_8
    index_convention := 【A2-N8-INDEX-CONVENTION】
    allowed_exception_mode := 【A2-N8-EXCEPTION-MODE】

A3 rule:
    未显式授权例外时，所有 Xi_k、D_eff 与区域判定均以 N=8 为唯一默认模板。
```

若输入显式调用非 N=8 模板，但未给出 A2 授权的切换条件，则不得进入默认流程。该情形优先判为“未决”；若与冻结模板冲突且不可修复，则判为“回退”。

## A3.3 Xi_k(α,β) 回填接口

A3 不重新推导 Xi_k(α,β)。v0.2 将其拆为可回填接口，便于把 A2 已冻结公式直接嵌入文稿。

```text
A2-XI.FROZEN:
    for k in K_8:
        Xi_k(α,β) := 【A2-XI-FORMULA-k】
        Dom(Xi_k) := 【A2-XI-DOMAIN-k】
        Normalization(Xi_k) := 【A2-XI-NORMALIZATION-k】
        Exception(Xi_k) := 【A2-XI-EXCEPTION-k】

A3 vector:
    Xi_8(α,β) := (Xi_k(α,β))_{k∈K_8}

A3 validity rule:
    八槽均须可计算、有限、符合 A2 有效域与归一化约束。
    不得跳过任一槽位继续分类。
```

| Xi 回填项 | 回填位 | 封口要求 |

| --- | --- | --- |

| Xi 公式 | 【A2-XI-FORMULA-k】 | 逐槽回填；不得用 v0.2 临时公式替代 |

| 有效域 | 【A2-XI-DOMAIN-k】 | α、β 与联合域条件均需写明 |

| 归一化 | 【A2-XI-NORMALIZATION-k】 | 符号、尺度、截断、归一化常数沿用 A2 |

| 异常条件 | 【A2-XI-EXCEPTION-k】 | 奇异、非有限、冲突、不可修复条件逐条列出 |

| 边界带 | 【A2-XI-PENDING-BAND-k】 | 若 A2 有未决带，必须单独回填 |



## A3.4 D_eff 默认算法回填接口

A3 调用 D_eff 默认算法，不替换、不拟合、不后处理。v0.2 将默认算法整理成“前置条件—计算步骤—稳定性检查—输出约束”四段。

```text
A2-DEFF.DEFAULT:
    input  := Xi_8(α,β)
    preconditions := 【A2-DEFF-PRECONDITIONS】
    steps := [
        【A2-DEFF-STEP-1】,
        【A2-DEFF-STEP-2】,
        ...,
        【A2-DEFF-STEP-m】
    ]
    stability_checks := 【A2-DEFF-STABILITY-CHECKS】
    fallback_triggers := 【A2-DEFF-FALLBACK-TRIGGERS】
    output := D_eff

A3 rule:
    若默认算法前置条件失败，A3 不得用替代算法补算 D_eff。
    若 D_eff 非有限、奇异、失稳或触发强制回退，正式 D_eff 置为 ∅。
```

| D_eff 项 | 回填位 | A3 处理 |

| --- | --- | --- |

| 前置条件 | 【A2-DEFF-PRECONDITIONS】 | 缺失但可复核 → 未决；冲突或不可满足 → 回退 |

| 默认步骤 | 【A2-DEFF-STEP-i】 | 逐步回填，保留 A2 顺序，不新增经验步骤 |

| 稳定性检查 | 【A2-DEFF-STABILITY-CHECKS】 | 与 A2 阈值表一致，不得弱化 |

| 输出约束 | 【A2-DEFF-OUTPUT-CONSTRAINTS】 | 有限性、范围、符号、单位、解释条件 |

| 回退触发 | 【A2-DEFF-FALLBACK-TRIGGERS】 | 任一强制回退触发即停止区域分类 |



## A3.5 标准输出与状态优先级

A3 v0.2 保留 v0.1 的四元组输出：

```text
O_A3 = (D_eff, R, S, E)

D_eff : 默认算法输出；若回退则为 ∅
R     : 区域标签；若未决可为候选集合；若回退则为 ∅
S     : 状态，S ∈ {通过, 未决, 回退}
E     : 解释项，必须包含触发门、阈值来源、边界原因、回退原因或审计轨迹
```

状态合成规则如下：

```text
if any(FALLBACK flag):
    S := 回退
elif any(PENDING flag):
    S := 未决
else:
    S := 通过
```

因此，A3 v0.2 明确采用“回退 > 未决 > 通过”的优先级。通过不是默认结果，而是所有门控检查均没有未决与回退之后的剩余结果。

## A3.6 A2 工程阈值表：v0.2 回填版

下表是 A3 v0.2 的工程门控表。每个门控均保留 A2 具体阈值的回填位。封版前必须将回填位替换为 A2 冻结值；替换前不得声称 A3 已完成数值封口。

| 门控 | 检查项 | 输入量 | 通过条件 | 未决条件 | 回退条件 |

| --- | --- | --- | --- | --- | --- |

| G0 | 模板一致性 | N, K_8 | 【A2-TH-G0-PASS】 | 【A2-TH-G0-PENDING】 | 【A2-TH-G0-FALLBACK】 |

| G1 | 参数有效性 | α, β | 【A2-TH-G1-PASS】 | 【A2-TH-G1-PENDING】 | 【A2-TH-G1-FALLBACK】 |

| G2 | Xi 完整性 | Xi_8 | 【A2-TH-G2-PASS】 | 【A2-TH-G2-PENDING】 | 【A2-TH-G2-FALLBACK】 |

| G3 | Xi 有限性 | Xi_k | 【A2-TH-G3-PASS】 | 【A2-TH-G3-PENDING】 | 【A2-TH-G3-FALLBACK】 |

| G4 | Xi 稳定性 | Xi_k / Xi_8 | 【A2-TH-G4-PASS】 | 【A2-TH-G4-PENDING】 | 【A2-TH-G4-FALLBACK】 |

| G5 | D_eff 前置条件 | Xi_8 → D_eff | 【A2-TH-G5-PASS】 | 【A2-TH-G5-PENDING】 | 【A2-TH-G5-FALLBACK】 |

| G6 | D_eff 有限性与范围 | D_eff | 【A2-TH-G6-PASS】 | 【A2-TH-G6-PENDING】 | 【A2-TH-G6-FALLBACK】 |

| G7 | D_eff 稳定性 | D_eff | 【A2-TH-G7-PASS】 | 【A2-TH-G7-PENDING】 | 【A2-TH-G7-FALLBACK】 |

| G8 | 区域决策树入口 | Xi_8, D_eff | 【A2-TH-G8-PASS】 | 【A2-TH-G8-PENDING】 | 【A2-TH-G8-FALLBACK】 |

| G9 | 区域唯一性 | R | 【A2-TH-G9-PASS】 | 【A2-TH-G9-PENDING】 | 【A2-TH-G9-FALLBACK】 |

| G10 | 纪律一致性 | S, E | 【A2-TH-G10-PASS】 | 【A2-TH-G10-PENDING】 | 【A2-TH-G10-FALLBACK】 |



门控合成不得采用平均、投票或人工覆盖。任一回退条件触发即整体回退；没有回退但存在未决条件时整体未决；所有门控通过时才允许整体通过。

## A3.7 区域分类决策树：v0.2 回填版

A3 v0.2 不新增区域名。区域集合、标签、边界带与出口规则均由 A2-REGION 给出。

```text
A2-REGION.FROZEN:
    region_set := 【A2-REGION-SET】
    labels := 【A2-REGION-LABELS】
    branch_conditions := 【A2-REGION-BRANCH-CONDITIONS】
    boundary_rules := 【A2-REGION-BOUNDARY-RULES】
    no_exit_rule := 【A2-REGION-NO-EXIT-RULE】

A3 region rule:
    1. 只有 G0...G8 均无回退且无未决时，才进入区域唯一性判断。
    2. 若决策树输出唯一区域，允许 R = R_i。
    3. 若输出多个候选区域，S = 未决，R = {R_i, R_j, ...}。
    4. 若无合法区域出口，S = 回退，R = ∅。
    5. 不得将边界态、候选集合或无出口状态改写成通过。
```

| 区域项 | 回填位 | 封口要求 |

| --- | --- | --- |

| 区域集合 | 【A2-REGION-SET】 | 列出 A2 冻结区域全集 |

| 区域标签 | 【A2-REGION-LABELS】 | 逐一回填正式名称，不使用临时别名 |

| 主分支条件 | 【A2-REGION-BRANCH-CONDITIONS】 | 写明由 Xi_8、D_eff 或阈值标志触发的分支 |

| 边界规则 | 【A2-REGION-BOUNDARY-RULES】 | 边界不强行判通过；默认进入未决，除非 A2 另有回退规则 |

| 无出口规则 | 【A2-REGION-NO-EXIT-RULE】 | 无合法区域出口时必须回退 |



## A3.8 通过 / 未决 / 回退纪律

A3 v0.2 将三态纪律写成硬约束，且不允许人工覆盖。

### A3.8.1 通过

- N=8 模板确认，且 K_8 索引完整。

- α、β 均在 A2 有效域内。

- 八槽 Xi_k(α,β) 均可计算、有限、稳定，且无异常条件。

- D_eff 由 A2-DEFF 默认算法得到，前置条件满足，输出有效。

- A2-TH 门控表 G0...G10 全部为通过。

- A2-REGION 决策树输出唯一合法区域。

- 解释项 E 写明触发路径与阈值来源。



### A3.8.2 未决

- 信息不足但可补充、可复查、可核验。

- 任一门控落入 A2 未决带，且未触发强制回退。

- Xi_k 或 D_eff 位于边界带，但 A2 未规定直接回退。

- 区域决策树输出多个候选区域。

- 默认算法前置条件尚未完全确认，但存在明确补齐路径。



### A3.8.3 回退

- N=8 模板无法成立，且无 A2 授权例外。

- 输入与 Xi_k(α,β) 冻结定义冲突。

- 任一关键 Xi_k 不可定义、非有限、奇异或不可修复。

- D_eff 默认算法无法启动，或输出非有限、奇异、失稳。

- 任一 A2-TH 强制回退条件触发。

- 区域决策树无合法出口。

- 需要替代算法才能继续，但 A2 未授权替代算法。



## A3.9 默认执行伪代码

```text
A3_CLASSIFY_v0_2(α, β):

    # G0: template gate
    N ← 8
    K ← K_8
    if not A2_N8_VALID(N, K):
        return (∅, ∅, 回退, "G0: N=8 模板不成立")

    # G1: input domain gate
    domain_flag ← A2_DOMAIN_CHECK(α, β)
    if domain_flag == FALLBACK:
        return (∅, ∅, 回退, "G1: 参数与 A2 有效域冲突")
    if domain_flag == PENDING:
        return (?, ?, 未决, "G1: 参数有效域待确认")

    # G2-G4: Xi gates
    Xi ← []
    for k in K_8:
        xk ← A2_XI_FROZEN(k, α, β)
        flag ← A2_XI_GATE(k, xk)
        if flag == FALLBACK:
            return (∅, ∅, 回退, "G2-G4: Xi 槽位触发回退")
        if flag == PENDING:
            return (?, ?, 未决, "G2-G4: Xi 槽位待复查")
        Xi.append(xk)

    # G5-G7: D_eff gates
    deff_flag, D_eff ← A2_DEFF_DEFAULT(Xi)
    if deff_flag == FALLBACK:
        return (∅, ∅, 回退, "G5-G7: D_eff 默认算法失败")
    if deff_flag == PENDING:
        return (?, ?, 未决, "G5-G7: D_eff 前置条件或稳定性待确认")

    # G8-G10: threshold + region gates
    flags ← A2_THRESHOLD_GATE(Xi, D_eff)
    if flags contains FALLBACK:
        return (∅, ∅, 回退, "A2-TH: 强制回退")
    if flags contains PENDING:
        return (D_eff?, ?, 未决, "A2-TH: 落入未决带")

    region_flag, R ← A2_REGION_TREE(Xi, D_eff)
    if region_flag == UNIQUE:
        return (D_eff, R, 通过, "A3: 区域唯一且全部门控通过")
    if region_flag == MULTIPLE:
        return (D_eff?, R_candidates, 未决, "A3: 区域候选不唯一")

    return (∅, ∅, 回退, "A3: 无合法区域出口")
```

## A3.10 冻结一致性审计

A3 v0.2 增加冻结一致性审计表。封版前逐项检查；任一“不一致”都必须回到 A2，而不是在 A3 内部直接改写。

| 审计项 | 一致性要求 | 失败表现 | 处置 |

| --- | --- | --- | --- |

| N=8 模板 | A3 只默认 N=8 | 出现未授权 N 切换 | 未决或回退 |

| Xi 定义 | A3 只引用 A2-XI | 重定义公式、改归一化、漏槽 | 回到 A2 修订 |

| D_eff | 只调用默认算法 | 替代算法、经验拟合、人工补算 | 回退 |

| 阈值表 | A3-TH 与 A2-TH 一一对应 | 阈值缺失、弱化、平均化 | 补齐或回退 |

| 区域树 | 区域名和分支沿用 A2 | 新增区域、合并区域、改边界 | 回到 A2 修订 |

| 三态纪律 | 回退 > 未决 > 通过 | 把未决写成通过，把回退继续分类 | 判定无效 |



## A3.11 A2 回填矩阵

以下矩阵是 v0.2 的关键封口清单。当前上下文未包含具体 A2 数值和区域标签，因此本稿不编造；回填时直接替换对应占位符。

| 编号 | 回填对象 | 占位符 | 封口说明 |

| --- | --- | --- | --- |

| F1 | K_8 索引约定 | 【A2-N8-INDEX-CONVENTION】 | 例如 k 的起止、排序、槽位含义；必须与 A2 一致 |

| F2 | Xi_k 公式 | 【A2-XI-FORMULA-k】 | 逐槽公式；若同式不同参数，也需写明 |

| F3 | Xi 有效域 | 【A2-XI-DOMAIN-k】 | α、β、联合域、排除点 |

| F4 | Xi 归一化 | 【A2-XI-NORMALIZATION-k】 | 符号、尺度、单位、截断 |

| F5 | Xi 异常与边界 | 【A2-XI-EXCEPTION-k】 / 【A2-XI-PENDING-BAND-k】 | 异常为回退，边界为未决，除非 A2 另有规定 |

| F6 | D_eff 步骤 | 【A2-DEFF-STEP-i】 | 默认算法完整步骤 |

| F7 | D_eff 约束 | 【A2-DEFF-OUTPUT-CONSTRAINTS】 | 有限性、范围、稳定性 |

| F8 | 阈值数值 | 【A2-TH-Gi-PASS/PENDING/FALLBACK】 | G0-G10 三态条件全部回填 |

| F9 | 区域集合 | 【A2-REGION-SET】 / 【A2-REGION-LABELS】 | 正式区域名与代码 |

| F10 | 区域分支 | 【A2-REGION-BRANCH-CONDITIONS】 | 真实分支条件，不使用描述性空话 |

| F11 | 边界与无出口 | 【A2-REGION-BOUNDARY-RULES】 / 【A2-REGION-NO-EXIT-RULE】 | 边界、候选、多出口、无出口的状态归属 |

| F12 | 报告证据项 | 【A2-EVIDENCE-REQUIREMENTS】 | 最终报告必须记录的阈值、路径、原因 |



## A3.12 最小判定报告格式

A3 v0.2 的最小报告格式如下。正式报告不得省略门控状态。

```text
A3 判定报告

输入：
    α = ...
    β = ...
    N = 8
    K_8 = 【A2-N8-INDEX-CONVENTION】

Xi 向量：
    Xi_8(α,β) = ...
    Xi 有效域检查 = 通过 / 未决 / 回退
    Xi 完整性检查 = 通过 / 未决 / 回退
    Xi 稳定性检查 = 通过 / 未决 / 回退

D_eff：
    D_eff 默认算法版本 = 【A2-DEFF-VERSION】
    D_eff = ...
    D_eff 可计算性 = 通过 / 未决 / 回退
    D_eff 稳定性 = 通过 / 未决 / 回退

A2 工程阈值表：
    G0 模板一致性 = 通过 / 未决 / 回退
    G1 参数有效性 = 通过 / 未决 / 回退
    G2 Xi 完整性 = 通过 / 未决 / 回退
    G3 Xi 有限性 = 通过 / 未决 / 回退
    G4 Xi 稳定性 = 通过 / 未决 / 回退
    G5 D_eff 前置条件 = 通过 / 未决 / 回退
    G6 D_eff 有限性与范围 = 通过 / 未决 / 回退
    G7 D_eff 稳定性 = 通过 / 未决 / 回退
    G8 区域决策树入口 = 通过 / 未决 / 回退
    G9 区域唯一性 = 通过 / 未决 / 回退
    G10 纪律一致性 = 通过 / 未决 / 回退

区域分类：
    R = ...
    候选区域 = ...
    决策树路径 = ...

最终输出：
    O_A3 = (D_eff, R, S, E)
    S = 通过 / 未决 / 回退
    E = ...
```

## A3.13 A3 v0.2 验收清单

| 验收项 | 通过标准 | 状态 |

| --- | --- | --- |

| N=8 默认模板已固定 | A2-N8 索引约定已回填 | 待勾选 |

| Xi_k(α,β) 定义已接入 | 公式、有效域、归一化、异常条件完整 | 待勾选 |

| D_eff 默认算法已接入 | 前置条件、步骤、稳定性、回退触发完整 | 待勾选 |

| A2 工程阈值表已回填 | G0-G10 三态条件均填入冻结值 | 待勾选 |

| 区域分类决策树已回填 | 区域集合、标签、分支、边界、无出口规则完整 | 待勾选 |

| 通过 / 未决 / 回退纪律未被改写 | 回退 > 未决 > 通过，且无人工覆盖 | 待勾选 |

| A3 可独立执行一次判定 | 最小报告格式可填完，且路径可复查 | 待勾选 |

| A3 未新增 A2 之外的定义 | 无新阈值、无新区域、无替代算法 | 待勾选 |



## A3.14 缩编结论

A3 v0.2 的核心流程为：

```text
(α,β)
  → N=8 / K_8
  → Xi_8(α,β)
  → D_eff 默认算法
  → A2 工程阈值表 G0...G10
  → A2 区域分类决策树
  → O_A3 = (D_eff, R, S, E)
```

其纪律为：通过必须唯一；未决不得伪装成结论；回退不得继续分类；A3 不修改 A2 冻结项。

**v0.2 当前可作为回填封口稿使用。最终封版前，必须把所有【A2-...】回填位替换为 A2 冻结内容，并完成 A3.13 验收清单。**
