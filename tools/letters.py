import os
import json
import numpy as np

letter_dir = os.path.join(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        ".."),
    "letters")


def load_letter(letter):
    with open(os.path.join(letter_dir, f"{letter}.json")) as f:
        return np.array(json.load(f))
