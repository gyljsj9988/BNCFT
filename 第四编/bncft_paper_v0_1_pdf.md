---
title: "BNCFT：双重无背景共形场论的最小结构、引力接口与低能广义相对论极限"
subtitle: "工作稿 v0.1｜从无背景共享场到有效度规、Ward 恒等式、单度规相、物质接口与诱导引力"
date: "2026-04-20"
lang: zh-CN
---

## 摘要

本文整理 BNCFT，即“双重无背景共形场论”的最小理论框架。BNCFT 的基本对象不是定义在预设时空背景上的场，而是两个无背景共形扇区

$$
\mathcal C_+,\qquad \mathcal C_-,
$$

以及连接二者的共享关系场

$$
\Phi^A.
$$

共享场不是普通时空场，而是前几何变量。它在某些红外相中产生关系坐标、有效四标架、有效度规、低能物质场以及引力动力学。本文的核心论证链为：

$$
\boxed{
(\mathcal C_+,\mathcal C_-,\Phi^A,\mathcal G_\mathrm{rel})
\Rightarrow
X^\mu[\Phi]
\Rightarrow
e_\mu{}^a
\Rightarrow
g_{\mu\nu}^\mathrm{eff}
\Rightarrow
\Gamma_\mathrm{IR}[g,\psi]
\Rightarrow
G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G T_{\mu\nu}.
}
$$

其中 $\mathcal G_\mathrm{rel}$ 是关系冗余群。它在 rank-4 几何相中投影为红外微分同胚不变性，并通过 Ward 恒等式给出

$$
\nabla_\mu T^\mu{}_{\nu}=0.
$$

进一步，BNCFT 的双扇区结构一般会产生两个有效标架。但在共享场锁定的单度规相中，反对角几何模式获得质量并在低能解耦，只剩一个健康的无质量自旋二模式。物质场则来自关系算符的低能极点、守恒流、界面零模或双扇区复合态。所有低能物种在 leading order 共享同一个传播锥，从而得到等效原理。

积分掉短波共享场、共形扇区和界面重模式后，有效引力作用量出现导数展开：

$$
\Gamma_g[g]
=
\int d^4X\sqrt{-g}
\left[
\frac{c_0}{\ell_I^4}
+
\frac{c_1}{\ell_I^2}R
+
c_2R^2
+
\cdots
\right].
$$

其中

$$
\frac{1}{16\pi G_\mathrm{eff}}
=
\frac{c_1}{\ell_I^2},
\qquad
M_\mathrm{Pl}^2
=
\frac{2c_1}{\ell_I^2}.
$$

因此，在 BNCFT 中 Newton 常数不是微观输入，而是共享场几何刚度、共形扇区应力响应和界面锁定通道的红外集体结果。本文最后给出 BNCFT 退化为广义相对论的相条件，并指出宇宙学常数、宇宙学相、黑洞熵和可观测偏离是后续必须处理的问题。

## 核心记号表

| 符号 | 地位 | 含义 |
|---|---:|---|
| $\mathcal C_+$, $\mathcal C_-$ | 基本 | 两个无背景共形扇区 |
| $\Phi^A$ | 基本 | 共享关系场，内部指标 $A$ 不是时空指标 |
| $\mathcal G_\mathrm{rel}$ | 基本冗余 | 标签、关系坐标、标架与 Weyl 表示冗余 |
| $\sigma\in\Sigma$ | 非物理标签 | 记账标签，不是物理时空点 |
| $X^\mu[\Phi]$ | 派生 | rank-4 几何相中的关系坐标 |
| $e_\mu{}^a$ | 派生 | 共享场凝聚态诱导的有效四标架 |
| $g_{\mu\nu}^\mathrm{eff}$ | 派生 | 低能有效度规 |
| $\ell_I$ | 相参数 | 界面相关长度或锁定尺度 |
| $c_0,c_1,\ldots$ | Wilson 系数 | 粗粒化后的有效引力作用量系数 |
| $T_{\mu\nu}$ | 派生 | 低能物质对有效度规的响应 |
| $G_\mathrm{eff},\Lambda_\mathrm{eff}$ | 派生 | 红外 Newton 常数与宇宙学常数 |

# 1. 引言

广义相对论把度规 $g_{\mu\nu}$ 提升为动力学变量，但仍然以可微流形、局域坐标和张量场作为基本语言。量子场论则通常从固定背景时空出发。若希望更彻底地理解时空本身的起源，就需要一种不把 $x^\mu$、$g_{\mu\nu}$、因果锥和体积元作为微观输入的框架。

BNCFT 的基本思想是：

$$
\boxed{
\text{时空不是舞台，而是关系场凝聚态的红外表现。}
}
$$

BNCFT 假设存在两个无背景共形扇区

$$
\mathcal C_+,\qquad \mathcal C_-,
$$

它们之间没有预设公共时空。二者通过共享关系场

$$
\Phi^A
$$

耦合。这个共享场在红外几何相中产生可比较关系，从而诱导关系坐标

$$
X^\mu[\Phi],
$$

有效四标架

$$
e_\mu{}^a,
$$

以及有效度规

$$
g_{\mu\nu}^\mathrm{eff}.
$$

