def rename_cost(old: str, new: str) -> int:
    a, b = old.lower(), new.lower()
    last = {}
    top = len(a) + len(b)
    d = [[0] * (len(b) + 2) for _ in range(len(a) + 2)]
    d[0][0] = top
    for i in range(len(a) + 1):
        d[i + 1][0] = top
        d[i + 1][1] = i
    for j in range(len(b) + 1):
        d[0][j + 1] = top
        d[1][j + 1] = j
    for i in range(1, len(a) + 1):
        col = 0
        for j in range(1, len(b) + 1):
            i1 = last.get(b[j - 1], 0)
            j1 = col
            cost = 1
            if a[i - 1] == b[j - 1]:
                cost = 0
                col = j
            d[i + 1][j + 1] = min(d[i][j] + cost, d[i + 1][j] + 1, d[i][j + 1] + 1,
                                  d[i1][j1] + (i - i1 - 1) + 1 + (j - j1 - 1))
        last[a[i - 1]] = i
    return d[len(a) + 1][len(b) + 1]
