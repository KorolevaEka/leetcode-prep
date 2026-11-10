from functools import cache

def expression_results(expression):

    @cache
    def solve(text):
        out = []
        for i, ch in enumerate(text):
            if ch in '+-*':
                for a in solve(text[:i]):
                    for b in solve(text[i + 1:]):
                        out.append(a + b if ch == '+' else b - a if ch == '-' else a * b)
        return tuple(out) if out else (int(text),)
    return sorted(solve(expression))