本文的目标不是构造某个具体微观模型，而是给出 BNCFT 到低能广义相对论的最小接口条件。核心问题包括：BNCFT 的最小公设是什么？如何从无背景共享场得到有效度规？为什么红外理论具有能动张量协变守恒？为什么双扇区结构不会在低能留下双度规或 ghost？低能物质场从哪里来，为什么共同耦合同一个度规？Newton 常数如何由 BNCFT 的共形数据和界面刚度诱导出来？

# 2. BNCFT 的最小公设

## 2.1 无公共背景

BNCFT 的首要公设是：

$$
\boxed{
\text{微观层面没有公共背景时空。}
}
$$

因此不预设

$$
(M,g_{\mu\nu}),
\qquad
x^\mu,
\qquad
ds^2,
\qquad
\sqrt{-g},
\qquad
\nabla_\mu.
$$

如果这些对象出现，它们只能是某个红外几何相中的派生对象。

BNCFT 可以使用一个标签集 $\Sigma$ 来记账，写作

$$
\sigma\in\Sigma.
$$

但必须强调：

$$
\boxed{
\sigma \text{ 不是物理时空点。}
}
$$

标签重标号

$$
\sigma\rightarrow f(\sigma)
$$

不改变物理。

## 2.2 两个无背景共形扇区

BNCFT 的两个基本共形扇区记为

$$
\mathcal C_+,\qquad \mathcal C_-.
$$

它们不是“定义在同一个背景流形上的两个 CFT”，而是两组无背景共形数据：

$$
\mathcal C_\pm
=
\left(
\mathfrak A_\pm,
\{\mathcal O_i^{(\pm)}\},
\Delta_i^{(\pm)},
C_{ij}{}^{k(\pm)},
\langle\cdot,\cdot\rangle_\pm
\right).
$$

其中 $\mathfrak A_\pm$ 是算符代数，$\mathcal O_i^{(\pm)}$ 是基算符，$\Delta_i^{(\pm)}$ 是尺度维数，$C_{ij}{}^{k(\pm)}$ 是融合数据或无背景 OPE 数据。

因此：

$$
\boxed{
\mathcal C_\pm
\text{ 是共形数据，而不是背景时空上的场论。}
}
$$

## 2.3 共享关系场

BNCFT 的核心对象是共享关系场

$$
\Phi^A.
$$

这里 $A,B,\ldots$ 是内部指标，不是时空指标。共享场的作用不是在某个背景中传播，而是在两个无背景共形扇区之间建立可比较关系：

$$
\mathcal C_+
\quad
\overset{\Phi^A}{\longleftrightarrow}
\quad
\mathcal C_-.
$$

因此：

$$
\boxed{
\Phi^A \neq g_{\mu\nu}.
}
$$

度规只能是共享场长波凝聚态的派生响应量。

形式上，BNCFT 的路径积分可写为

$$
Z_\mathrm{BNCFT}[J]
=
\int
\frac{
\mathcal D\Phi\,
\mathcal D\chi_+\,
\mathcal D\chi_-
}{
\mathrm{Vol}(\mathcal G_\mathrm{rel})
}
\exp
\left[
iS_\mathrm{BNCFT}[\Phi,\chi_+,\chi_-]
+
iJ\cdot\mathcal O_\mathrm{rel}
\right].
$$

其中

$$
S_\mathrm{BNCFT}
=
S_+[\chi_+]
+
S_-[\chi_-]
+
S_\mathrm{share}[\Phi]
+
S_\mathrm{int}[\Phi,\chi_+,\chi_-].
$$

这里的 $S_\pm$ 不是普通固定背景 CFT 作用量，而是两个无背景共形扇区的动力学表示。

## 2.4 关系冗余群

由于标签没有物理意义，BNCFT 必须具有关系冗余群

$$
\mathcal G_\mathrm{rel}.
$$

它至少包含标签重标号冗余、关系坐标选择冗余、内部标架冗余，以及 Weyl 表示冗余或 Weyl 模。物理量必须满足

$$
\mathcal O_\mathrm{phys}[\Phi,\chi_+,\chi_-]
=
\mathcal O_\mathrm{phys}[g\cdot\Phi,g\cdot\chi_+,g\cdot\chi_-],
\qquad
g\in\mathcal G_\mathrm{rel}.
$$

因此普通形式的局域算符 $\mathcal O(\sigma)$ 不是物理量。真正的局域性必须是关系局域性。

## 2.5 关系穿衣算符

在几何相中，若可以构造关系坐标

$$
X^\mu=X^\mu[\Phi],
$$

则可以定义关系穿衣算符：

$$
\mathcal O_i^\mathrm{rel}(X)
=
\int_\Sigma d\mu(\sigma)\,
\delta^{(4)}
\left(
X-X[\Phi](\sigma)
\right)
\mathcal O_i(\sigma).
$$

这表示“在共享场定义的关系位置 $X$ 处测得的算符”。因此：

$$
\boxed{
\mathcal O_i(\sigma)
\longrightarrow
\mathcal O_i^\mathrm{rel}(X).
}
$$

红外局域场论中的局域算符不是基本对象，而是被共享场穿衣后的关系对象。

# 3. 从共享场到有效度规

## 3.1 rank-4 几何相

BNCFT 的最小公设不保证一定出现四维时空。四维性是相性质。若共享场凝聚为

$$
\Phi^A=\bar\Phi^A+\varphi^A,
$$

并且存在四个独立慢变量

$$
X^\mu=F^\mu[\bar\Phi],
\qquad
\mu=0,1,2,3,
$$

满足

