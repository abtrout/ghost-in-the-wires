"""Transposition ciphers."""


def rail_decipher(rails):
    """Rail Fence https://en.wikipedia.org/wiki/Transposition_cipher#Rail_Fence_cipher."""
    step, indices = -1, [0] * len(rails)
    i, res = 0, ""
    while indices[i] < len(rails[i]):
        res += rails[i][indices[i]]
        indices[i] += 1
        step = step if 0 < i < len(rails) - 1 else -1 * step
        i += step
    return res


def columnar(rows, d_row=1, d_col=1):
    """Columnar https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition."""
    assert len(set(map(len, rows))) == 1, "invalid input; number of columns"
    assert {d_row, d_col}.issubset(
        {1, -1}), "invalid direction(s); choose +1 or -1"

    num_cols = len(rows[0])
    return "".join([
        row[col]
        for col in range(0, num_cols)[::d_col]
        for row in rows[::d_row]
    ])


def every_nth(input_str, n):
    """Read every nth character."""
    assert 0 < n < len(input_str), "invalid n; expect positive and less than input length"
    return "".join([
        input_str[(((n*i) + (i // len(input_str))) % len(input_str))]
        for i in range(len(input_str))
    ])
