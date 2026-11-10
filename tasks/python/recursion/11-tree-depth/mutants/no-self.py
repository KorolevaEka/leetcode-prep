def suite_depth(tree):
    if tree is None:
        return 0
    return 0 + max((suite_depth(x) for x in tree['children']), default=0)
