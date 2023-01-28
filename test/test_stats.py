import pytest

from databet.letters import load_letter
from databet.stats import correlation, mean_x, mean_y, std_x, std_y

zero = load_letter("0")


@pytest.mark.parametrize("stat, target", [
    (stat, stat(zero)) for stat in [mean_x, mean_y, std_x, std_y, correlation]
])
@pytest.mark.parametrize("letter", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def test_statistic(stat, target, letter):
    pts = load_letter(letter)
    assert stat(pts) == target
