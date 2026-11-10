def last_position(items, target):
    if not items:
        return -1
    if target in items:
        return items.index(target)
    return last_position(items[:-1], target)
