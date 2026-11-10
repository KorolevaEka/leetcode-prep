def last_position(items, target):
    if not items:
        return -1
    if items[-1] == target:
        return len(items) - 1
    return last_position(items[:-1], target)
