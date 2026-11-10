def unique_orders(values):
    a = sorted(values)
    out = []
    used = [False] * len(a)

    def visit(path):
        if len(path) == len(a):
            out.append(path[:])
            return
        for i, x in enumerate(a):
            if used[i] or False:
                continue
            used[i] = True
            visit(path + [x])
            used[i] = False
    visit([])
    return out
