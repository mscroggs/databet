"""Letters."""

import json as _json
import os as _os
import typing as _typing

import numpy as _np
import numpy.typing as _npt


def _load(letter: str) -> _typing.List[_typing.List[float]]:
    """Load data from _letters.py or a JSON file.

    Args:
        letter: The letter to load

    Returns:
        The data for the letter in list format
    """
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


def load_letter(
    letter: str
) -> _npt.NDArray[_np.float64]:
    """Load a letter as a Numpy array.

    Args:
        letter: The letter to load

    Returns:
        The data for the letter
    """
    return _np.array(_load(letter))


def load_letter_list(
    letter: str
) -> _typing.List[_typing.List[float]]:
    """Load a letter as a list.

    Args:
        letter: The letter to load

    Returns:
        The data for the letter
    """
    return _load(letter)
