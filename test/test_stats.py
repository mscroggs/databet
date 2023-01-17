import json
import numpy as np
import pytest
from tools.stats import mean_x, mean_y, std_x, std_y, correlation

with open("letters/0.json") as f:
    zero = np.array(json.load(f))


@pytest.mark.parametrize("stat, target", [
    (stat, stat(zero)) for stat in [mean_x, mean_y, std_x, std_y, correlation]
])
@pytest.mark.parametrize("letter", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def test_statistic(stat, target, letter):
    with open(f"letters/{letter}.json") as f:
        pts = np.array(json.load(f))
    assert stat(pts) == target
