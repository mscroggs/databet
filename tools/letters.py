import json
import numpy as np
import os

letter_dir = os.path.join(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        ".."),
    "letters")


def load_letter(letter):
    letter_file = os.path.join(letter_dir, f"{letter.upper()}.json")
    if not os.path.isfile(letter_file):
        letter_file = os.path.join(letter_dir, "0.json")

    with open(letter_file) as f:
        return np.array(json.load(f))
