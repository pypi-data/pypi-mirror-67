"""Computes the von Neumann entropy of a density matrix."""
import numpy as np
from numpy import linalg as lin_alg


def von_neumann_entropy(rho: np.ndarray) -> float:
    r"""
    Compute the von Neumann entropy of a density matrix [WikVent]_.

    Let :math:`P \in \text{Pos}(\mathcal{X})` be a positive semidefinite
    operator, for a complex Euclidean space :math:`\mathcal{\X}`. Then one
    defines the *von Neumann entropy* as

    .. math::
        H(P) = H(\lambda(P)),

    where :math:`\lambda(P)` is the vector of eigenvalues of :math:`P` and where
    the function `H(\dot)` is the Shannon entropy function defined as

    .. math::
        H(u) = - \sum_{\substack{a \in \Sigma \\ u(a) > 0}} u(a) \text{log}(u(a)).

    where the :math:`\text{log}` function is assumed to be the base-2 logarithm,
    and where :math:`\Sigma` is an alphabet where :math:`u \in [0, \infty`)^{\Sigma}
    is a vector of nonnegative real numbers indexed by :math:`\Sigma`.

    Examples
    ==========

    Consider the following Bell state

    .. math::
        u = \frac{1}{\sqrt{2}} \left(e_0 \otimes e_0 + e_1 \otimes e_1 \right)
        \in \mathcal{X}.

    The corresponding density matrix of $u$ may be calculated by:

    .. math::
        \rho = u u^* = \frac{1}{2} \begin{pmatrix}
                         1 & 0 & 0 & 1 \\
                         0 & 0 & 0 & 0 \\
                         0 & 0 & 0 & 0 \\
                         1 & 0 & 0 & 1
                       \end{pmatrix} \text{D}(\mathcal{X}).

    Calculating the von Neumann entropy of :math:`\rho` in `toqito` can be done
    as follows.

    >>> from toqito.states.distance.von_neumann_entropy import von_neumann_entropy
    >>> import numpy as np
    >>> test_input_mat = np.array(
    >>>     [[1 / 2, 0, 0, 1 / 2], [0, 0, 0, 0], [0, 0, 0, 0], [1 / 2, 0, 0, 1 / 2]]
    >>> )
    >>> von_neumann_entropy(test_input_mat)
    5.88418203051333e-15

    Consider the density operator corresponding to the maximally mixed state of
    dimension two

    .. math::
        \rho = \frac{1}{2}
        \begin{pmatrix}
            1 & 0 \\
            0 & 1
        \end{pmatrix}.

    As this state is maximally mixed, the von Neumann entropy of :math:`\rho` is
    equal to one. We can see this in `toqito` as follows.

    >>> from toqito.states.distance.von_neumann_entropy import von_neumann_entropy
    >>> import numpy as np
    >>> rho = 1/2 * np.identity(2)
    >>> von_neumann_entropy(rho)
    1.0

    References
    ==========
    .. [WikVent] Wikipedia: Von Neumann entropy
        https://en.wikipedia.org/wiki/Von_Neumann_entropy

    .. [WATVEC] Watrous, John.
        "The theory of quantum information."
        Section: "Definitions of quantum entropic functions".
        Cambridge University Press, 2018.

    :param rho: A density matrix.
    :return: The von Neumann entropy of `rho`.
    """
    eigs, _ = lin_alg.eig(rho)
    eigs = [eig for eig in eigs if eig > 0]
    return -np.sum(np.real(eigs * np.log2(eigs)))