$$
\mathrm{rank}
\left(
\frac{\partial X^\mu}{\partial \sigma^i}
\right)=4,
$$

则该相具有四维关系坐标结构。因此：

$$
\boxed{
\text{四维性不是微观公设，而是共享场凝聚态的 rank-4 相条件。}
}
$$

## 3.2 关系坐标冗余与微分同胚

关系坐标的选择不唯一。若

$$
X^\mu\rightarrow X'^\mu(X),
$$

物理不变。这在红外表现为微分同胚不变性：

$$
\boxed{
\text{关系坐标冗余}
\longrightarrow
\text{diffeomorphism invariance}.
}
$$

无穷小变换为

$$
X^\mu\rightarrow X^\mu-\xi^\mu(X).
$$

低能场变换为

$$
\delta_\xi\psi=\mathcal L_\xi\psi.
$$

有效度规变换为

$$
\delta_\xi g_{\mu\nu}
=
\nabla_\mu\xi_\nu+
\nabla_\nu\xi_\mu.
$$

## 3.3 有效四标架

共享场本身不是度规。度规通过共享场长波构型的投影出现。引入共享场靶空间到局域 Lorentz 标架的投影：

$$
E_A{}^a(\Phi),
\qquad
a=0,1,2,3.
$$

定义有效四标架：

$$
\boxed{
e_\mu{}^a(X)
=
\ell_I
E_A{}^a(\bar\Phi)
\partial_\mu\bar\Phi^A.
}
$$

其中 $\ell_I$ 是界面相关长度或锁定尺度。有效度规定义为

$$
\boxed{
g_{\mu\nu}^\mathrm{eff}
=
\eta_{ab}e_\mu{}^a e_\nu{}^b.
}
$$

即

$$
\boxed{
g_{\mu\nu}^\mathrm{eff}
=
\ell_I^2
\eta_{ab}
E_A{}^a(\bar\Phi)
E_B{}^b(\bar\Phi)
\partial_\mu\bar\Phi^A
\partial_\nu\bar\Phi^B.
}
$$

这就是 BNCFT 的基本引力接口公式。

## 3.4 共形类与 Weyl 因子

由于基本扇区是共形的，BNCFT 通常首先给出度规共形类：

$$
[g_{\mu\nu}]
=
\{\Omega^2g_{\mu\nu}\}.
$$

完整度规需要确定 Weyl 因子：

$$
g_{\mu\nu}=e^{2\omega}\hat g_{\mu\nu}.
$$

其中 $\hat g_{\mu\nu}$ 决定因果结构，$\omega$ 决定尺度。若 $\omega$ 是规范冗余，则可以规范固定。若 $\omega$ 是物理 dilaton，则必须在低能解耦，否则红外理论不是纯 GR，而是标量-张量理论。

# 4. BNCFT 的 Ward 恒等式

## 4.1 微观关系 Ward 恒等式

把所有微观表示变量合并为

$$
q^I=(\Phi^A,\chi_+,\chi_-).
$$

关系冗余的无穷小变换写为

$$
\delta_\epsilon q^I
=
R^I{}_{\alpha}[q]\epsilon^\alpha.
$$

BNCFT 的基本不变性为

$$
\delta_\epsilon S_\mathrm{BNCFT}=0.
$$

量子层面，若测度无异常，则

$$
0=\delta_\epsilon Z[J].
$$

得到带源 Ward 恒等式：

$$
\left\langle
\delta_\epsilon
\left(
J\cdot\mathcal O_\mathrm{rel}
\right)
\right\rangle
=0.
$$

对 1PI 有效作用量：

$$
\boxed{
\mathcal W_\epsilon\Gamma
=
\left\langle
\frac{\delta\Gamma}{\delta q^I},
R^I{}_{\alpha}[q]\epsilon^\alpha
\right\rangle
=0.
}
$$

这是真正的前几何 Ward 恒等式。它不依赖 $x^\mu$、$g_{\mu\nu}$ 或 $\nabla_\mu$。

## 4.2 红外 diffeomorphism Ward 恒等式

进入 rank-4 几何相后，关系冗余的一部分表现为微分同胚不变性：

$$
\delta_\xi\Gamma_\mathrm{IR}[g,\psi]=0.
$$

物质作用量的变分为

$$
\delta_\xi\Gamma_m
=
\int d^4X\sqrt{-g}
\left[
-\frac12T_{\mu\nu}\delta_\xi g^{\mu\nu}
+
\sum_sE_s\delta_\xi\psi_s
\right],
$$

其中

$$
T_{\mu\nu}
=
-\frac2{\sqrt{-g}}
\frac{\delta\Gamma_m}{\delta g^{\mu\nu}},
$$

$$
E_s
=
\frac1{\sqrt{-g}}
\frac{\delta\Gamma_m}{\delta\psi_s}.
$$

代入

$$
\delta_\xi g^{\mu\nu}
=
-\nabla^\mu\xi^\nu-\nabla^\nu\xi^\mu,
$$

得到

$$
0
=
\int d^4X\sqrt{-g}
\left[
T_{\mu\nu}\nabla^\mu\xi^\nu
+
\sum_sE_s\mathcal L_\xi\psi_s
\right].
$$

分部积分并利用 $\xi^\nu$ 任意，得到

$$
\boxed{
\nabla^\mu T_{\mu\nu}
=
\sum_sE_s\mathcal D_\nu\psi_s.
}
$$

