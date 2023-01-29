import os

import pytest

with open(os.path.join(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), ".."), "README.md"
)) as f:
    readme = f.read()

snippets = [s.split("```")[0] for s in readme.split("```python")[1:]]


@pytest.mark.parametrize("s", snippets)
def test_snippet(s):
    exec(s)
