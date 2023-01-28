import json as _json
import numpy as _np
import os as _os

letter_dir = _os.path.join(
    _os.path.join(_os.path.dirname(_os.path.realpath(__file__)), ".."),
    "letters")


def load_letter(letter, format="numpy"):
    letter_file = _os.path.join(letter_dir, f"{letter.upper()}.json")
    if not _os.path.isfile(letter_file):
        letter_file = _os.path.join(letter_dir, "0.json")

    with open(letter_file) as f:
        data = _json.load(f)

    if format == "list":
        return data
    if format == "numpy":
        return _np.array(data)

    raise ValueError(f"Unknown format: {format}")
