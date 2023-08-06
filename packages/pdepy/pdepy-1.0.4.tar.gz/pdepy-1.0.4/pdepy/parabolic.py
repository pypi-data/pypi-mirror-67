"""
Finite-difference solver for parabolic equation:
    u_y = p*u_xx + q*u_x + r*u + s.

Initial and boundary conditions:
    u(x, 0)  = init(x),     0 <= x <= xf,
    u(0, y)  = bound_x0(y), 0 <= y <= yf,
    u(xf, y) = bound_xf(y), 0 <= y <= yf.
"""

import numpy as np
from scipy import linalg

from pdepy import time, utils


@utils.validate_method(valid_methods=["ec", "eu", "ic", "iu"])
def solve(axis, params, conds, method="iu"):
    """
    Methods
    -------
        * ec: explicit central
        * eu: explicit upwind
        * ic: implicit central
        * iu: implicit upwind

    Parameters
    ----------
    axis : array_like
        Axis 'x' and 'y'; [x, y], each element should be an array_like.
    params : array_like
        The parameters of the equation; [p, q, r, s], each element should
        be a scalar.
    conds : array_like
        Initial and boundary conditions; [init, bound_x0, bound_xf], each
        element should be a scalar or an array_like of size 'x.size' for
        'init' and 'y.size' for 'bound_x'.
    method : string | optional
        Finite-difference method.

    Returns
    -------
    u : ndarray
        A 2-D ndarray; u[x, y].
    """
    u = time.set_u(*axis, *conds)
    consts = _cal_constants(*axis)

    𝛉 = _set_𝛉(method)

    if method[0] == "e":
        _explicit(u, 𝛉, *consts, *params)
    elif method[0] == "i":
        _implicit(u, 𝛉, *consts, *params)

    return u


def _explicit(u, 𝛉, 𝛂, β, k, p, q, r, s):
    """Métodos de diferenças finitas explícitos."""
    for j in np.arange(u.shape[1] - 1):
        u[1:-1, j + 1] = (
            (𝛂 * p + β * (𝛉 * np.abs(q) - q)) * u[:-2, j]
            + (𝛂 * p + β * (𝛉 * np.abs(q) + q)) * u[2:, j]
            + (1 + k * r - 2 * (𝛂 * p + 𝛉 * β * np.abs(q))) * u[1:-1, j]
            + k * s
        )


def _implicit(u, 𝛉, 𝛂, β, k, p, q, r, s):
    """Métodos de diferenças finitas implícitos."""
    aux0 = 𝛂 * p + β * (𝛉 * np.abs(q) + q)
    aux1 = 𝛂 * p + β * (𝛉 * np.abs(q) - q)
    aux2 = -1 + k * r - 2 * (𝛂 * p + 𝛉 * β * np.abs(q))

    mat = _set_mat(𝛉, 𝛂, β, k, p, q, r, np.shape(u)[0] - 2, (aux0, aux1, aux2))

    for j in np.arange(u.shape[1] - 1):
        vec = _set_vec(𝛉, 𝛂, β, k, p, q, s, u[:, j : j + 2], (aux0, aux1))

        u[1:-1, j + 1] = linalg.solve(mat, vec)


def _set_mat(𝛉, 𝛂, β, k, p, q, r, n, aux):
    """Monta a matriz do sistema em cada iteração de '_implicit()'."""
    main = np.full(n, aux[2])
    upper = np.full(n - 1, aux[0])
    lower = np.full(n - 1, aux[1])

    return np.diag(main) + np.diag(upper, 1) + np.diag(lower, -1)


def _set_vec(𝛉, 𝛂, β, k, p, q, s, u, aux):
    """Monta o vetor do sistema em cada iteração de '_implicit()'."""
    vec = -u[1:-1, 0] - k * s

    vec[0] -= aux[1] * u[0, 1]
    vec[-1] -= aux[0] * u[-1, 1]

    return vec


def _cal_constants(x, y):
    """Calcula as constantes '𝛂', 'β' e 'k'."""
    h = x[-1] / (x.size - 1)
    k = y[-1] / (y.size - 1)

    𝛂 = k / h ** 2
    β = k / (2 * h)

    return (𝛂, β, k)


def _set_𝛉(method):
    """Retorna o valor de '𝛉' conforme 'method'."""
    if method[1] == "c":
        return 0
    elif method[1] == "u":
        return 1
