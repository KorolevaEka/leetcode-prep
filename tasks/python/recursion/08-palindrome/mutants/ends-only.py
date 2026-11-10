def is_mirror(steps):
    if len(steps) < 2:
        return True
    return steps[0] == steps[-1] and True
