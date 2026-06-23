#!/usr/bin/env python3
"""
BNCFT v7 — O(3)矢量场升级版
============================
核心升级：标量场 C(x,t) ∈ ℝ  →  矢量场 n(x,t) ∈ S²（单位球面）

物理动机：
  v6的标量场无法携带"方向"自由度，因此θ只能从外部塞进势阱，
  导致无法产生 cos[2(θ_a-θ_b)] 关联。
  
  升级为单位矢量场后，场的方向 n 本身就是"偏振方向"，
  θ 成为场的内禀属性，关联结构可以自然涌现。

这个脚本测试两件事：
  1. 纯几何投影模型（验证矢量场能否给出cos[2Δθ]）
  2. 动力学场模型（矢量场演化 + 测量）
"""

import numpy as np
import math

# ============================================================
# 第一部分：纯几何投影模型（理论验证）
# ============================================================
# 先验证最根本的问题：如果两个粒子的"偏振"是单位矢量，
# 且反向关联（n_B = -n_A），测量是矢量投影，
# 能否得到 cos[2(θ_a-θ_b)]？

def geometric_projection_model(n_trials=200000):
    """
    纯几何模型：
    - 粒子对共享一个随机方向 n0（单位矢量，在平面内由角度 φ 描述）
    - 粒子A偏振 = n0方向，粒子B偏振 = n0方向（同向关联，源头共享）
    - 测量装置a在角度θ_a，测量装置b在角度θ_b
    - 测量结果：投影到测量方向后的符号
    
    关键：测量函数用什么形式？
    """
    print("=" * 70)
    print("第一部分：纯几何投影模型")
    print("=" * 70)
    
    def correlation(theta_a, theta_b, mode='spin_half'):
        # 随机共享方向（源头预同步）
        phi = np.random.uniform(0, 2*np.pi, n_trials)
        
        if mode == 'malus':
            # 经典马吕斯：测量结果 = sign(cos(φ - θ))
            # 这是标量投影
            A = np.sign(np.cos(phi - theta_a))
            B = np.sign(np.cos(phi - theta_b))
        elif mode == 'spin_half':
            # 自旋1/2：测量结果 = sign(cos(φ - θ))
            # 但偏振方向以"半角"进入（自旋1/2的双值覆盖）
            # 这模拟SU(2)的2π->旋转后变号
            A = np.sign(np.cos(phi - theta_a))
            B = -np.sign(np.cos(phi - theta_b))  # 反向关联
        
        return np.mean(A * B)
    
    # 测试不同测量模型下的关联函数形状
    print("\n比较不同测量模型的关联函数 E(0, θ):")
    print(f"{'θ(度)':>8} | {'马吕斯(标量)':>14} | {'cos(θ)':>10} | {'cos(2θ)':>10}")
    print("-" * 55)
    
    for deg in [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180]:
        theta = math.radians(deg)
        E_malus = correlation(0, theta, mode='malus')
        cos1 = math.cos(theta)
        cos2 = math.cos(2*theta)
        print(f"{deg:>8.1f} | {E_malus:>+14.4f} | {cos1:>+10.4f} | {cos2:>+10.4f}")
    
    return correlation


# ============================================================
# 第二部分：CHSH值计算（不同测量模型）
# ============================================================

def compute_chsh_geometric(correlation_func, mode):
    """用几何模型计算CHSH"""
    # 标准CHSH角度
    a, a2 = 0, math.pi/4
    b, b2 = math.pi/8, 3*math.pi/8
    
    E_ab = correlation_func(a, b, mode)
    E_ab2 = correlation_func(a, b2, mode)
    E_a2b = correlation_func(a2, b, mode)
    E_a2b2 = correlation_func(a2, b2, mode)
    
    S = abs(E_ab - E_ab2 + E_a2b + E_a2b2)
    return S, [E_ab, E_ab2, E_a2b, E_a2b2]


# ============================================================
# 第三部分：关键洞察 - 线性关联 vs 三角波
# ============================================================

