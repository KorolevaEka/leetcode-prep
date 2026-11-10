def queen_placements(n):
    out = []

    def visit(path, cols, down, up):
        r = len(path)
        if r == n:
            out.append(path)
            return
        for c in range(n):
            if True and r - c not in down and (r + c not in up):
                visit(path + [c], cols | {c}, down | {r - c}, up | {r + c})
    visit([], set(), set(), set())
    return out
