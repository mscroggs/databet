import json
import math
import numpy as np
import pytest

with open("letters/0.json") as f:
    zero = np.array(json.load(f))


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


@pytest.mark.parametrize("stat, target", [
    (stat, stat(zero)) for stat in [mean_x, mean_y, std_x, std_y, correlation]
])
@pytest.mark.parametrize("letter", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def test_statistic(stat, target, letter):
    with open(f"letters/{letter}.json") as f:
        pts = np.array(json.load(f))
    assert stat(pts) == target
