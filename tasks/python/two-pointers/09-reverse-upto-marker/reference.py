def reverse_upto(items: list, stop) -> list:
    out = list(items)
    if stop not in out:
        return out
    i, j = 0, out.index(stop)
    while i < j:
        out[i], out[j] = out[j], out[i]
        i += 1
        j -= 1
    return out
