"""Computes the trace distance of two matrices."""
import numpy as np
from toqito.states.distance.trace_norm import trace_norm


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    r"""
    Compute the trace distance between density operators `rho` and `sigma`.

    The trace distance between :math:`\rho` and :math:`\sigma` is defined as

    .. math::
        \delta(\rho, \sigma) = \frac{1}{2} \left( \text{Tr}(\left| \rho - \sigma
         \right| \right).

    More information on the trace distance can be found in [WIKTD]_.

    Examples
    ==========

    Consider the following Bell state

    .. math::
        u = \frac{1}{\sqrt{2}} \left( e_0 \otimes e_0 + e_1 \otimes e_1 \right)
        \in \mathcal{X}.

    The corresponding density matrix of :math:`u` may be calculated by:

    .. math::
        \rho = u u^* = \begin{pmatrix}
                         1 & 0 & 0 & 1 \\
                         0 & 0 & 0 & 0 \\
                         0 & 0 & 0 & 0 \\
                         1 & 0 & 0 & 1
                       \end{pmatrix} \text{D}(\mathcal{X}).

    The trace distance between :math:`\rho` and another state :math:`\sigma` is
    equal to :math:`0` if any only if :math:`\rho = \sigma`. We can check this
    using the `toqito` package.

    >>> from toqito.states.states.bell import bell
    >>> from toqito.states.distance.trace_distance import trace_distance
    >>> rho = bell(0) * bell(0).conj().T
    >>> sigma = rho
    >>> trace_distance(rho, sigma)
    0.0

    References
    ==========
    .. [WIKTD] Quantiki: Trace distance
            https://www.quantiki.org/wiki/trace-distance

    :param rho: An input matrix.
    :param sigma: An input matrix.
    :return: The trace distance between `rho` and `sigma`.
    """
    return trace_norm(np.abs(rho - sigma)) / 2
