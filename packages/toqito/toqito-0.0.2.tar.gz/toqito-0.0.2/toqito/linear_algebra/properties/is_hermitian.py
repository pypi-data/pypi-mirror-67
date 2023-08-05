"""Determines whether or not a matrix is Hermitian."""
import numpy as np


def is_hermitian(mat: np.ndarray) -> bool:
    r"""
    Check if matrix is Hermitian [WIKHRM]_.

    A Hermitian matrix is a complex square matrix that is equal to its own
    conjugate transpose.

    Examples
    ==========

    Consider the following matrix

    .. math::
        A = \begin{pmatrix}
                                2 & 2 +1j & 4 \\
                                2 - 1j & 3 & 1j \\
                                4 & -1j & 1
                           \end{pmatrix}

    our function indicates that this is indeed a Hermitian matrix as it holds that

    .. math::
        A = A^*.

    >>> from toqito.linear_algebra.properties.is_hermitian import is_hermitian
    >>> import numpy as np
    >>> mat = np.array([[2, 2 + 1j, 4], [2 - 1j, 3, 1j], [4, -1j, 1]])
    >>> is_hermitian(mat)
    True

    Alternatively, the following example matrix :math:`B` defined as

    .. math::
        B = \begin{pmatrix}
                                1 & 2 & 3 \\
                                4 & 5 & 6 \\
                                7 & 8 & 9
                             \end{pmatrix}

    is not Hermitian.

    >>> from toqito.linear_algebra.properties.is_hermitian import is_hermitian
    >>> import numpy as np
    >>> mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> is_hermitian(mat)
    False

    References
    ==========
    .. [WIKHRM] Wikipedia: Hermitian matrix.
        https://en.wikipedia.org/wiki/Hermitian_matrix

    :param mat: Matrix to check.
    :return: Return True if matrix is Hermitian, and False otherwise.
    """
    return np.allclose(mat, mat.conj().T)
