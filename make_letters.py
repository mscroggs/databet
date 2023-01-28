import json
from databet.letters import load_letter

data = {}
for letter in "0ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    data[letter] = load_letter(letter, "list")

with open("databet/_letters.py", "w") as f:
    f.write("letters = " + json.dumps(data) + "  # noqa: E501\n")
