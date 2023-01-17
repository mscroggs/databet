import math
import numpy as np


def two_dp(value):
    """Round a value to 2 decimal places."""
    return int(math.floor(value * 100 + 0.5))


def mean_x(data):
    """Compute the mean of the first component to 2 decimal places."""
    return two_dp(np.mean(data[:, 0]))


def mean_y(data):
    """Compute the mean of the second component to 2 decimal places."""
    return two_dp(np.mean(data[:, 1]))


def std_x(data):
    """Compute the standard deviation of the first component to 2 decimal places."""
    return two_dp(np.std(data[:, 0]))


def std_y(data):
    """Compute the standard deviation of the second component to 2 decimal places."""
    return two_dp(np.std(data[:, 1]))


def correlation(data):
    """Compute the correlation coefficient to 2 decimal places."""
    return two_dp(np.corrcoef(data[:, 0], data[:, 1])[0, 1])