当物质场满足有效运动方程 $E_s=0$，则

$$
\boxed{
\nabla^\mu T_{\mu\nu}=0.
}
$$

因此，能动张量协变守恒不是外加假设，而是 BNCFT 关系冗余在几何相中的 Ward 恒等式。

## 4.3 与 Bianchi 恒等式的一致性

引力有效作用量定义响应张量

$$
\mathcal E_{\mu\nu}
=
\frac2{\sqrt{-g}}
\frac{\delta\Gamma_g}{\delta g^{\mu\nu}}.
$$

若 $\Gamma_g$ 微分同胚不变，则

$$
\boxed{
\nabla^\mu\mathcal E_{\mu\nu}=0.
}
$$

Einstein-Hilbert 极限中：

$$
\mathcal E_{\mu\nu}
=
\frac1{8\pi G_\mathrm{eff}}
\left(
G_{\mu\nu}+\Lambda g_{\mu\nu}
\right).
$$

于是

$$
\nabla^\mu
\left(
G_{\mu\nu}+\Lambda g_{\mu\nu}
\right)=0.
$$

场方程 $\mathcal E_{\mu\nu}=T_{\mu\nu}$ 与 Ward 恒等式自动相容。因此：

$$
\boxed{
\text{BNCFT 的关系 Ward 恒等式是 Einstein 方程一致性的红外来源。}
}
$$

# 5. 单度规相与无 ghost 条件

## 5.1 双扇区诱导两个标架

由于 BNCFT 有两个共形扇区，几何相中原则上会出现两个有效四标架：

$$
e_{+\mu}{}^a,
\qquad
e_{-\mu}{}^a.
$$

对应两个度规：

$$
g_{+\mu\nu}
=
\eta_{ab}e_{+\mu}{}^ae_{+\nu}{}^b,
$$

$$
g_{-\mu\nu}
=
\eta_{ab}e_{-\mu}{}^ae_{-\nu}{}^b.
$$

定义对角与反对角组合：

$$
\boxed{
e_\mu{}^a
=
\frac12
(e_{+\mu}{}^a+e_{-\mu}{}^a),
}
$$

$$
\boxed{
b_\mu{}^a
=
\frac12
(e_{+\mu}{}^a-e_{-\mu}{}^a).
}
$$

于是

$$
e_{\pm\mu}{}^a=e_\mu{}^a\pm b_\mu{}^a.
$$

线性阶上

$$
g_{+\mu\nu}-g_{-\mu\nu}=4b_{(\mu\nu)}.
$$

所以 $b_{\mu\nu}$ 表示两个扇区的相对几何模式。

## 5.2 对角冗余与反对角物理模式

共享场锁定保留对角关系冗余：

$$
\xi_+=\xi_-=\xi.
$$

它成为红外微分同胚不变性。反对角组合

$$
\xi_+=-\xi_-=\zeta
$$

不是低能精确冗余，而是被共享场锁定。因此：

$$
\boxed{
g_{\mu\nu}\text{ 是对角几何模式，}
\qquad
b_{\mu\nu}\text{ 是反对角物理模式。}
}
$$

若 $b_{\mu\nu}$ 轻，则低能不是 GR，而是双度规或 massive gravity 型理论。GR 相要求

$$
\boxed{
E\ll m_b,
}
$$

其中 $m_b$ 是反对角模式质量。

## 5.3 Fierz-Pauli 条件

反对角模式的二次质量项一般为

$$
\Gamma_\mathrm{mass}
=
-\frac{M_b^2m_b^2}{8}
\int d^4X\sqrt{-g}
\left(
b_{\mu\nu}b^{\mu\nu}
-
\alpha b^2
\right).
$$

若 $\alpha\neq1$，则 massive spin-2 的 trace 模式成为 ghost。健康线性 massive spin-2 要求

$$
\boxed{
\alpha=1.
}
$$

即质量项必须是 Fierz-Pauli 型：

$$
\boxed{
b_{\mu\nu}b^{\mu\nu}-b^2.
}
$$

因此 BNCFT 的锁定势在二次层面必须满足

$$
\Gamma_\mathrm{lock}^{(2)}
\propto
b_{\mu\nu}b^{\mu\nu}-b^2.
$$

## 5.4 Weyl/dilaton 模

由于 BNCFT 基本扇区共形，红外 Weyl 模 $\omega$ 需要特别处理。若

$$
g_{\mu\nu}=e^{2\omega}\hat g_{\mu\nu},
$$

则 $\omega$ 有三种可能：它是 Weyl 冗余，可规范固定；它是重 dilaton，满足 $m_\omega^2\gg E^2$；或者它是轻标量。第三种情况下，低能理论一般是标量-张量理论，而不是纯 GR。

因此 GR 相要求：

$$
\boxed{
\omega \text{ 是规范冗余，或 } m_\omega^2\gg E^2.
}
$$

若 $\omega$ 物理传播，还必须满足 Einstein frame kinetic 正定：

$$
K_E(\omega)>0.
$$

## 5.5 高导数 ghost

诱导引力作用量一般含有

$$
R^2,
\qquad
R_{\mu\nu}R^{\mu\nu},
\qquad
C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}.
$$

其中 Weyl-squared 项通常引入 massive spin-2 ghost。若其质量为

$$
M_2^2
\sim
\frac{M_\mathrm{Pl}^2}{|c_C|},
$$

则健康低能要求

