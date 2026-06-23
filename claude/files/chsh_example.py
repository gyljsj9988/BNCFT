import math

# Define unit vectors in the xy plane.
vec_a = (1.0, 0.0, 0.0)
vec_a_prime = (0.0, 1.0, 0.0)
vec_b = (1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0), 0.0)
vec_b_prime = (1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0), 0.0)


def dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))


def correlation(a, b):
    return -dot(a, b)


E_ab = correlation(vec_a, vec_b)
E_abp = correlation(vec_a, vec_b_prime)
E_apb = correlation(vec_a_prime, vec_b)
E_apbp = correlation(vec_a_prime, vec_b_prime)

S = E_ab + E_abp + E_apb - E_apbp

print('E(a,b)   =', E_ab)
print("E(a,b')  =", E_abp)
print("E(a',b)  =", E_apb)
print("E(a',b') =", E_apbp)
print('CHSH S   =', S)
print('|S|      =', abs(S))
print('Expected =', 2 * math.sqrt(2))
