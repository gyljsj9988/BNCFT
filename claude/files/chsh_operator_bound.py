import math

# Pauli matrices as nested lists
sigma = [
    [[0, 1], [1, 0]],
    [[0, -1j], [1j, 0]],
    [[1, 0], [0, -1]],
]

singlet = [0, 1 / math.sqrt(2), -1 / math.sqrt(2), 0]


def kron(a, b):
    return [
        [a[i][j] * b[p][q] for j in range(len(a[0])) for q in range(len(b[0]))]
        for i in range(len(a)) for p in range(len(b))
    ]


def mat_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_mul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def mat_vec_mul(m, v):
    return [sum(m[i][j] * v[j] for j in range(len(v))) for i in range(len(m))]


def inner(v, w):
    return sum(complex(v[i]).conjugate() * w[i] for i in range(len(v)))


def measurement_operator(n):
    op = [[0, 0], [0, 0]]
    for i in range(3):
        op = mat_add(op, [[n[i] * sigma[i][r][c] for c in range(2)] for r in range(2)])
    return op


def expectation(op, state):
    psi = mat_vec_mul(op, state)
    return inner(state, psi)


def build_chsh(a, a_p, b, b_p):
    A = measurement_operator(a)
    A_p = measurement_operator(a_p)
    B = measurement_operator(b)
    B_p = measurement_operator(b_p)
    return mat_add(
        mat_sub(
            mat_add(kron(A, B), kron(A, B_p)),
            kron(A_p, B_p)
        ),
        kron(A_p, B)
    )


def norm(v):
    return math.sqrt(sum(abs(x) ** 2 for x in v))


if __name__ == '__main__':
    a = [1.0, 0.0, 0.0]
    a_p = [0.0, 1.0, 0.0]
    b = [1 / math.sqrt(2), 1 / math.sqrt(2), 0.0]
    b_p = [1 / math.sqrt(2), -1 / math.sqrt(2), 0.0]

    B = build_chsh(a, a_p, b, b_p)
    B2 = mat_mul(B, B)
    exp_B2 = expectation(B2, singlet)
    S = expectation(B, singlet)

    print('S =', S)
    print('|S| =', abs(S))
    print('Expectation of B^2 =', exp_B2)
    print('sqrt(E[B^2]) =', math.sqrt(abs(exp_B2)))
    print('Tsirelson bound =', 2 * math.sqrt(2))