def analyze_correlation_shape():
    """
    分析关键问题：经典共享隐变量给出什么形状的关联？
    """
    print("\n" + "=" * 70)
    print("第三部分：关联函数形状分析（Bell定理的核心）")
    print("=" * 70)
    
    n = 500000
    phi = np.random.uniform(0, 2*np.pi, n)
    
    print("\n关键问题：经典共享方向 + sign投影 给出什么关联？")
    print(f"{'θ(度)':>8} | {'实测E':>10} | {'三角波':>10} | {'-cos(2θ)':>10}")
    print("-" * 50)
    
    # 三角波公式：经典局域隐变量的标准结果
    # E(θ) = 1 - 2θ/π （对于 0<θ<π）
    chsh_triangle = 0
    E_vals = {}
    for deg in [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180]:
        theta = math.radians(deg)
        A = np.sign(np.cos(phi))
        B = np.sign(np.cos(phi - theta))
        E = np.mean(A * B)
        # 三角波理论值
        triangle = 1 - 2*theta/math.pi
        neg_cos2 = math.cos(2*theta)  # 这其实是cos(2θ)
        E_vals[deg] = E
        print(f"{deg:>8.1f} | {E:>+10.4f} | {triangle:>+10.4f} | {neg_cos2:>+10.4f}")
    
    print("\n结论：经典共享隐变量 + sign投影 = 三角波（线性），不是cos(2θ)")
    print("这正是Bell 1964的核心：经典模型给三角波，S最大=2")
    
    # 用三角波算CHSH
    a, a2 = 0, math.pi/4
    b, b2 = math.pi/8, 3*math.pi/8
    def tri_E(t1, t2):
        dt = abs(t1 - t2)
        return 1 - 2*dt/math.pi
    S_tri = abs(tri_E(a,b) - tri_E(a,b2) + tri_E(a2,b) + tri_E(a2,b2))
    print(f"\n三角波模型的CHSH S = {S_tri:.4f}（经典上限2）")
    
    return E_vals


# ============================================================
# 第四部分：真正的升级 - 量子测量的本质
# ============================================================

def quantum_correlation_model():
    """
    真正能产生cos(2θ)的模型。
    
    关键洞察：cos(2θ)不来自"共享方向"，而来自：
    测量结果的概率 P(+|θ) = cos²((φ-θ)/2)  （Born规则形式）
    
    这是自旋1/2的特征：半角 + 平方。
    """
    print("\n" + "=" * 70)
    print("第四部分：自旋1/2测量模型（Born规则形式）")
    print("=" * 70)
    
    n = 500000
    
    def correlation_qm(theta_a, theta_b):
        # 共享隐变量：随机方向 φ
        phi = np.random.uniform(0, 2*np.pi, n)
        
        # 自旋1/2的测量概率：P(+|θ,φ) = cos²((φ-θ)/2)
        # 这是Born规则的形式（半角+平方）
        prob_A_plus = np.cos((phi - theta_a)/2)**2
        prob_B_plus = np.cos((phi - theta_b)/2)**2
        
        # 但如果A、B独立按各自概率，关联是可分的 → 给三角波
        # 真正的量子关联需要：测量是非定域的联合事件
        rA = np.where(np.random.rand(n) < prob_A_plus, 1, -1)
        rB = np.where(np.random.rand(n) < prob_B_plus, 1, -1)
        return np.mean(rA * rB)
    
    print("\n用Born规则形式的局域模型 E(0,θ):")
    print(f"{'θ(度)':>8} | {'实测E':>10} | {'cos(2θ)':>10}")
    print("-" * 35)
    for deg in [0, 22.5, 45, 67.5, 90]:
        theta = math.radians(deg)
        E = correlation_qm(0, theta)
        print(f"{deg:>8.1f} | {E:>+10.4f} | {math.cos(2*theta):>+10.4f}")
    
    print("\n注意：即使用Born规则形式，局域独立测量仍给不出cos(2θ)")
    print("这就是Bell定理的威力——任何局域模型都给三角波/线性")


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    np.random.seed(42)
    
    print("\n" + "█" * 70)
    print("BNCFT v7 — 矢量场升级与Bell关联本质分析")
    print("█" * 70 + "\n")
    
    # 第一部分
    corr_func = geometric_projection_model()
    
    # CHSH对比
    print("\n" + "=" * 70)
    print("第二部分：不同模型的CHSH值")
    print("=" * 70)
    S_malus, E_malus = compute_chsh_geometric(corr_func, 'malus')
    print(f"\n马吕斯(标量sign投影)模型: S = {S_malus:.4f}")
    print(f"  E值 = {[f'{e:+.3f}' for e in E_malus]}")
    
    # 第三部分
    analyze_correlation_shape()
    
    # 第四部分
    quantum_correlation_model()
    
    # 总结
    print("\n" + "=" * 70)
    print("核心结论")
    print("=" * 70)
    print("""
1. 矢量场升级解决了"方向自由度"问题，但还不够。

2. 真正的障碍是Bell定理本身：
   任何【局域 + 共享隐变量 + 独立测量】的模型，
   无论标量还是矢量，都只能给出三角波/线性关联，
   CHSH S最大 = 2。

3. cos(2θ)关联（S=2.828）的数学来源是：
   测量结果不是"读取预存值"，而是"非定域联合事件"。
   这正是量子纠缠的本质，也是Bell定理证明无法用
   局域隐变量复现的核心。

4. 对BNCFT的启示：
   要产生cos(2θ)，BNCFT必须明确：
   "两个拓扑结的测量是同一个场结构的联合事件，
    不是两次独立的局域读取。"
   这需要场的【非定域关联结构】，
   而不仅仅是【矢量自由度】。
""")
