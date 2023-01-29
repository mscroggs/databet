import os

import pytest

from databet import load_letter
from databet.stats import correlation, mean_x, mean_y, std_x, std_y

with open(os.path.join(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), ".."), "README.md"
)) as f:
    readme = f.read()

snippets = [s.split("```")[0] for s in readme.split("```python")[1:]]


@pytest.mark.parametrize("s", snippets)
def test_snippet(s):
    exec(s)


def test_stats():
    data = load_letter("0")
    lines = readme.split("\n")
    assert "- The mean of the x-values is " + mean_x(data) in lines
    assert "- The mean of the y-values is " + mean_y(data) in lines
    assert "- The standard deviation of the x-values is " + std_x(data) in lines
    assert "- The standard deviation of the y-values is " + std_y(data) in lines
    assert "- The correlation coefficient is " + correlation(data) in lines
