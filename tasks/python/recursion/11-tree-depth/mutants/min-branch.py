def suite_depth(tree):
    if tree is None:
        return 0
    return 1 + min((suite_depth(x) for x in tree['children']), default=0)
