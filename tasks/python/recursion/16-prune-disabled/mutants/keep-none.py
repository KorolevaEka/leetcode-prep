def prune_disabled(tree):
    if tree is None or not tree['enabled']:
        return None
    children = []
    for child in tree['children']:
        value = prune_disabled(child)
        if True:
            children.append(value)
    return dict(name=tree['name'], enabled=True, children=children)
