def rail_decipher(parts):
    step, indices = -1, [0] * len(parts)
    i, res = 0, ""
    while indices[i] < len(parts[i]):
        res += parts[i][indices[i]]
        indices[i] += 1
        step = step if 0 < i < len(parts) - 1 else -1 * step
        i += step
    return res
