def mirror_tree(tree):
    if tree is None:
        return None
    value, left, right = tree
    return (value, mirror_tree(right), mirror_tree(left))
