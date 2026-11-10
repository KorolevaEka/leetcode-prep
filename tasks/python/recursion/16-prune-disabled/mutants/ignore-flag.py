def prune_disabled(tree):
    if tree is None:
        return None
    children = []
    for child in tree['children']:
        value = prune_disabled(child)
        if value is not None:
            children.append(value)
    return dict(name=tree['name'], enabled=True, children=children)
