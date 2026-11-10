def effective_settings(tree, inherited):
    if tree is None:
        return []
    current = {**inherited, **tree['settings']}
    out = [(tree['name'], current)]
    for child in tree['children']:
        out += effective_settings(child, inherited)
    return out
