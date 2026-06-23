from pathlib import Path

path = Path(r'f:/BNCFT/claude/files/bncft_paper.tex')
text = path.read_text(encoding='utf-8')
start = text.index('\\section{Emergence of SU(2)}')
end = text.index('\\section{Derivation of Bell Correlations}')
new_text = r"""
\\section{Emergence of SU(2)}
\\label{sec:emergence}

A classical topological soliton has rotational zero modes described by rigid rotations of its internal field configuration. For a unit vector field $\\mathbf{n}(x) \\in S^2$, these rotations act as
\\begin{equation}
\\mathbf{n}(x) = R\\,\\mathbf{n}_0(x), \\qquad R \\in SO(3).
\\end{equation}
To capture the possibility of spinor behavior with $720^\\circ$ periodicity, we lift the rotation group to its double cover,
\\begin{equation}
A(\\tau) \\in SU(2), \\qquad R_{ij}(A) = \\frac{1}{2}\\text{Tr}(\\sigma_i A \\sigma_j A^\\dagger)
\\end{equation}
where $\\sigma_i$ are the Pauli matrices.

\\subsection{Collective Coordinate Lagrangian}

The slow rotational dynamics of the soliton are described by an effective rigid-body Lagrangian:
\\begin{equation}
L = \\frac{\\Lambda}{2} \\text{Tr}(\\dot A \\dot A^\\dagger),
\\end{equation}
with $\\Lambda$ the moment of inertia of the soliton,
\\begin{equation}
\\Lambda = \\int d^3x\\, \\rho_{\\text{rot}}(x),
\\end{equation}
where $\\rho_{\\text{rot}}$ is the rotational part of the energy density. Using the right-invariant body angular velocity,
\\begin{equation}
\\Omega = -i A^\\dagger \\dot A = \\frac{1}{2}\\Omega_i \\sigma_i,
\\end{equation}
one finds
\\begin{equation}
L = \\frac{\\Lambda}{2} \\Omega_i \\Omega_i.
\\end{equation}

\\subsection{Canonical Quantization}

The conjugate angular momenta are
\\begin{equation}
J_i = \\frac{\\partial L}{\\partial \\Omega_i} = \\Lambda \\Omega_i.
\\end{equation}
Quantization promotes $J_i$ to operators satisfying the SU(2) algebra:
\\begin{equation}
[J_i,J_j] = i\\epsilon_{ijk}J_k.
\\end{equation}
The Hamiltonian becomes
\\begin{equation}
H = \\frac{J^2}{2\\Lambda}, \\qquad J^2 = J_i J_i.
\\end{equation}
Its eigenvalues are
\\begin{equation}
J^2 |j,m\\rangle = j(j+1) |j,m\\rangle, \\qquad j = 0, \\tfrac{1}{2}, 1, \\tfrac{3}{2}, \\ldots.
\\end{equation}

\\subsection{Measurement Operators}

A local measurement along direction $\\hat{\\mathbf{n}}$ is represented by
\\begin{equation}
M(\\hat{\\mathbf{n}}) = 2\\,\\hat{\\mathbf{n}}\\cdot\\mathbf{J} = 2(n_x J_x + n_y J_y + n_z J_z).
\\end{equation}
For the spin-$1/2$ representation this gives eigenvalues $\\pm1$. The noncommutativity follows immediately:
\\begin{equation}
[M(\\hat{\\mathbf{a}}), M(\\hat{\\mathbf{b}})] = 2i(\\hat{\\mathbf{a}}\\times\\hat{\\mathbf{b}})\\cdot\\mathbf{J} \\neq 0 \\quad \\text{for } \\hat{\\mathbf{a}}\\not\\parallel\\hat{\\mathbf{b}}.
\\end{equation}
This is the precise origin of the noncommuting measurement structure in BNCFT.

\\subsection{Finkelstein--Rubinstein Constraint}

The Finkelstein--Rubinstein constraint relates the soliton's topological charge $B$ to its rotation phase. Under a $2\\pi$ rotation,
\\begin{equation}
\\Psi \\mapsto (-1)^B \\Psi.
\\end{equation}
Thus
\\begin{itemize}
\\item $B$ even \\Rightarrow integer spin, $360^\\circ$ returns the same state;\\
\\item $B$ odd \\Rightarrow half-integer spin, $360^\\circ$ changes the sign and $720^\\circ$ is required to return to the original state.
\\end{itemize}
For odd-charge solitons, the collective coordinate must be quantized in a half-integer SU(2) representation.
"""

path.write_text(text[:start] + new_text + text[end:], encoding='utf-8')
print('replacement successful')
