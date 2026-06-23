#!/usr/bin/env python3
"""
BNCFT v8 — 路2：场层面联合测量模型
=====================================
核心思想：
  两个拓扑结不是独立粒子，而是同一个连通场结构的两端。
  测量A和测量B不是两次独立读取，而是整个场结构在
  两个边界条件(θ_a, θ_b)下的【联合响应】。

诚实声明：
  本脚本逐步测试不同的"联合测量"机制，
  每一步都明确标注：
    [物理] = 有物理动机的设定
    [凑数] = 为了得到cos(2θ)而人为加入（需要警惕）

目标：找出能给出cos(2θ)的最小物理假设，
     并判断这个假设是否物理合理，还是又一次凑数。
"""

import numpy as np
import math


# ============================================================
# 测试1：共享相位 + 联合投影（最朴素的非定域尝试）
# ============================================================

def test1_shared_phase_joint():
    """
    [物理] 共享场结构：A、B共享同一个相位变量 φ
    [测试] 联合测量：测量结果同时依赖 θ_a, θ_b, φ
    
    问题：什么样的联合测量函数能给cos(2θ)？
    """
    print("=" * 70)
    print("测试1：共享相位 + 不同联合测量函数")
    print("=" * 70)
    
    n = 500000
    phi = np.random.uniform(0, 2*np.pi, n)
    
    # 尝试几种联合测量函数
    def joint_A_minus_B(theta_a, theta_b):
        # [凑数] 直接用 cos(θ_a - θ_b) —— 这是作弊，A单独不该知道θ_b
        # 仅作为对照
        return math.cos(2*(theta_a - theta_b))
    
    def joint_via_field(theta_a, theta_b):
        # [物理] A的结果只依赖θ_a和φ，B的结果只依赖θ_b和φ
        # 但用矢量内积形式（自旋的双值覆盖：半角）
        # 关键尝试：场在测量点的投影 = cos(φ - θ)，结果取符号
        sA = np.sign(np.cos(phi - theta_a))
        sB = np.sign(np.cos(phi - theta_b))
        return np.mean(sA * sB)
    
    print("\n对照不同测量函数 E(0,θ):")
    print(f"{'θ(度)':>8} | {'场投影(局域)':>14} | {'目标cos(2θ)':>12}")
    print("-" * 45)
    for deg in [0, 22.5, 45, 67.5, 90]:
        theta = math.radians(deg)
        E_field = joint_via_field(0, theta)
        print(f"{deg:>8.1f} | {E_field:>+14.4f} | {math.cos(2*theta):>+12.4f}")
    
    print("\n→ 局域场投影还是三角波，确认路1走不通")


# ============================================================
# 测试2：真正的非定域 - 场的全局约束
# ============================================================

def test2_global_constraint():
    """
    [物理] 关键升级：场不是在A、B处独立取值，
           而是整个场满足一个【全局约束】。
    
    具体：把两个测量看作对同一个2维场矢量的两次投影，
         但这个矢量在测量瞬间被"联合归一化"。
    
    这模拟了：测量是整体事件，不是局域读取。
    """
    print("\n" + "=" * 70)
    print("测试2：全局约束下的联合测量")
    print("=" * 70)
    
    n = 500000
    
    def correlation(theta_a, theta_b):
        # [物理] 共享一个2维场矢量，方向随机
        phi = np.random.uniform(0, 2*np.pi, n)
        
        # 场在A测量方向的分量
        proj_A = np.cos(phi - theta_a)
        # 场在B测量方向的分量
        proj_B = np.cos(phi - theta_b)
        
        # [关键尝试-物理?] 联合测量：
        # 结果不是各自取符号，而是看两个投影的"联合符号关系"
        # 如果场是一个整体，测量A影响了场在B的呈现
        # 用投影的乘积符号作为联合结果
        joint = proj_A * proj_B
        # 联合事件的关联 = <sign(proj_A * proj_B)> 的某种形式
        E = np.mean(np.sign(joint))
        return E
    
    print("\nE(0,θ) 用联合符号:")
    print(f"{'θ(度)':>8} | {'联合符号':>10} | {'cos(2θ)':>10}")
    print("-" * 35)
    for deg in [0, 22.5, 45, 67.5, 90]:
        theta = math.radians(deg)
        E = correlation(0, theta)
        print(f"{deg:>8.1f} | {E:>+10.4f} | {math.cos(2*theta):>+10.4f}")
    
    # 检查：sign(cos(φ-a)cos(φ-b))的平均
    # 数学上 = 1 - 2*(被积区域)/2π
    print("\n→ 检查这个形状是什么")


# ============================================================
# 测试3：连续值联合测量（不取符号）
# ============================================================

def test3_continuous_joint():
    """
    [物理] 测量结果是连续的场投影值，不强制±1。
    [物理] 关联 = 两个投影的统计平均。
    
    这对应：测量读取的是场振幅，不是二值化的"咔哒"。
    """
    print("\n" + "=" * 70)
    print("测试3：连续值联合测量（场振幅，不二值化）")
    print("=" * 70)
    
    n = 500000
    
    def correlation(theta_a, theta_b):
        phi = np.random.uniform(0, 2*np.pi, n)
        # 连续投影值（不取符号）
        proj_A = np.cos(phi - theta_a)
        proj_B = np.cos(phi - theta_b)
        # 关联 = <proj_A * proj_B>
        E = np.mean(proj_A * proj_B)
        # 归一化（使E(0,0)=1）
        return E * 2  # <cos*cos>=1/2 cos(a-b)，乘2归一化
    
    print("\nE(0,θ) 连续投影乘积:")
    print(f"{'θ(度)':>8} | {'连续投影':>10} | {'cos(θ)':>10} | {'cos(2θ)':>10}")
    print("-" * 48)
    for deg in [0, 22.5, 45, 67.5, 90, 135, 180]:
        theta = math.radians(deg)
        E = correlation(0, theta)
        print(f"{deg:>8.1f} | {E:>+10.4f} | {math.cos(theta):>+10.4f} | {math.cos(2*theta):>+10.4f}")
    
    print("\n→ 连续投影给cos(θ)，不是cos(2θ)。差一个因子2。")
    print("   这个因子2是关键！需要'半角'结构。")


