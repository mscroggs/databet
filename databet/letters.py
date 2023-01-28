import json as _json
import numpy as _np
import os as _os


def _load(letter):
    try:
        from ._letters import letters
        if letter not in letters:
            return _load("0")
        return letters[letter]
    except ImportError:
        letter_file = _os.path.join(_os.path.join(_os.path.join(
            _os.path.dirname(_os.path.realpath(__file__)), ".."
        ), "letters"), f"{letter.upper()}.json")
        if not _os.path.isfile(letter_file):
            return _load("0")
        with open(letter_file) as f:
            return _json.load(f)


def load_letter(letter, format="numpy"):
    data = _load(letter)

    if format == "list":
        return data
    if format == "numpy":
        return _np.array(data)

    raise ValueError(f"Unknown format: {format}")