$$
E\ll M_2.
$$

因此单度规 GR 相的有效截断为

$$
\Lambda_\mathrm{GR}
=
\min
\left(
m_b,
m_\omega,
M_\mathrm{hd},
\ell_I^{-1},
\Lambda_\mathrm{ghost}
\right).
$$

在 $E\ll\Lambda_\mathrm{GR}$ 时，只有一个健康的无质量自旋二模式传播。

## 5.6 单度规相条件

BNCFT 的 GR 相要求

$$
\boxed{c_1>0,}
$$

$$
\boxed{m_b^2>0,\qquad E\ll m_b,}
$$

$$
\boxed{\Gamma_\mathrm{lock}^{(2)}\propto b_{\mu\nu}b^{\mu\nu}-b^2,}
$$

$$
\boxed{\omega \text{ 为冗余或重场},}
$$

$$
\boxed{E\ll M_\mathrm{hd},}
$$

以及

$$
\boxed{
g_{\mu\nu}^{(s)}
=
g_{\mu\nu}
+
\mathcal O(E^2/\Lambda_\mathrm{GR}^2)
}
$$

对所有低能物种成立。满足这些条件后

$$
g_{+\mu\nu}\simeq g_{-\mu\nu}\simeq g_{\mu\nu}.
$$

# 6. BNCFT 的物质接口

## 6.1 物质场是关系算符的低能极点

BNCFT 的微观对象不是 $\psi(x)$、$A_\mu(x)$、$\Psi(x)$ 这样的背景场，而是两个扇区中的关系算符

$$
\mathcal O_i^{(+)},
\qquad
\mathcal O_j^{(-)},
$$

以及界面算符

$$
\mathcal O_a^{(I)}[\Phi,\chi_+,\chi_-].
$$

进入几何相后，定义关系穿衣算符 $\mathcal O_i^\mathrm{rel}(X)$。若其两点函数有低能孤立极点

$$
\langle
\mathcal O_i^\mathrm{rel}(p)
\mathcal O_j^\mathrm{rel}(-p)
\rangle
\sim
\frac{Z_{ij}}{p^2+m_s^2}
+
\text{continuum},
$$

则可引入低能有效场

$$
\psi_s(X).
$$

因此：

$$
\boxed{
\text{低能物质场是关系算符谱中的长寿命低能极点。}
}
$$

## 6.2 标量、规范场与费米子

标量场来自标量关系算符极点：

$$
\mathcal O_s^\mathrm{rel}\longrightarrow\phi_s(X).
$$

其有效作用量为

$$
\Gamma_\phi
=
-\frac12
\int d^4X\sqrt{-g}
\left[
g^{\mu\nu}\nabla_\mu\phi_s\nabla_\nu\phi_s
+
m_s^2\phi_s^2
+
\xi_sR\phi_s^2
+
\cdots
\right].
$$

规范场可来自内部关系冗余的连接，或守恒流的无质量自旋一极点。若存在关系守恒流

$$
J_I^\mu(X),
\qquad
\nabla_\mu J_I^\mu=0,
$$

并且

$$
\langle J_I^\mu(p)J_J^\nu(-p)\rangle
\sim
\frac{Z_{IJ}}{p^2}
\left(
g^{\mu\nu}
-
\frac{p^\mu p^\nu}{p^2}
\right),
$$

则引入规范场

$$
A_\mu^I(X).
$$

其有效作用量为

$$
\Gamma_A
=
-\frac14
\int d^4X\sqrt{-g}
\frac1{g_I^2}
F_{\mu\nu}^IF^{I\mu\nu}
+
\cdots.
$$

规范耦合由流刚度决定：

$$
g_I^{-2}\sim C_J.
$$

费米子需要有效四标架和自旋结构。其作用量为

$$
\Gamma_\Psi
=
\int d^4X\sqrt{-g}
\bar\Psi
\left(
ie_a{}^\mu\gamma^aD_\mu
-
m_\Psi
\right)
\Psi.
$$

费米子可以来自扇区自旋算符极点、界面拓扑零模或双扇区复合费米子。若界面 Dirac 算符有零模

$$
\not D_I[\bar\Phi]\Psi_0=0,
$$

则低能手征性可由指数控制：

$$
n_L-n_R
=
\mathrm{index}(\not D_I).
$$

## 6.3 异常抵消

若低能费米子是手征的，必须满足规范异常抵消：

$$
\boxed{
\sum_f
\mathrm{Tr}_{R_f}
\left(
T^I\{T^J,T^K\}
\right)
=0.
}
$$

还要满足混合引力-规范异常抵消：

$$
\boxed{
\sum_f\mathrm{Tr}_{R_f}(T^I)=0.
}
$$

在 BNCFT 中异常来自

$$
\mathcal A
=
\mathcal A_+
+
\mathcal A_-
+
\mathcal A_I.
$$

健康低能理论要求

$$
\boxed{
\mathcal A_+
+
\mathcal A_-
+
\mathcal A_I
=0.
}
$$

若有未抵消 diffeomorphism anomaly，则会破坏 $\nabla_\mu T^\mu{}_{\nu}=0$，并与引力方程不相容。

## 6.4 等效原理的物质侧来源

某个物种 $s$ 的二次作用量一般写成

$$
\Gamma_s^{(2)}
=
\frac12
\int d^4X\sqrt{-g}
\psi_s
\left[
-\mathcal K_s^{\mu\nu}\nabla_\mu\nabla_\nu
+
m_s^2
+
\cdots
\right]
\psi_s.
$$

