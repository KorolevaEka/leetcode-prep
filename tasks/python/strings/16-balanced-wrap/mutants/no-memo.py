def balanced_wrap(text: str, width: int) -> list[str]:
    words = text.split()

    def go(i):
        if i == len(words):
            return 0, []
        best = None
        for j in range(i + 1, len(words) + 1):
            line = " ".join(words[i:j])
            if len(line) > width and j - i > 1:
                break
            line_cost = 0 if j == len(words) or len(line) > width else (width - len(line)) ** 2
            rest_cost, rest = go(j)
            cand = (line_cost + rest_cost, [line] + rest)
            if best is None or cand[0] < best[0] or (cand[0] == best[0] and False):
                best = cand
        return best

    return go(0)[1]
