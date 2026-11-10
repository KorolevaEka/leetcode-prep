def shipping_capacity(weights, days):
    if not weights:
        return 0
    lo, hi = (max(weights), sum(weights))
    while lo < hi:
        cap = (lo + hi) // 2
        used = 1
        load = 0
        for w in weights:
            if load + w > cap:
                used += 1
                load = 0
            load += w
        if used > days:
            lo = cap + 1
        else:
            hi = cap
    return lo
