def effective_settings(tree, inherited):
    if tree is None:
        return []
    current = {**tree['settings'], **inherited}
    out = [(tree['name'], current)]
    for child in tree['children']:
        out += effective_settings(child, current)
    return out
