"""Check if list of vectors constitute a mutually unbiased basis."""
from typing import Any, List, Union
import numpy as np


def is_mub(vec_list: List[Union[np.ndarray, List[Union[float, Any]]]]) -> bool:
    r"""
    Check if list of vectors constitute a mutually unbiased basis [WIKMUB]_.

    We say that two orthonormal bases

    .. math::
        \begin{equation}
            \mathcal{B}_0 = \left{u_a: a \in \Sigma \right} \subset
            \mathbb{C}^{\Sigma}
            \qquad \text{and} \\quad
            \mathca{B}_1 = \left{v_a: a \in \Sigma \right} \subset
            \mathbb{C}^{\Sigma}
        \end{equation}

    are mutually unbiased if and only if :math:`\abs{\langle u_a, v_b \rangle} =
    1/\sqrt{\Sigma}` for all :math:`a, b \in \Sigma`.

    For :math:`n \in \mathbb{N}`, a set of orthonormal bases :math:`\left{
    \mathcal{B}_0, \ldots, \mathcal{B}_{n-1} \right}` are mutually unbiased
    bases if and only if every basis is mutually unbiased with every other
    basis in the set, i.e. :math:`\mathcal{B}_x` is mutually unbiased with
    :math:`\mathcal{B}_x^{\prime}` for all :math:`x \not= x^{\prime}` with
    :math:`x, x^{\prime} \in \Sigma`.

    Examples
    ==========

    MUB of dimension 2.

    For :math:`d=2`, the following constitutes a mutually unbiased basis:

    .. math::
        \begin{equation}
            M_0 = \left{ |0 \rangle, |1 \rangle \right}, \\
            M_1 = \left{ \frac{|0 \rangle + |1 \rangle}{\sqrt{2}},
            \frac{|0 \rangle - |1 \rangle}{\sqrt{2}} \right}, \\
            M_2 = \left{ \frac{|0 \rangle i|1 \rangle}{\sqrt{2}},
            \frac{|0 \rangle - i|1 \rangle}{\sqrt{2}} \right}, \\
        \end{equation}

    >>> import numpy as np
    >>> from toqito.core.ket import ket
    >>> from toqito.states.properties.is_mub import is_mub
    >>> e_0, e_1 = ket(2, 0), ket(2, 1)
    >>> mub_1 = [e_0, e_1]
    >>> mub_2 = [1 / np.sqrt(2) * (e_0 + e_1), 1 / np.sqrt(2) * (e_0 - e_1)]
    >>> mub_3 = [1 / np.sqrt(2) * (e_0 + 1j * e_1), 1 / np.sqrt(2) * (e_0 - 1j * e_1)]
    >>> mubs = [mub_1, mub_2, mub_3]
    >>> is_mub(mubs)
    True

    Non non-MUB of dimension 2.

    >>> import numpy as np
    >>> from toqito.core.ket import ket
    >>> from toqito.states.properties.is_mub import is_mub
    >>> e_0, e_1 = ket(2, 0), ket(2, 1)
    >>> mub_1 = [e_0, e_1]
    >>> mub_2 = [1 / np.sqrt(2) * (e_0 + e_1), e_1]
    >>> mub_3 = [1 / np.sqrt(2) * (e_0 + 1j * e_1), e_0]
    >>> mubs = [mub_1, mub_2, mub_3]
    >>> is_mub(mubs)
    False

    References
    ==========
    .. [WIKMUB] Wikipedia: Mutually unbiased bases
        https://en.wikipedia.org/wiki/Mutually_unbiased_bases

    :param vec_list: The list of vectors to check.
    :return: True if `vec_list` constitutes a mutually unbiased basis, and
             False otherwise.
    """
    if len(vec_list) <= 1:
        raise ValueError("There must be at least two bases provided as input.")

    dim = vec_list[0][0].shape[0]
    for i, _ in enumerate(vec_list):
        for j, _ in enumerate(vec_list):
            for k in range(dim):
                if i != j:
                    if not np.isclose(
                        np.abs(
                            np.inner(
                                vec_list[i][k].conj().T[0], vec_list[j][k].conj().T[0]
                            )
                        )
                        ** 2,
                        1 / dim,
                    ):
                        return False
    return True
