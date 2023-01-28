import pytest

from databet.plotting import plot_letter, plot_word


@pytest.mark.parametrize("letter", "ABCabc")
def test_plot_letter(letter):
    plot_letter(letter, f"__test__plot_letter__{letter}.png")


@pytest.mark.parametrize("word", ["Lorem", "Ipsum", "13"])
def test_plot_word(word):
    plot_word(word, f"__test__plot_word__{word}.png")
