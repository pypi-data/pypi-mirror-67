"""Computes the Schmidt decomposition of a bipartite vector."""
from typing import List, Tuple, Union
from scipy.sparse import issparse, linalg

import numpy as np


def schmidt_decomposition(
    vec: np.ndarray, dim: Union[int, List[int], np.ndarray] = None, k_param: int = 0
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    r"""
    Compute the Schmidt decomposition of a bipartite vector [WIKSCD]_.

    Examples
    ==========

    Consider the :math:`3`-dimensional maximally entangled state

    .. math::
        u = \frac{1}{\sqrt{3}} \left( |000> + |111> + |222> \right)

    We can generate this state using the `toqito` module as follows.

    >>> from toqito.states.states.max_entangled import max_entangled
    >>> max_entangled(3)
    array([[0.57735027],
           [0.        ],
           [0.        ],
           [0.        ],
           [0.57735027],
           [0.        ],
           [0.        ],
           [0.        ],
           [0.57735027]])

    Computing the Schmidt decomposition of :math:`u`, we can obtain the
    corresponding singular values of :math:`u` as

    .. math::
        \frac{1}{\sqrt{3}} \left[1, 1, 1 \right]^{\text{T}}

    >>> from toqito.states.operations.schmidt_decomposition import schmidt_decomposition
    >>> singular_vals, u_mat, vt_mat = schmidt_decomposition(max_entangled(3))
    >>> print(singular_vals)
    [[0.57735027]
     [0.57735027]
     [0.57735027]]
    >>> print(u_mat)
    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    >>> print(vt_mat)
    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]

    References
    ==========
    .. [WIKSCD] Wikipedia: Schmidt decomposition
        https://en.wikipedia.org/wiki/Schmidt_decomposition

    :param vec:
    :param dim:
    :param k_param:
    :return: The Schmidt decomposition of the `vec` input.
    """
    eps = np.finfo(float).eps

    if dim is None:
        dim = np.round(np.sqrt(len(vec)))
    if dim is list:
        dim = np.array(dim)

    # Allow the user to enter a single number for `dim`.
    if isinstance(dim, float):
        dim = np.array([dim, len(vec) / dim])
        if np.abs(dim[1] - np.round(dim[1])) >= 2 * len(vec) * eps:
            raise ValueError(
                "InvalidDim: The value of `dim` must evenly divide"
                " `len(vec)`; please provide a `dim` array "
                "containing the dimensions of the subsystems."
            )
        dim[1] = np.round(dim[1])

    # Try to guess whether SVD or SVDS will be faster, and then perform the
    # appropriate singular value decomposition.
    adj = 20 + 1000 * (not issparse(vec))

    # Just a few Schmidt coefficients.
    if 0 < k_param <= np.ceil(np.min(dim) / adj):
        u_mat, singular_vals, vt_mat = linalg.svds(
            linalg.LinearOperator(np.reshape(vec, dim[::-1].astype(int)), k_param)
        )
    # Otherwise, use lots of Schmidt coefficients.
    else:
        u_mat, singular_vals, vt_mat = np.linalg.svd(
            np.reshape(vec, dim[::-1].astype(int))
        )

    if k_param > 0:
        u_mat = u_mat[:, :k_param]
        singular_vals = singular_vals[:k_param]
        vt_mat = vt_mat[:, :k_param]

    # singular_vals = np.diag(singular_vals)
    singular_vals = singular_vals.reshape(-1, 1)
    if k_param == 0:
        # Schmidt rank.
        r_param = np.sum(singular_vals > np.max(dim) * np.spacing(singular_vals[0]))
        # Schmidt coefficients.
        singular_vals = singular_vals[:r_param]
        u_mat = u_mat[:, :r_param]
        vt_mat = vt_mat[:, :r_param]

    u_mat = u_mat.conj().T
    return singular_vals, u_mat, vt_mat
