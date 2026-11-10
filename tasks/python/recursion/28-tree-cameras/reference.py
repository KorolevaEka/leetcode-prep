def tree_cameras(tree):
    count = 0

    def visit(node):
        nonlocal count
        if node is None:
            return 1
        _, left, right = node
        a = visit(left)
        b = visit(right)
        if a == 0 or b == 0:
            count += 1
            return 2
        if a == 2 or b == 2:
            return 1
        return 0
    state = visit(tree)
    return count + (state == 0)
