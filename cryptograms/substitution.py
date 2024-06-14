# Substitute input characters based on a new alphabet.
# The given sub_alphas should be a 26 character string
# specifying the mapping from original alphabet ("a...z").
def substitute(input, sub_alphas):
    return "".join([
        sub_alphas[ord(c) - ord('a')] if c.isalpha() else c
        for c in input.lower()
    ])


def caesar_shift(input, offset):
    alphas = "abcdefghijklmnopqrstuvwxyz"
    # Build dictionary by shifting the alphabet `offset` positions.
    if offset < 0:
        offset = offset + len(alphas)
    shift = offset % len(alphas)
    sub_alphas = alphas[shift:] + alphas[:shift]
    # Substitute!
    print(f"Shifting {shift} with alphabet {sub_alphas}")
    return substitute(input, sub_alphas)


def atbash(input):
    alphas = "abcdefghijklmnopqrstuvwxyz"
    return substitute(input, alphas[::-1])
