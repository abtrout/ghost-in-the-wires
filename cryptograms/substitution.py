import string

# Substitute input characters according to sub_alphas.
# https://en.wikipedia.org/wiki/Substitution_cipher#Simple
def simple_substitute(input, sub_alphas):
    # NB: sub_alphas maps original to a substitute positionally. 
    assert len(sub_alphas) == len(string.ascii_lowercase), "invalid alphabet; incorrect length"
    assert len(set(sub_alphas)) == len(string.ascii_lowercase), "invalid alphabet; missing characters"
    # Replace input characters as determined by given sub_alphas.
    return "".join([
        sub_alphas[ord(c) - ord('a')]
        if c.isalpha() else c
        for c in input.lower()
    ])


# Substitute with a (right or left) shifted alphabet.
# https://en.wikipedia.org/wiki/Caesar_cipher
def caesar_shift(input, offset):
    alphas = string.ascii_lowercase
    if offset < 0:
        offset = offset + len(alphas)
    shift = offset % len(alphas)
    return simple_substitute(input, alphas[shift:] + alphas[:shift])


# Substitute with the alphabet reversed.
# https://en.wikipedia.org/wiki/Atbash
def atbash(input):
    return simple_substitute(input, string.ascii_lowercase[::-1])


# Playfair digram substitution cipher.
# https://en.wikipedia.org/wiki/Playfair_cipher
def playfair_decrypt(key_prefix, input):
    input = input.replace(" ", "")
    assert len(input) % 2 == 0, "invalid input with odd length"

    alphas = "abcdefghiklmnopqrstuvwxyz"  # Note `j` is skipped.
    key = mixed_alphabet(key_prefix, alphas=alphas) 
    res = ''
    for i in range(0, len(input), 2):
        x, y = key.find(input[i]), key.find(input[i+1])
        xrow, xcol, yrow, ycol = int(x/5), x%5, int(y/5), y%5
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

# Bifid 
# https://en.wikipedia.org/wiki/Bifid_cipher
def bifid_decrypt(key_prefix, ct):
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
    coords = zip(nums[:len(nums)//2], nums[len(nums)//2:])
    return "".join([key[5*row + col] for row, col in coords])

# Telephone keypad substitution cipher.
# https://en.wikipedia.org/wiki/Telephone_keypad#
def telephone_decrypt(ct):
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


# Vignere substitution cipher.
# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
def vignere_decrypt(key, ct):
    res, i = "", 0
    for c in ct:
        if c.isalpha():
            shift = ord(key[i % len(key)]) - ord('a')
            res += chr(ord('a') + ((ord(c) - shift - ord('a')) % 26))
            i += 1  # only advance through `key` for alphas!
        else:
            res += c
    return res

# Autokey substitution cipher.
# https://en.wikipedia.org/wiki/Autokey_cipher
def autokey_decrypt(key, ct):
    res, i = '', 0
    for c in ct:
        if c.isalpha():
            shift = ord(key[i % len(key)]) - ord('a')
            x = chr(ord('a') + ((ord(c) - shift - ord('a')) % 26))
            res += x
            key += x
            i += 1
        else:
            res += c
    return res


# Morse code as a substitution cipher.
# https://en.wikipedia.org/wiki/Morse_code
def morse_decode(input):
    assert set(input).issubset({'.', '-', ' '}), "invalid input; expected dots 'n dashes"

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
        for m in input.split(" ")
    ])

# Morse decode a binary string by alternating the mapping of 0/1 to -/. 
# for each character. This is used in several challenges.
def twisted_morse_decode(input):
    assert set(input).issubset({'0', '1', ' '}), "invalid input; expected binary string"

    return "".join([
        morse_decode(
            c.replace("0", "-" if i % 2 == 0 else ".")
                .replace("1", "." if i % 2 == 0 else "-")
        )
        for i, c in enumerate(input.split())
    ])


# Constructs a "mixed alphabet" with the given key.
def mixed_alphabet(key, alphas=string.ascii_lowercase):
    return "".join(list(dict.fromkeys(key + alphas)))


# Invert mapping between alphabets.
def invert_alphabet(alphas):
    assert len(alphas) == len(string.ascii_lowercase), "invalid alphabet; incorrect length"
    assert len(set(alphas)) == len(string.ascii_lowercase), "invalid alphabet; missing characters"

    res = ["?"] * len(alphas)
    for i, a in enumerate(alphas):
        res[ord(a) - ord('a')] = chr(ord('a') + i)
    return "".join(res)
