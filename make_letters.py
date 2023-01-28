"""Script to make _letters.py in databet pip package."""

import json

from databet.letters import load_letter_list


def make():
    """Make _letters.py."""
    data = {}
    for letter in "0ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        data[letter] = load_letter_list(letter)

    with open("databet/_letters.py", "w") as f:
        f.write("\"\"\"Letters.\"\"\"\n\n")
        f.write("letters = " + json.dumps(data) + "  # noqa: E501\n")


if __name__ == "__main__":
    make()
