"""Script to make _letters.py in databet pip package."""

import json


def make():
    """Make _letters.py."""
    data = {}
    for letter in "0ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        with open(f"letters/{letter}.json") as f:
            data[letter] = json.load(f)

    with open("databet/_letters.py", "w") as f:
        f.write("\"\"\"Letters.\"\"\"\n\n")
        f.write("letters = " + json.dumps(data) + "  # noqa: E501\n")


if __name__ == "__main__":
    make()
