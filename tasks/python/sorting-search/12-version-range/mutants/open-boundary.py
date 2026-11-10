def versions_between(versions, low, high):

    def key(v):
        a = list(map(int, v.split('.')))
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return tuple(a)
    return sorted([v for v in versions if key(low) < key(v) < key(high)], key=key)
