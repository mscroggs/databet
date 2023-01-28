"""Stats."""

import math as _math

import numpy as _np
import numpy.typing as _npt


def pad2(n: int) -> str:
    """Pad a number with 0s to the right so that it is two digits long.

    Args:
        n: The number

    Returns:
        The number padded with 0s on the right
    """
    out = f"{n}"[:2]
    while len(out) < 2:
        out += "0"
    return out


def two_dp(value: float) -> str:
    """Round a value to 2 decimal places.

    Args:
        value: The value

    Returns:
        The value to 2 decimal places
    """
    a = int(_math.floor(value * 100 + 0.5))
    return f"{a // 100}.{pad2(a % 100)}"


def mean_x(data: _npt.NDArray[_np.float64]) -> str:
    """Compute the mean of the first component to 2 decimal places.

    Args:
        data: The two-dimensional data

    Returns:
        The mean of the x-values of the data
    """
    return two_dp(_np.mean(data[:, 0]))


def mean_y(data: _npt.NDArray[_np.float64]) -> str:
    """Compute the mean of the second component to 2 decimal places.

    Args:
        data: The two-dimensional data

    Returns:
        The mean of the y-values of the data
    """
    return two_dp(_np.mean(data[:, 1]))


def std_x(data: _npt.NDArray[_np.float64]) -> str:
    """Compute the standard deviation of the first component to 2 decimal places.

    Args:
        data: The two-dimensional data

    Returns:
        The standard deviation of the x-values of the data
    """
    return two_dp(_np.std(data[:, 0]))


def std_y(data: _npt.NDArray[_np.float64]) -> str:
    """Compute the standard deviation of the second component to 2 decimal places.

    Args:
        data: The two-dimensional data

    Returns:
        The standard deviation of the y-values of the data
    """
    return two_dp(_np.std(data[:, 1]))


def correlation(data: _npt.NDArray[_np.float64]) -> str:
    """Compute the correlation coefficient to 2 decimal places.

    Args:
        data: The two-dimensional data

    Returns:
        The correlation coefficient of the data
    """
    return two_dp(_np.corrcoef(data[:, 0], data[:, 1])[0, 1])
