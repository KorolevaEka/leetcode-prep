def is_mirror(steps):
    if len(steps) < 2:
        return False
    return steps[0] == steps[-1] and is_mirror(steps[1:-1])
