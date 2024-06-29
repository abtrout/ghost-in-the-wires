"""Substitution ciphers."""

import string


def simple_substitute(input_str, sub_alphas):
    """Simple https://en.wikipedia.org/wiki/Substitution_cipher#Simple."""
    assert len(sub_alphas) == len(
        string.ascii_lowercase), "invalid substitution alphabet; incorrect length"
    assert len(set(sub_alphas)) == len(
        string.ascii_lowercase), "invalid substitution alphabet; missing characters"
    return "".join([
        sub_alphas[ord(c) - ord('a')]
        if c.isalpha() else c
        for c in input_str.lower()
    ])


def mixed_alphabet(key, alphas=string.ascii_lowercase):
    """Construct a "mixed" substitution alphabet with the given key."""
    return "".join(list(dict.fromkeys(key + alphas)))


def invert_alphabet(alphas):
    """Invert the given substitution alphabet."""
    assert len(alphas) == len(
        string.ascii_lowercase), "invalid alphabet; incorrect length"
    assert len(set(alphas)) == len(
        string.ascii_lowercase), "invalid alphabet; missing characters"

    res = ["?"] * len(alphas)
    for i, a in enumerate(alphas):
        res[ord(a) - ord('a')] = chr(ord('a') + i)
    return "".join(res)


def caesar_shift(input_str, offset):
    """Caesar https://en.wikipedia.org/wiki/Caesar_cipher."""
    alphas = string.ascii_lowercase
    if offset < 0:
        offset = offset + len(alphas)
    shift = offset % len(alphas)
    return simple_substitute(input_str, alphas[shift:] + alphas[:shift])


def atbash(input_str):
    """Atbash https://en.wikipedia.org/wiki/Atbash."""
    return simple_substitute(input_str, string.ascii_lowercase[::-1])


def playfair_decrypt(key_prefix, input_str):
    """Playfair[1] digram substitution cipher based on the Polybius[2] square.
    [1] https://en.wikipedia.org/wiki/Playfair_cipher
    [2] https://en.wikipedia.org/wiki/Polybius_square
    """
    input_str = input_str.replace(" ", "")
    assert len(input_str) % 2 == 0, "invalid input with odd length"

    alphas = "abcdefghiklmnopqrstuvwxyz"  # Note `j` is skipped.
    key = mixed_alphabet(key_prefix, alphas=alphas)
    res = ''
    for i in range(0, len(input_str), 2):
        x, y = key.find(input_str[i]), key.find(input_str[i+1])
        xrow, xcol, yrow, ycol = int(x/5), x % 5, int(y/5), y % 5
        if xrow == yrow:
            res += key[5*xrow + ((xcol-1) % 5)]
            res += key[5*yrow + ((ycol-1) % 5)]
        elif xcol == ycol:
            res += key[5*((xrow-1) % 5) + xcol]
            res += key[5*((yrow-1) % 5) + ycol]
        else:
            res += key[5*xrow + ycol]
            res += key[5*yrow + xcol]
    return res


def bifid_decrypt(key_prefix, ct):
    """Bifid digram/polybius https://en.wikipedia.org/wiki/Bifid_cipher."""
    alphas = "abcdefghiklmnopqrstuvwxyz"  # Note `j` is skipped.
    key = ''.join(list(dict.fromkeys(key_prefix + alphas)))
    # Find coordinates from ciphertext characters.
    nums = []
    for c in ct:
        if not c.isalpha():
            continue
        i = key.find(c)
        nums.extend((i // 5, i % 5))
    # Invert the row/column swap done during encryption.
    half = len(nums) // 2
    return "".join([
        key[5*row + col]
        for row, col in zip(nums[:half], nums[half:])
    ])


def vignere_decrypt(key, ct):
    """Vignere https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher."""
    res, i = "", 0
    for c in ct:
        if c.isalpha():
            shift = ord(key[i % len(key)]) - ord('a')
            res += chr(ord('a') + ((ord(c) - shift - ord('a')) % 26))
            i += 1  # only advance through `key` for alphas!
        else:
            res += c
    return res


def autokey_decrypt(key, ct):
    """Autokey https://en.wikipedia.org/wiki/Autokey_cipher."""
    res, i = '', 0
    for c in ct:
        if c.isalpha():
            shift = ord(key[i % len(key)]) - ord('a')
            x = chr(ord('a') + ((ord(c) - shift - ord('a')) % 26))
            res += x
            key += x  # append ciphertext to key.
            i += 1
        else:
            res += c
    return res


def telephone_decrypt(ct):
    """Telephone keypad https://en.wikipedia.org/wiki/Telephone_keypad."""
    keypad = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "prs",
        "8": "tuv", "9": "wxy", "0": "q z"
    }
    res = ""
    for i in range(0, len(ct), 2):
        button = keypad[ct[i]]
        match ct[i+1]:
            case "\\":
                res += button[0]
            case "|":
                res += button[1]
            case "/":
                res += button[2]
    return res


def morse_decode(input_str):
    """Morse Code https://en.wikipedia.org/wiki/Morse_code"""
    assert set(input_str).issubset(
        {'.', '-', ' '}), "invalid input; expected dots 'n dashes"

    morse_forward = {
        "a": ".-",    "b": "-...",  "c": "-.-.",
        "d": "-..",   "e": ".",     "f": "..-.",
        "g": "--.",   "h": "....",  "i": "..",
        "j": ".---",  "k": "-.-",   "l": ".-..",
        "m": "--",    "n": "-.",    "o": "---",
        "p": ".--.",  "q": "--.-",  "r": ".-.",
        "s": "...",   "t": "-",     "u": "..-",
        "v": "...-",  "w": ".--",   "x": "-..-",
        "y": "-.--",  "z": "--..",  "1": ".----",
        "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.", "0": "-----",
    }
    morse_reverse = {v: k for k, v in morse_forward.items()}
    return "".join([
        morse_reverse.get(m, "?")
        for m in input_str.split(" ")
    ])


def twisted_morse_decode(input_str):
    """Morse decode but alternate the mapping between 0/1 and -/. with each letter."""
    assert set(input_str).issubset(
        {'0', '1', ' '}), "invalid input; expected binary string"

    return "".join([
        morse_decode(
            c.replace("0", "-" if i % 2 == 0 else ".")
            .replace("1", "." if i % 2 == 0 else "-")
        )
        for i, c in enumerate(input_str.split())
    ])
