from .substitution import *

def test_caesar_shift():
    # Test shifts on a complete alphabet.
    assert caesar_shift("abcdefghijklmnopqrstuvwxyz", 1) == "bcdefghijklmnopqrstuvwxyza"
    assert caesar_shift("abcdefghijklmnopqrstuvwxyz", 5) == "fghijklmnopqrstuvwxyzabcde"
    assert caesar_shift("abcdefghijklmnopqrstuvwxyz", 25) == "zabcdefghijklmnopqrstuvwxy"
    assert caesar_shift("abcdefghijklmnopqrstuvwxyz", 26) == "abcdefghijklmnopqrstuvwxyz"
    # Negative indicies should work the same way, but in the opposite direction.
    assert caesar_shift("abcdefghijklmnopqrstuvwxyz", -1) == "zabcdefghijklmnopqrstuvwxy"
    assert caesar_shift("abcdefghijklmnopqrstuvwxyz", -5) == "vwxyzabcdefghijklmnopqrstu"
    assert caesar_shift("abcdefghijklmnopqrstuvwxyz", -25) == "bcdefghijklmnopqrstuvwxyza"
    assert caesar_shift("abcdefghijklmnopqrstuvwxyz", -26) == "abcdefghijklmnopqrstuvwxyz"

def test_atbash():
    assert atbash("abcdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedcba"
