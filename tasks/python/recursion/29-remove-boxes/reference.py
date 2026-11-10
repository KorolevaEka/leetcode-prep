from functools import cache

def cleanup_score(colors):

    @cache
    def visit(l, r, k):
        if l > r:
            return 0
        while l < r and colors[r] == colors[r - 1]:
            r -= 1
            k += 1
        best = visit(l, r - 1, 0) + (k + 1) ** 2
        for i in range(l, r):
            if colors[i] == colors[r]:
                best = max(best, visit(l, i, k + 1) + visit(i + 1, r - 1, 0))
        return best
    return visit(0, len(colors) - 1, 0)
