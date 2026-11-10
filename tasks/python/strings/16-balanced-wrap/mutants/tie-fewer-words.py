def balanced_wrap(text: str, width: int) -> list[str]:
    words = text.split()
    n = len(words)
    cost = [0] * (n + 1)
    nxt = [n] * (n + 1)
    for i in range(n - 1, -1, -1):
        best = None
        length = -1
        for j in range(i, n):
            length += len(words[j]) + 1
            if length > width and j > i:
                break
            if j == n - 1 or length > width:
                line_cost = 0
            else:
                line_cost = (width - length) ** 2
            total = line_cost + cost[j + 1]
            if best is None or total < best:
                best = total
                nxt[i] = j + 1
        cost[i] = best
    lines = []
    i = 0
    while i < n:
        lines.append(" ".join(words[i:nxt[i]]))
        i = nxt[i]
    return lines