等效原理要求

$$
\boxed{
\mathcal K_s^{\mu\nu}
=
Z_sg^{\mu\nu}
+
\mathcal O(E^2/\Lambda_\mathrm{BNCFT}^2).
}
$$

归一化后

$$
\boxed{
g_{\mu\nu}^{(s)}
=
g_{\mu\nu}
+
\mathcal O(E^2/\Lambda_\mathrm{BNCFT}^2).
}
$$

因此所有低能物种共享同一个传播锥：

$$
g^{\mu\nu}p_\mu p_\nu+m_s^2=0.
$$

这就是 BNCFT 中等效原理的来源：

$$
\boxed{
\text{共享场锁定}
+
\text{物质普适投影}
+
\text{额外模式解耦}
\Rightarrow
\text{等效原理}.
}
$$

# 7. 诱导引力与 Planck 质量

## 7.1 有效引力作用量

积分掉短波共享场、共形扇区自由度和界面重模式后，在单度规相中得到：

$$
\Gamma_g[g]
=
\int d^4X\sqrt{-g}
\left[
\frac{c_0}{\ell_I^4}
+
\frac{c_1}{\ell_I^2}R
+
c_2R^2
+
c_3R_{\mu\nu}R^{\mu\nu}
+
\cdots
\right].
$$

与 Einstein-Hilbert 作用量比较：

$$
S_\mathrm{EH}
=
\frac1{16\pi G_\mathrm{eff}}
\int d^4X\sqrt{-g}
(R-2\Lambda_\mathrm{eff}),
$$

得到

$$
\boxed{
\frac1{16\pi G_\mathrm{eff}}
=
\frac{c_1}{\ell_I^2}.
}
$$

即

$$
\boxed{
M_\mathrm{Pl}^2
=
\frac1{8\pi G_\mathrm{eff}}
=
\frac{2c_1}{\ell_I^2}.
}
$$

因此 $G_\mathrm{eff}$ 不是基本常数，而是 BNCFT 界面相的红外响应：

$$
\boxed{
G_\mathrm{eff}
=
\frac{\ell_I^2}{16\pi c_1}.
}
$$

## 7.2 $c_1$ 的来源

$c_1$ 一般分解为

$$
\boxed{
c_1
=
c_1^\mathrm{stiff}
+
c_1^{(+)}
+
c_1^{(-)}
+
c_1^{(I)}
+
c_1^\mathrm{meas}.
}
$$

其中 $c_1^\mathrm{stiff}$ 来自共享场几何刚度，$c_1^{(\pm)}$ 来自两个共形扇区短波模式的应力响应，$c_1^{(I)}$ 来自界面通道，$c_1^\mathrm{meas}$ 来自关系冗余测度、规范固定和局域反项。

压缩写作：

$$
\boxed{
c_1
\sim
\alpha_\Phi K_\Phi
+
\alpha_+C_{T,+}
+
\alpha_-C_{T,-}
+
\alpha_IC_{T,I}
+
\alpha_\mathrm{lock}N_\mathrm{lock}
+
\delta c_1.
}
$$

这里 $K_\Phi$ 是共享场刚度，$C_T$ 是应力张量两点函数归一化，也可理解为有效中心荷或有效自由度数，$N_\mathrm{lock}$ 是界面锁定通道数。

因此：

$$
\boxed{
M_\mathrm{Pl}^2
\sim
\frac{
\text{共享场刚度}
+
\text{共形应力响应}
+
\text{界面锁定通道}
}{\ell_I^2}.
}
$$

## 7.3 响应函数定义

在平直背景附近

$$
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}.
$$

对 transverse-traceless 模式

$$
\partial^\mu h_{\mu\nu}^\mathrm{TT}=0,
\qquad
h^{\mathrm{TT}\mu}{}_{\mu}=0,
$$

有效作用量二次项为

$$
\Gamma_\mathrm{TT}^{(2)}
=
\frac12
\int\frac{d^4p}{(2\pi)^4}
h_{\mu\nu}^\mathrm{TT}(-p)
\Pi_2(p^2)
h^{\mathrm{TT}\mu\nu}(p).
$$

Einstein-Hilbert 项给出

$$
\Pi_2(p^2)
=
\frac{M_\mathrm{Pl}^2}{4}p^2
+
\mathcal O(p^4).
$$

所以

$$
\boxed{
M_\mathrm{Pl}^2
=
4
\left.
\frac{d\Pi_2(p^2)}{dp^2}
\right|_{p^2=0}.
}
$$

并且

$$
\boxed{
c_1
=
2\ell_I^2
\left.
\frac{d\Pi_2(p^2)}{dp^2}
\right|_{p^2=0}.
}
$$

因此 $c_1$ 是 BNCFT 对角自旋二关系应力响应的 $p^2$ 系数。健康 GR 相要求：

$$
\boxed{c_1>0.}
$$

## 7.4 大 $N_\mathrm{eff}$ 与经典引力

若

$$
C_{T,+}\sim N_+,
\qquad
C_{T,-}\sim N_-,
\qquad
C_{T,I}\sim N_I,
$$

则

$$
c_1\sim N_\mathrm{eff}.
$$

于是

$$
M_\mathrm{Pl}^2
\sim
\frac{N_\mathrm{eff}}{\ell_I^2}.
$$

