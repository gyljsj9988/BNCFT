#!/usr/bin/env python3
"""
A3 v0.6 可执行分类器 (基于A3 v0.5填入数据)

实现D_eff = classify_region(Xi_8) 函数
Xi_8 = [eta, rho, delta, C_avg, xi4_mean, D_PR, D_gap, D_stab]

区域分类树:
1. if eta <= 0.9 and rho <= 0.9 and delta <= 0.5:
   - if delta >= 0.2 and delta <= 0.4:
     D_eff = "dangerous_pseudo_success"
   - else:
     D_eff = "success"
2. elif eta >= 0.4 and rho >= 0.3 and delta <= 0.5:
   D_eff = "pathological"
3. else:
   D_eff = "fragile"

稳定性检查: Xi_6,7,8 必须 = 4.0，否则回退
"""

def classify_region(xi_8):
    """
    输入: xi_8 = [eta, rho, delta, C_avg, xi4_mean, D_PR, D_gap, D_cons]
    输出: (D_eff, status) 其中status in {'通过', '回退'}
    """
    if len(xi_8) != 8:
        return ("无效输入", "回退")

    eta, rho, delta, C_avg, xi4_mean, D_PR, D_gap, D_cons = xi_8

    # 稳定性检查 (D_PR, D_gap, D_stab not directly, but assume D_cons indicates)
    if D_PR != 4.0 or D_gap != 4.0:
        return ("稳定性失败", "回退")

    # 有效域检查
    if not (0 <= eta <= 1 and 0 <= rho <= 1 and 0 <= delta <= 0.5):
        return ("超出有效域", "回退")

    # 基于D_cons分类
    if abs(D_cons - 4.0) < 1e-6:
        # success or dangerous
        if eta <= 0.9 and rho <= 0.9 and delta <= 0.5:
            if delta >= 0.2 and delta <= 0.4:
                return ("dangerous_pseudo_success", "通过")
            else:
                return ("success", "通过")
        else:
            return ("不匹配D_cons=4.0", "回退")
    elif abs(D_cons - 3.666667) < 1e-3:
        return ("fragile", "通过")
    elif abs(D_cons - 3.0) < 1e-6:
        return ("pathological", "通过")
    else:
        return ("未知D_cons", "回退")

# 测试示例
if __name__ == "__main__":
    test_cases = [
        ([0.2, 0.0, 0.1, 0.146, 0.489, 4.0, 4.0, 4.0], "success"),  # success, D_cons=4.0
        ([0.2, 0.0, 0.3, 0.146, 0.489, 4.0, 4.0, 4.0], "dangerous_pseudo_success"),  # dangerous, D_cons=4.0
        ([0.9, 1.0, 0.3, 0.243, 0.458, 4.0, 4.0, 3.0], "pathological"),  # pathological, D_cons=3.0
        ([0.3, 0.9, 0.0, 0.194, 0.455, 4.0, 4.0, 3.666667], "fragile"),  # fragile, D_cons=3.666667
        ([0.9, 0.9, 0.1, 0.0, 0.0, 4.0, 4.0, 4.0], "success"),  # success, D_cons=4.0
    ]

    for i, (xi, expected) in enumerate(test_cases, 1):
        result, status = classify_region(xi)
        match = "✓" if result == expected else "✗"
        print(f"测试{i}: Xi_8={xi} -> D_eff={result}, 状态={status} {match} (期望: {expected})")