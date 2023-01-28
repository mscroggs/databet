import math as _math
import numpy as _np


def pad2(n):
    """Pad a number with 0s to the right so that it is two digits long."""
    out = f"{n}"[:2]
    while len(out) < 2:
        out += "0"
    return out


def two_dp(value):
    """Round a value to 2 decimal places."""
    a = int(_math.floor(value * 100 + 0.5))
    return f"{a // 100}.{pad2(a % 100)}"


def mean_x(data):
    """Compute the mean of the first component to 2 decimal places."""
    return two_dp(_np.mean(data[:, 0]))


def mean_y(data):
    """Compute the mean of the second component to 2 decimal places."""
    return two_dp(_np.mean(data[:, 1]))


def std_x(data):
    """Compute the standard deviation of the first component to 2 decimal places."""
    return two_dp(_np.std(data[:, 0]))


def std_y(data):
    """Compute the standard deviation of the second component to 2 decimal places."""
    return two_dp(_np.std(data[:, 1]))


def correlation(data):
    """Compute the correlation coefficient to 2 decimal places."""
    return two_dp(_np.corrcoef(data[:, 0], data[:, 1])[0, 1])
