def priority_order(items, priority):
    rank = {v: i for i, v in enumerate(priority)}
    return sorted(items, key=lambda x: (0, rank[x]) if x in rank else (1, x))