这说明：

$$
\boxed{
\text{Planck 质量可以是大 }N_\mathrm{eff}\text{ 的集体刚度。}
}
$$

当 $N_\mathrm{eff}\gg1$ 时，引力涨落被压低，红外引力更经典。但大量物种也会降低有效量子引力截断：

$$
\Lambda_\mathrm{species}
\sim
\frac{M_\mathrm{Pl}}{\sqrt{N_\mathrm{light}}}.
$$

若 $N_\mathrm{light}\sim N_\mathrm{eff}$，则

$$
\Lambda_\mathrm{species}\sim\ell_I^{-1}.
$$

因此 $\ell_I^{-1}$ 是 BNCFT 几何接口的自然新物理尺度。

# 8. 低能广义相对论极限

综合以上结果，BNCFT 的低能有效作用量为

$$
\Gamma_\mathrm{IR}[g,\psi]
=
\frac1{16\pi G_\mathrm{eff}}
\int d^4X\sqrt{-g}
(R-2\Lambda_\mathrm{eff})
+
\Gamma_m[g,\psi]
+
\Gamma_\mathrm{corr}.
$$

其中

$$
\Gamma_\mathrm{corr}
=
\mathcal O
\left(
R^2\ell_I^2,
\frac{E^2}{m_b^2},
\frac{E^2}{m_\omega^2},
\frac{E^2}{M_\mathrm{hd}^2}
\right).
$$

变分得到

$$
G_{\mu\nu}
+
\Lambda_\mathrm{eff}g_{\mu\nu}
=
8\pi G_\mathrm{eff}T_{\mu\nu}
+
\Delta_{\mu\nu}.
$$

在

$$
E\ll\Lambda_\mathrm{GR},
$$

$$
R\ell_I^2\ll1,
$$

$$
|\Delta_{\mu\nu}|\ll |G_{\mu\nu}|,
$$

得到广义相对论低能极限：

$$
\boxed{
G_{\mu\nu}
+
\Lambda_\mathrm{eff}g_{\mu\nu}
=
8\pi G_\mathrm{eff}T_{\mu\nu}.
}
$$

其中

$$
\boxed{
G_\mathrm{eff}
=
\frac{\ell_I^2}{16\pi c_1}.
}
$$

以及

$$
\boxed{
\Lambda_\mathrm{eff}
=
-\frac{c_0}{2c_1}\ell_I^{-2}.
}
$$

# 9. BNCFT 到 GR 的相条件

BNCFT 不自动等于 GR。GR 是 BNCFT 相空间中的一个特殊健康红外相。该相需要满足以下条件。

| 条件 | 数学表达 | 作用 |
|---|---|---|
| rank-4 关系凝聚 | $\mathrm{rank}(\partial_iX^\mu[\bar\Phi])=4$ | 产生四维关系坐标 |
| 非退化有效标架 | $e_\mu{}^a=\ell_IE_A{}^a\partial_\mu\bar\Phi^A$, $\det e\neq0$ | 产生有效度规 |
| 对角 diffeomorphism | $\delta_\xi g_{\mu\nu}=\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu$ | 保证 Ward 恒等式 |
| 单度规锁定 | $g_{+\mu\nu}\simeq g_{-\mu\nu}\simeq g_{\mu\nu}$ | 避免双度规低能相 |
| 反对角模式重 | $m_b^2>0$, $E\ll m_b$ | 让 $b_{\mu\nu}$ 解耦 |
| 无 ghost | $c_1>0$，FP 锁定势，高导数 ghost 在截断以上 | 保证谱健康 |
| Weyl/dilaton 解耦 | $\omega$ 为冗余或 $m_\omega^2\gg E^2$ | 避免第五力或标量-张量低能相 |
| 物质普适耦合 | $g_{\mu\nu}^{(s)}=g_{\mu\nu}+\mathcal O(E^2/\Lambda^2)$ | 给出等效原理 |
| 异常抵消 | $\mathcal A^\mathrm{diff}=\mathcal A^\mathrm{gauge}=\mathcal A^\mathrm{mixed}=0$ | 保证量子一致性 |

满足这些条件时，BNCFT 在低能退化为

$$
\boxed{
\text{GR}
+
\text{低能物质 EFT}
+
\text{受压低的 BNCFT 修正}.
}
$$

# 10. 失败相与可排除边界

BNCFT 的优势之一是它给出明确失败条件。若

$$
c_1<0,
$$

则无质量自旋二模式是 ghost。若

$$
m_b\lesssim E,
$$

则反对角几何传播，低能是双度规理论。若

$$
m_\omega\lesssim E,
$$

则低能是标量-张量理论，可能出现第五力。若

