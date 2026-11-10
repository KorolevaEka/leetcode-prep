def max_tree_path(tree):
    if tree is None:
        return None
    best = 0

    def visit(node):
        nonlocal best
        if node is None:
            return 0
        value, left, right = node
        a = max(0, visit(left))
        b = max(0, visit(right))
        best = max(best, value + a + b)
        return value + max(a, b)
    visit(tree)
    return best
