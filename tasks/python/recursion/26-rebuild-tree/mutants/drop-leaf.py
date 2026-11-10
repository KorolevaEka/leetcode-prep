def rebuild_tree(preorder, inorder):
    position = {v: i for i, v in enumerate(inorder)}
    cursor = 0

    def build(left, right):
        nonlocal cursor
        if left >= right - 1:
            return None
        root = preorder[cursor]
        cursor += 1
        pivot = position[root]
        a = build(left, pivot)
        b = build(pivot + 1, right)
        return (root, a, b)
    return build(0, len(inorder))