$$
g_{\mu\nu}^{(s)}\neq g_{\mu\nu}^{(s')}
$$

在 leading order 成立，则等效原理破缺。若存在未抵消异常

$$
\nabla_\mu T^\mu{}_{\nu}=\mathcal A_\nu\neq0,
$$

则与引力方程不相容。若高曲率 ghost 低于 EFT 截断，则红外理论不健康。

因此 BNCFT 不是一个“任意解释一切”的框架，而是一个有明确健康条件和排除边界的相理论。

# 11. 尚未解决的问题

## 11.1 宇宙学常数问题

有效作用量中有

$$
\frac{c_0}{\ell_I^4}\int\sqrt{-g}.
$$

这给出

$$
\Lambda_\mathrm{eff}
=
-\frac{c_0}{2c_1}\ell_I^{-2}.
$$

若 $c_0\sim c_1$，则 $\Lambda_\mathrm{eff}$ 通常过大。因此 BNCFT 必须解释为什么

$$
|c_0|\ll |c_1|,
$$

或者为什么真空能不以普通方式引力化。可能机制包括双共形扇区抵消：

$$
c_0^{(+)}+c_0^{(-)}+c_0^{(I)}\approx0,
$$

或者 $\sqrt{-g}$ 不是微观体积元，真空能只改变共享场张力而不直接进入 Einstein 方程；也可能 $\Lambda$ 是全局约束下的积分常数。

## 11.2 宇宙学相

需要研究共享场均匀凝聚态

$$
\bar\Phi^A=\bar\Phi^A(t)
$$

是否诱导 FRW 度规

$$
ds^2=-dt^2+a^2(t)d\vec x^2.
$$

并推导

$$
H^2
=
\frac{8\pi G_\mathrm{eff}}3\rho
+
\frac{\Lambda_\mathrm{eff}}3
+
\Delta_\mathrm{BNCFT}.
$$

其中

$$
\Delta_\mathrm{BNCFT}
\sim
\mathcal O(H^4\ell_I^2,\dot H H^2\ell_I^2,\cdots).
$$

## 11.3 黑洞与视界

在 BNCFT 中，视界可能解释为共享场关系映射的因果退化面：

$$
g^{\mu\nu}\partial_\mu r\partial_\nu r=0.
$$

黑洞熵可能来自双共形扇区通过共享场的界面纠缠：

$$
S_\mathrm{BH}
=
\frac{A}{4G_\mathrm{eff}}
+
\alpha\log\frac{A}{\ell_I^2}
+
\cdots.
$$

这需要单独发展。

## 11.4 现象学窗口

BNCFT 的偏离可能出现在等效原理破缺、引力波色散、变动 $G_\mathrm{eff}$、暗能量演化、黑洞熵修正以及高曲率早期宇宙修正。一般形式为

$$
g_{\mu\nu}^{(s)}
-
g_{\mu\nu}^{(s')}
=
\mathcal O(E^2/\Lambda_\mathrm{BNCFT}^2),
$$

$$
v_\mathrm{GW}^2
=
1+
\alpha_\mathrm{GW}E^2\ell_I^2+
\cdots,
$$

$$
G_\mathrm{eff}(t)
=
G_0[1+\epsilon_G(t)].
$$

这些给出可检验边界。

# 12. 结论

本文给出 BNCFT 的最小理论骨架。其核心是

$$
\boxed{
\mathcal C_+,
\quad
\mathcal C_-,
\quad
\Phi^A,
\quad
\mathcal G_\mathrm{rel}.
}
$$

微观层面没有

$$
x^\mu,
\qquad
g_{\mu\nu},
\qquad
\sqrt{-g},
\qquad
\nabla_\mu,
\qquad
\text{因果锥}.
$$

这些对象在共享场的 rank-4 几何相中出现：

$$
\Phi^A
\longrightarrow
X^\mu[\Phi]
\longrightarrow
e_\mu{}^a
\longrightarrow
g_{\mu\nu}^\mathrm{eff}.
$$

关系冗余在红外投影为微分同胚不变性，并通过 Ward 恒等式给出

$$
\nabla_\mu T^\mu{}_{\nu}=0.
$$

双扇区几何通过共享场锁定进入单度规相：

$$
g_{+\mu\nu}\simeq g_{-\mu\nu}\simeq g_{\mu\nu}.
$$

反对角模式、Weyl 模和高导数 ghost 必须在低能解耦。物质场来自关系算符的低能极点、守恒流、界面零模和双扇区复合态。所有低能物种共享同一个传播锥，从而产生等效原理。

积分掉短波模式后得到

$$
\Gamma_g[g]
=
\int\sqrt{-g}
\left[
\frac{c_0}{\ell_I^4}
+
\frac{c_1}{\ell_I^2}R
+
\cdots
\right].
$$

其中

$$
\boxed{
M_\mathrm{Pl}^2
=
\frac{2c_1}{\ell_I^2},
}
$$

$$
\boxed{
G_\mathrm{eff}
=
\frac{\ell_I^2}{16\pi c_1}.
}
$$

而

$$
c_1
\sim
\alpha_\Phi K_\Phi
+
\alpha_+C_{T,+}
+
\alpha_-C_{T,-}
+
\alpha_IC_{T,I}
+
\alpha_\mathrm{lock}N_\mathrm{lock}
+
\delta c_1.
$$

因此，在 BNCFT 中，引力强度是共享场几何刚度、共形应力响应和界面锁定通道的集体结果。

最终，在满足

$$
E\ll\Lambda_\mathrm{GR},
\qquad
R\ell_I^2\ll1,
\qquad
c_1>0
$$

以及异常抵消、单度规锁定、额外模式解耦等条件时，BNCFT 的红外方程为

$$
\boxed{
G_{\mu\nu}
+
\Lambda_\mathrm{eff}g_{\mu\nu}
=
8\pi G_\mathrm{eff}T_{\mu\nu}
+
\mathcal O(E^2/\Lambda_\mathrm{BNCFT}^2,R\ell_I^2).
}
$$

这就是 BNCFT 到广义相对论的低能极限。
