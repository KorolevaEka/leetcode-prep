def budget_combinations(costs, target):
    a = sorted(costs)
    out = []

    def visit(start, left, path):
        if left == 0:
            out.append(path)
            return
        for i in range(start, len(a)):
            if i > start and a[i] == a[i - 1]:
                continue
            if a[i] > left:
                break
            visit(i, left - a[i], path + [a[i]])
    visit(0, target, [])
    return out
