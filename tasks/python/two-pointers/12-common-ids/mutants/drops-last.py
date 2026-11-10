def common_ids(a: list[int], b: list[int]) -> list[int]:
    i = j = 0
    out = []
    while i < len(a) - 1 and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            if not out or out[-1] != a[i]:
                out.append(a[i])
            i += 1
            j += 1
    return out
