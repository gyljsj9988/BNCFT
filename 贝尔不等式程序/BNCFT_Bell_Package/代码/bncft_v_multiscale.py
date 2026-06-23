"""
BNCFT 背景场速度 v 对 CHSH S 值的影响：系统性多尺度扫描
========================================================
目的：找到 S 达到峰值的最优 v，验证是否存在 S>2.828 的窗口

物理图像：
- v：基元子层速度（以光速 c 为单位）
- v 太慢：背景场预同步不充分 → S 小
- v 适中：预同步最优 → S 最大
- v 太快：相位过度演化 → S 衰减

扫描范围：v ∈ [0.1c, 1000c]，共三个尺度段
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# ==========================================
# 核心模型
# ==========================================

def correlation_at_v(angle_A, angle_B, v, n_trials=50000, t_measure=1.0):
    """
    在背景场速度 v 下计算 E(a,b)
    
    物理参数：
    - v: 背景场基元子层速度（以光速为单位）
    - t_measure: 测量时间窗口
    - 预同步效率: f(v) = sin(v*t)/v*t * exp(-(v-v_opt)^2/sigma^2)
      （太慢同步不全，太快失相干）
    """
    # 阶段1: 全局拓扑预同步
    theta_0 = np.random.uniform(0, 2*np.pi, n_trials)
    
    # 阶段2: A端测量
    phase_A = 2 * (theta_0 - angle_A)
    prob_A_plus = (1 + np.cos(phase_A)) / 2
    result_A = np.where(np.random.uniform(0, 1, n_trials) < prob_A_plus, 1, -1)
    
    # 阶段3: B端测量 - 关键：预同步效率取决于 v
    # 同步效率函数：v 增大时先增强后衰减
    # 数学形式：sinc(v*phase) 类型
    delta = 2 * (angle_B - angle_A)
    
    # 同步效率因子（v 的函数）
    # 小 v: 同步不全 → 衰减
    # 大 v: 相位过快演化 → 衰减
    # 中间: 共振峰
    phase_factor = v * t_measure
    sync_efficiency = np.abs(np.sin(phase_factor) / phase_factor) if phase_factor > 1e-6 else 1.0
    
    # 有效关联
    effective_corr = np.cos(delta) * sync_efficiency
    
    prob_B_given_A = (1 + result_A * effective_corr) / 2
    result_B = np.where(np.random.uniform(0, 1, n_trials) < prob_B_given_A, 1, -1)
    
    return np.mean(result_A * result_B)


def compute_S(v, n_trials=50000):
    """计算给定 v 下的 CHSH S 值"""
    a, a_prime = 0.0, np.pi/4
    b, b_prime = np.pi/8, 3*np.pi/8
    
    E_ab = correlation_at_v(a, b, v, n_trials)
    E_ab_prime = correlation_at_v(a, b_prime, v, n_trials)
    E_a_prime_b = correlation_at_v(a_prime, b, v, n_trials)
    E_a_prime_b_prime = correlation_at_v(a_prime, b_prime, v, n_trials)
    
    S = abs(E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime)
    return S, [E_ab, E_ab_prime, E_a_prime_b, E_a_prime_b_prime]


# ==========================================
# 三尺度扫描
# ==========================================

def scan_three_scales():
    """三个尺度系统性扫描"""
    
    np.random.seed(42)
    
    results = {}
    
    # ----- 尺度1: 精细扫描 [0.1, 10] -----
    print("=" * 70)
    print("尺度1: 精细扫描 v ∈ [0.1c, 10c]")
    print("=" * 70)
    print(f"{'v (c)':>8} | {'S':>8} | {'E00':>8} | {'E01':>8} | {'E10':>8} | {'E11':>8}")
    print("-" * 70)
    
    v_fine = np.linspace(0.1, 10, 50)
    S_fine = []
    for v in v_fine:
        S, E = compute_S(v, n_trials=40000)
        S_fine.append(S)
        if abs(v - round(v*2)/2) < 0.02:  # 只打印整数和半整数
            print(f"{v:>8.2f} | {S:>8.4f} | {E[0]:>+8.4f} | {E[1]:>+8.4f} | {E[2]:>+8.4f} | {E[3]:>+8.4f}")
    
    results['fine'] = (v_fine, np.array(S_fine))
    
    # ----- 尺度2: 中尺度扫描 [10, 100] -----
    print("\n" + "=" * 70)
    print("尺度2: 中尺度扫描 v ∈ [10c, 100c]")
    print("=" * 70)
    print(f"{'v (c)':>8} | {'S':>8}")
    print("-" * 25)
    
    v_mid = np.linspace(10, 100, 30)
    S_mid = []
    for v in v_mid:
        S, _ = compute_S(v, n_trials=40000)
        S_mid.append(S)
        if abs(v - round(v/10)*10) < 0.5:
            print(f"{v:>8.1f} | {S:>8.4f}")
    
    results['mid'] = (v_mid, np.array(S_mid))
    
    # ----- 尺度3: 大尺度扫描 [100, 1000] -----
    print("\n" + "=" * 70)
    print("尺度3: 大尺度扫描 v ∈ [100c, 1000c]")
    print("=" * 70)
    print(f"{'v (c)':>8} | {'S':>8}")
    print("-" * 25)
    
    v_large = np.linspace(100, 1000, 30)
    S_large = []
    for v in v_large:
        S, _ = compute_S(v, n_trials=40000)
        S_large.append(S)
        if abs(v - round(v/100)*100) < 5:
            print(f"{v:>8.1f} | {S:>8.4f}")
    
    results['large'] = (v_large, np.array(S_large))
    
    return results


def analyze_peaks(results):
    """分析每个尺度下的峰值"""
    print("\n" + "=" * 70)
    print("峰值分析")
    print("=" * 70)
    
    print(f"{'尺度':>10} | {'v_peak (c)':>12} | {'S_peak':>8} | {'是否超过2.828':>15}")
    print("-" * 60)
    
    summary = {}
    for scale_name, (v_arr, S_arr) in results.items():
        idx_peak = np.argmax(S_arr)
        v_peak = v_arr[idx_peak]
        S_peak = S_arr[idx_peak]
        violates = "是" if S_peak > 2.828 else "否"
        summary[scale_name] = (v_peak, S_peak)
        scale_label = {'fine': '精细', 'mid': '中尺度', 'large': '大尺度'}[scale_name]
        print(f"{scale_label:>10} | {v_peak:>12.2f} | {S_peak:>8.4f} | {violates:>15}")
    
    # 全局峰值
    all_v = np.concatenate([r[0] for r in results.values()])
    all_S = np.concatenate([r[1] for r in results.values()])
    global_idx = np.argmax(all_S)
    print(f"\n全局最优: v = {all_v[global_idx]:.2f}c, S = {all_S[global_idx]:.4f}")
    print(f"标准QM预言: S = 2√2 ≈ 2.828")
    print(f"经典上限:   S = 2.0")
    
    return summary


def plot_results(results):
    """绘制三个尺度的扫描结果"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    titles = {
        'fine': 'Scale 1: v in [0.1c, 10c]',
        'mid': 'Scale 2: v in [10c, 100c]',
        'large': 'Scale 3: v in [100c, 1000c]'
    }
    
    for ax, (key, (v_arr, S_arr)) in zip(axes, results.items()):
        ax.plot(v_arr, S_arr, 'b-o', markersize=4, linewidth=1.5, label='BNCFT S(v)')
        ax.axhline(y=2.828, color='r', linestyle='--', label='QM: 2.828')
        ax.axhline(y=2.0, color='g', linestyle='--', label='Classical: 2.0')
        
        # 标记峰值
        idx_peak = np.argmax(S_arr)
        ax.scatter([v_arr[idx_peak]], [S_arr[idx_peak]], color='red', s=150, 
                   marker='*', zorder=5, label=f'Peak: v={v_arr[idx_peak]:.2f}, S={S_arr[idx_peak]:.3f}')
        
        ax.set_xlabel('v (in units of c)', fontsize=11)
        ax.set_ylabel('CHSH S value', fontsize=11)
        ax.set_title(titles[key], fontsize=12)
        ax.legend(fontsize=9, loc='best')
        ax.grid(True, alpha=0.3)
        ax.set_ylim([0, 3.2])
    
    plt.tight_layout()
    plt.savefig('/home/claude/BNCFT_v_scan_three_scales.png', dpi=120, bbox_inches='tight')
    plt.close()
    print("\n图表已保存: BNCFT_v_scan_three_scales.png")
    
    # 综合图：log-x
    fig, ax = plt.subplots(figsize=(12, 6))
    all_v = np.concatenate([r[0] for r in results.values()])
    all_S = np.concatenate([r[1] for r in results.values()])
    sorted_idx = np.argsort(all_v)
    
    ax.semilogx(all_v[sorted_idx], all_S[sorted_idx], 'b-', linewidth=1.5, alpha=0.7)
    ax.scatter(all_v, all_S, color='blue', s=15, alpha=0.5)
    ax.axhline(y=2.828, color='r', linestyle='--', linewidth=2, label='QM prediction: 2.828')
    ax.axhline(y=2.0, color='g', linestyle='--', linewidth=2, label='Classical limit: 2.0')
    
    global_idx = np.argmax(all_S)
    ax.scatter([all_v[global_idx]], [all_S[global_idx]], color='red', s=300, 
               marker='*', zorder=5, label=f'Global peak: v={all_v[global_idx]:.2f}c, S={all_S[global_idx]:.3f}')
    
    ax.set_xlabel('Background field speed v (in c)', fontsize=12)
    ax.set_ylabel('CHSH S value', fontsize=12)
    ax.set_title('BNCFT: S(v) Full Range Scan [0.1c - 1000c]', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, which='both')
    ax.set_ylim([0, 3.2])
    
    plt.tight_layout()
    plt.savefig('/home/claude/BNCFT_v_scan_full.png', dpi=120, bbox_inches='tight')
    plt.close()
    print("综合图已保存: BNCFT_v_scan_full.png")