# ============================================================
# 测试4：半角结构 - 自旋1/2的核心
# ============================================================

def test4_half_angle():
    """
    [物理?] 关键洞察：cos(2θ)中的因子2来自'半角'。
    
    如果拓扑结的'方向'以半角进入测量（即旋转2π变号），
    那么投影是 cos((φ-θ)/2)，关联可能给cos(θ_a-θ_b)。
    
    这正是自旋1/2（SU(2)双值覆盖）的特征。
    BNCFT的拓扑结如果有这个性质，就能产生量子关联。
    """
    print("\n" + "=" * 70)
    print("测试4：半角结构（SU(2)双值覆盖）")
    print("=" * 70)
    
    n = 1000000
    
    def correlation_halfangle(theta_a, theta_b):
        phi = np.random.uniform(0, 4*np.pi, n)  # 注意：4π周期（双值覆盖）
        # 半角投影
        proj_A = np.cos((phi - theta_a)/2)
        proj_B = np.cos((phi - theta_b)/2)
        E = np.mean(proj_A * proj_B)
        return E * 2
    
    print("\nE(0,θ) 半角连续投影:")
    print(f"{'θ(度)':>8} | {'半角投影':>10} | {'cos(θ)':>10}")
    print("-" * 35)
    for deg in [0, 45, 90, 135, 180, 270, 360]:
        theta = math.radians(deg)
        E = correlation_halfangle(0, theta)
        print(f"{deg:>8.1f} | {E:>+10.4f} | {math.cos(theta):>+10.4f}")
    
    print("\n→ 半角给出更长周期，但仍是连续投影本质")


# ============================================================
# 测试5：诚实的最终对照 - 量子关联到底需要什么
# ============================================================

def test5_what_quantum_needs():
    """
    诚实地展示：量子cos(2θ)关联，在数学上等价于什么。
    
    量子关联 E(a,b) = -cos(2(a-b)) 来自：
      ⟨ψ| σ·a ⊗ σ·b |ψ⟩  其中|ψ⟩是Bell态
    
    这个表达式的关键：σ·a 和 σ·b 是【不对易】的算符，
    它们作用在【纠缠态】上，不能分解为独立的局域值。
    """
    print("\n" + "=" * 70)
    print("测试5：量子关联的真正数学结构")
    print("=" * 70)
    
    # 直接用量子力学公式
    print("\n标准量子力学（Bell态 + Pauli算符）:")
    print(f"{'θ(度)':>8} | {'量子E=-cos(2θ)':>16}")
    print("-" * 30)
    for deg in [0, 22.5, 45, 67.5, 90]:
        theta = math.radians(deg)
        E_qm = -math.cos(2*theta)
        print(f"{deg:>8.1f} | {E_qm:>+16.4f}")
    
    # 量子CHSH
    a, a2 = 0, math.pi/4
    b, b2 = math.pi/8, 3*math.pi/8
    def qm_E(t1, t2):
        return -math.cos(2*(t1-t2))
    S = abs(qm_E(a,b) - qm_E(a,b2) + qm_E(a2,b) + qm_E(a2,b2))
    print(f"\n量子CHSH S = {S:.4f} = 2√2 ✓")
    
    print("""
关键数学事实：
  量子E(a,b) = -cos(2(a-b)) 中的(a-b)是【两个测量的角度差】
  但在局域模型里，A的结果只能依赖a（不能依赖b）
  
  -cos(2(a-b)) = -cos(2a)cos(2b) - sin(2a)sin(2b)
  
  这可以分解！如果A输出"矢量"(cos2a, sin2a)，
  B输出"矢量"(cos2b, sin2b)，关联是它们的内积。
  
  但单次测量结果必须是【标量±1】，不是矢量。
  正是"把矢量内积压缩成±1标量"这一步，
  局域模型做不到，量子纠缠能做到。
""")


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    np.random.seed(42)
    
    print("\n" + "█" * 70)
    print("BNCFT v8 — 路2：场层面联合测量探索")
    print("█" * 70 + "\n")
    
    test1_shared_phase_joint()
    test2_global_constraint()
    test3_continuous_joint()
    test4_half_angle()
    test5_what_quantum_needs()
    
    print("\n" + "=" * 70)
    print("总结：路2的探索结果")
    print("=" * 70)
    print("""
诚实结论：

1. 局域场投影（标量或矢量）→ 永远三角波，S=2

2. 连续投影乘积 → cos(θ)，差一个因子2

3. 半角结构 → 改变周期，但本质仍是局域

4. 真正的cos(2θ)需要：
   测量结果是【矢量内积】而非【标量乘积】，
   即单次测量必须"记住"一个方向，而不只是±1。
   
   这在数学上等价于：测量算符不对易（量子性）。

5. 对BNCFT的明确启示：
   如果BNCFT的拓扑结在测量时输出的是一个【内禀矢量】
   （比如拓扑结的指向、自旋方向），且两个结的测量
   通过共享场结构形成【矢量内积关联】，
   那么cos(2θ)可以涌现。

   关键问题变成：BNCFT的拓扑结测量，
   输出的是标量（±1）还是矢量（方向）？
   如果是矢量 → 有希望
   如果是标量 → 和经典一样，S≤2
""")
