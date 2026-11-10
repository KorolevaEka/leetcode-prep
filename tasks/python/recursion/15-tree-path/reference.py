def find_suite_path(tree, target):
    if tree is None:
        return None
    if tree['name'] == target:
        return [target]
    for child in tree['children']:
        path = find_suite_path(child, target)
        if path is not None:
            return [tree['name']] + path
    return None