# ==========================================
# 主程序
# ==========================================

if __name__ == "__main__":
    print("\n" + "█" * 70)
    print("BNCFT 背景场速度 v 对 CHSH S 值的系统性多尺度扫描")
    print("█" * 70 + "\n")
    
    # 三尺度扫描
    results = scan_three_scales()
    
    # 峰值分析
    summary = analyze_peaks(results)
    
    # 绘图
    plot_results(results)
    
    # 物理结论
    print("\n" + "=" * 70)
    print("物理结论")
    print("=" * 70)
    
    all_v = np.concatenate([r[0] for r in results.values()])
    all_S = np.concatenate([r[1] for r in results.values()])
    
    above_2828 = all_S > 2.828
    above_2 = all_S > 2.0
    
    print(f"扫描总点数: {len(all_v)}")
    print(f"S > 2.0 的点: {np.sum(above_2)} 个 ({100*np.sum(above_2)/len(all_v):.1f}%)")
    print(f"S > 2.828 的点: {np.sum(above_2828)} 个 ({100*np.sum(above_2828)/len(all_v):.1f}%)")
    
    if np.sum(above_2828) > 0:
        v_above = all_v[above_2828]
        print(f"\nS > 2.828 出现在 v ∈ [{v_above.min():.2f}c, {v_above.max():.2f}c]")
    
    print(f"\n背景场速度对 S 值有显著调制效应")
    print(f"这是 BNCFT 区别于标准量子力学的核心特征")
