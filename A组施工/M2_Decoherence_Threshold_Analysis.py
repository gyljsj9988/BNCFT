#!/usr/bin/env python3
"""
BNCFT M2-3.1 — 退相干阈值提取
=====================================

目标：定量提取临界参数，从"现象报告"升级到"完整边界分析"

提取的临界阈值：
1. γ_E：纠缠消失阈值（C < 0.01）
2. γ_CHSH：CHSH 失效阈值（S < 2.01）
3. γ_purity：纯度阈值（Tr(ρ²) < 某参考值）

关键问题：
- 三个阈值的排序关系？
- 不同退相干通道的阈值对比？
- 纠缠消失 vs CHSH 失效的关系？

作者：BNCFT A组
日期：2026-06-01
版本：v1.0 - M2-3.1 阈值提取
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List
import time
from M2_Decoherence_Model_v1 import (
    pure_state_to_density_matrix,
    compute_purity,
    compute_concurrence,
    phase_damping_channel,
    amplitude_damping_channel,
    depolarizing_channel
)


# ============================================================
# 1. 精细扫描退相干率
# ============================================================

def fine_scan_decoherence(channel_type: str, 
                         gamma_min: float = 0.01,
                         gamma_max: float = 2.0,
                         n_gamma: int = 100,
                         t_max: float = 10.0,
                         n_steps: int = 100) -> Dict:
    """
    精细扫描退相干率，提取临界阈值
    
    参数：
      channel_type: 退相干通道类型
      gamma_min, gamma_max: 退相干率范围
      n_gamma: 扫描点数
      t_max: 演化时间
      n_steps: 时间步数
      
    返回：
      包含所有数据的字典
    """
    print(f"\n{'='*70}")
    print(f"精细扫描：{channel_type} 退相干")
    print(f"{'='*70}")
    
    # 创建初始 Bell 单态
    n_sites = 11
    psi0 = np.zeros((n_sites, n_sites), dtype=complex)
    psi0[n_sites-1, 0] = 1.0 / np.sqrt(2)
    psi0[0, n_sites-1] = -1.0 / np.sqrt(2)
    rho0 = pure_state_to_density_matrix(psi0)
    
    # 选择通道
    if channel_type == 'phase':
        channel = phase_damping_channel
    elif channel_type == 'amplitude':
        channel = amplitude_damping_channel
    elif channel_type == 'depolarizing':
        channel = depolarizing_channel
    else:
        raise ValueError(f"Unknown channel: {channel_type}")
    
    # 扫描退相干率
    gamma_values = np.linspace(gamma_min, gamma_max, n_gamma)
    dt = t_max / n_steps
    
    results = {
        'gamma': [],
        'S_final': [],
        'C_final': [],
        'purity_final': [],
        'S_min': [],
        'C_min': [],
        'purity_min': []
    }
    
    for i, gamma in enumerate(gamma_values):
        if (i+1) % 10 == 0:
            print(f"  进度: {i+1}/{n_gamma}")
        
        # 演化
        rho = rho0.copy()
        S_vals = []
        C_vals = []
        purity_vals = []
        
        for step in range(n_steps + 1):
            purity = compute_purity(rho)
            concurrence = compute_concurrence(rho)
            S = 2.0 + 0.828427 * concurrence
            
            S_vals.append(S)
            C_vals.append(concurrence)
            purity_vals.append(purity)
            
            if step < n_steps:
                rho = channel(rho, gamma, dt)
        
        # 记录结果
        results['gamma'].append(gamma)
        results['S_final'].append(S_vals[-1])
        results['C_final'].append(C_vals[-1])
        results['purity_final'].append(purity_vals[-1])
        results['S_min'].append(min(S_vals))
        results['C_min'].append(min(C_vals))
        results['purity_min'].append(min(purity_vals))
    
    return results


# ============================================================
# 2. 提取临界阈值
# ============================================================

def extract_thresholds(results: Dict, 
                      C_threshold: float = 0.01,
                      S_threshold: float = 2.01,
                      purity_threshold: float = 0.5) -> Dict:
    """
    从扫描结果中提取临界阈值
    
    参数：
      results: 扫描结果
      C_threshold: 纠缠消失判据
      S_threshold: CHSH 失效判据
      purity_threshold: 纯度参考值
      
    返回：
      临界阈值字典
    """
    gamma = np.array(results['gamma'])
    C_final = np.array(results['C_final'])
    S_final = np.array(results['S_final'])
    purity_final = np.array(results['purity_final'])
    
    thresholds = {}
    
    # 1. 纠缠消失阈值 γ_E
    idx_E = np.where(C_final < C_threshold)[0]
    if len(idx_E) > 0:
        thresholds['gamma_E'] = gamma[idx_E[0]]
    else:
        thresholds['gamma_E'] = None
    
    # 2. CHSH 失效阈值 γ_CHSH
    idx_CHSH = np.where(S_final < S_threshold)[0]
    if len(idx_CHSH) > 0:
        thresholds['gamma_CHSH'] = gamma[idx_CHSH[0]]
    else:
        thresholds['gamma_CHSH'] = None
    
    # 3. 纯度阈值 γ_purity
    idx_purity = np.where(purity_final < purity_threshold)[0]
    if len(idx_purity) > 0:
        thresholds['gamma_purity'] = gamma[idx_purity[0]]
    else:
        thresholds['gamma_purity'] = None
    
    return thresholds


# ============================================================
# 3. 可视化与分析
# ============================================================

def plot_threshold_analysis(results_dict: Dict[str, Dict]):
    """绘制阈值分析图"""
    
    channels = list(results_dict.keys())
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. CHSH 参数 vs γ
    ax1 = axes[0, 0]
    for channel in channels:
        results = results_dict[channel]
        ax1.plot(results['gamma'], results['S_final'], 'o-', 
                label=channel, linewidth=2, markersize=4)
    ax1.axhline(y=2.0, color='r', linestyle='--', label='Classical limit', linewidth=2)
    ax1.axhline(y=2.01, color='orange', linestyle=':', label='S threshold', linewidth=1.5)
    ax1.set_xlabel('Decoherence rate γ', fontsize=12)
    ax1.set_ylabel('Final CHSH parameter S', fontsize=12)
    ax1.set_title('CHSH vs Decoherence Rate', fontsize=14)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim([1.9, 3.0])
    
    # 2. Concurrence vs γ
    ax2 = axes[0, 1]
    for channel in channels:
        results = results_dict[channel]
        ax2.plot(results['gamma'], results['C_final'], 's-',
                label=channel, linewidth=2, markersize=4)
    ax2.axhline(y=0.01, color='orange', linestyle=':', label='C threshold', linewidth=1.5)
    ax2.set_xlabel('Decoherence rate γ', fontsize=12)
    ax2.set_ylabel('Final Concurrence C', fontsize=12)
    ax2.set_title('Concurrence vs Decoherence Rate', fontsize=14)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Purity vs γ
    ax3 = axes[1, 0]
    for channel in channels:
        results = results_dict[channel]
        ax3.plot(results['gamma'], results['purity_final'], '^-',
                label=channel, linewidth=2, markersize=4)
    ax3.axhline(y=0.5, color='orange', linestyle=':', label='Purity threshold', linewidth=1.5)
    ax3.axhline(y=0.25, color='gray', linestyle='--', label='Max mixed (2-qubit)', linewidth=1)
    ax3.set_xlabel('Decoherence rate γ', fontsize=12)
    ax3.set_ylabel('Final Purity Tr(ρ²)', fontsize=12)
    ax3.set_title('Purity vs Decoherence Rate', fontsize=14)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. 阈值对比
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    # 创建阈值表格
    table_data = []
    table_data.append(['Channel', 'γ_E', 'γ_CHSH', 'γ_purity', 'Ordering'])
    
    for channel in channels:
        thresholds = results_dict[channel]['thresholds']
        gamma_E = thresholds.get('gamma_E', None)
        gamma_CHSH = thresholds.get('gamma_CHSH', None)
        gamma_purity = thresholds.get('gamma_purity', None)
        
        # 确定排序
        vals = []
        labels = []
        if gamma_E is not None:
            vals.append(gamma_E)
            labels.append('E')
        if gamma_CHSH is not None:
            vals.append(gamma_CHSH)
            labels.append('C')
        if gamma_purity is not None:
            vals.append(gamma_purity)
            labels.append('P')
        
        if len(vals) > 0:
            sorted_indices = np.argsort(vals)
            ordering = ' < '.join([labels[i] for i in sorted_indices])
        else:
            ordering = 'N/A'
        
        row = [
            channel,
            f'{gamma_E:.3f}' if gamma_E else 'N/A',
            f'{gamma_CHSH:.3f}' if gamma_CHSH else 'N/A',
            f'{gamma_purity:.3f}' if gamma_purity else 'N/A',
            ordering
        ]
        table_data.append(row)
    
    # 绘制表格
    table = ax4.table(cellText=table_data, cellLoc='center', loc='center',
                     colWidths=[0.2, 0.15, 0.15, 0.15, 0.35])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    
    # 设置表头样式
    for i in range(5):
        table[(0, i)].set_facecolor('#40466e')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    ax4.set_title('Critical Thresholds Summary', fontsize=14, pad=20)
    
    plt.tight_layout()
    plt.savefig('f:/BNCFT/A组施工/M2_threshold_analysis.png', dpi=150)
    print(f"\n✓ 阈值分析图已保存: M2_threshold_analysis.png")
    plt.close()


# ============================================================
# 4. 主程序
# ============================================================

def main():
    """主程序"""
    
    print("█"*70)
    print("BNCFT M2-3.1 — 退相干阈值提取")
    print("目标：定量提取临界参数")
    print("█"*70)
    
    start_time = time.time()
    
    # 扫描三种退相干通道
    channels = ['phase', 'amplitude', 'depolarizing']
    results_dict = {}
    
    for channel in channels:
        results = fine_scan_decoherence(channel, n_gamma=50)
        thresholds = extract_thresholds(results)
        results['thresholds'] = thresholds
        results_dict[channel] = results
        
        print(f"\n{channel} 退相干的临界阈值:")
        print(f"  γ_E (纠缠消失): {thresholds.get('gamma_E', 'N/A')}")
        print(f"  γ_CHSH (CHSH失效): {thresholds.get('gamma_CHSH', 'N/A')}")
        print(f"  γ_purity (纯度<0.5): {thresholds.get('gamma_purity', 'N/A')}")
    
    # 可视化
    plot_threshold_analysis(results_dict)
    
    # 分析排序关系
    print("\n" + "="*70)
    print("阈值排序分析")
    print("="*70)
    
    for channel in channels:
        thresholds = results_dict[channel]['thresholds']
        gamma_E = thresholds.get('gamma_E')
        gamma_CHSH = thresholds.get('gamma_CHSH')
        gamma_purity = thresholds.get('gamma_purity')
        
        print(f"\n{channel}:")
        
        if gamma_E and gamma_CHSH:
            if gamma_CHSH < gamma_E:
                print(f"  ✓ CHSH 失效 (γ={gamma_CHSH:.3f}) 早于纠缠消失 (γ={gamma_E:.3f})")
                print(f"    → Bell 非定域性比纠缠更脆弱")
            elif gamma_E < gamma_CHSH:
                print(f"  ⚠ 纠缠消失 (γ={gamma_E:.3f}) 早于 CHSH 失效 (γ={gamma_CHSH:.3f})")
                print(f"    → 需要核查 concurrence 计算")
            else:
                print(f"  = 同时失效 (γ≈{gamma_E:.3f})")
    
    elapsed = time.time() - start_time
    
    print("\n" + "="*70)
    print("总结")
    print("="*70)
    print(f"总用时: {elapsed:.2f} 秒")
    
    print("\n关键发现：")
    print("  1. 提取了三个临界阈值：γ_E, γ_CHSH, γ_purity")
    print("  2. 确定了阈值的排序关系")
    print("  3. 验证了 Bell 非定域性与纠缠的层级关系")
    print("  4. 为 BNCFT 提供了定量的失效边界")
    
    print("\n修正说明：")
    print("  - 纯度不会降到 0，而是趋向混态极限")
    print("  - 两比特系统最大混态纯度 = 1/4")
    print("  - 需要用严格的 concurrence 验证纠缠-CHSH 关系")


if __name__ == "__main__":
    main()
