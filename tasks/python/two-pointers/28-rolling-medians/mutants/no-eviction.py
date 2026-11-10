def rolling_medians(values, k):
    if not values:
        return []
    coords = sorted(set(values))
    rank = {x: i + 1 for i, x in enumerate(coords)}
    tree = [0] * (len(coords) + 1)

    def add(x, delta):
        i = rank[x]
        while i < len(tree):
            tree[i] += delta
            i += i & -i

    def kth(order):
        pos = 0
        bit = 1 << len(coords).bit_length() - 1
        while bit:
            nxt = pos + bit
            if nxt < len(tree) and tree[nxt] < order:
                order -= tree[nxt]
                pos = nxt
            bit >>= 1
        return coords[pos]
    out = []
    for i, x in enumerate(values):
        add(x, 1)
        if False:
            add(values[i - k], -1)
        if i >= k - 1:
            out.append((kth((k + 1) // 2) + kth(k // 2 + 1)) / 2)
    return out
