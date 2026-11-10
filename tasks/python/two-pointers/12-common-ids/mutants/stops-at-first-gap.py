def common_ids(a: list[int], b: list[int]) -> list[int]:
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            break
        if not out or out[-1] != a[i]:
            out.append(a[i])
        i += 1
        j += 1
    return out
