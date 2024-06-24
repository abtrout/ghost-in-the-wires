import random
import string

from .substitution import *

alphabet = string.ascii_lowercase


def test_caesar_shift():
    # Verify right shifts on full alphabet.
    assert caesar_shift(alphabet, 1) == "bcdefghijklmnopqrstuvwxyza"
    assert caesar_shift(alphabet, 5) == "fghijklmnopqrstuvwxyzabcde"
    assert caesar_shift(alphabet, 25) == "zabcdefghijklmnopqrstuvwxy"
    assert caesar_shift(alphabet, 26) == alphabet
    # Negative offsets shift to the left.
    assert caesar_shift(alphabet, -1) == "zabcdefghijklmnopqrstuvwxy"
    assert caesar_shift(alphabet, -5) == "vwxyzabcdefghijklmnopqrstu"
    assert caesar_shift(alphabet, -25) == "bcdefghijklmnopqrstuvwxyza"
    assert caesar_shift(alphabet, -26) == alphabet
    # Example from Wikipedia.
    assert (
        caesar_shift("thequickbrownfoxjumpsoverthelazydog", 23)
        == "qebnrfzhyoltkclugrjmplsboqebixwvald"
    )


def test_atbash():
    assert atbash(alphabet) == alphabet[::-1] 