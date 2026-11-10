def equal_buckets(costs, k):
    if not costs or k > len(costs) or sum(costs) % k:
        return False
    target = sum(costs) // k
    a = sorted(costs, reverse=True)
    buckets = [0] * k

    def visit(i):
        if i == len(a):
            return True
        seen = set()
        for j in range(k):
            if buckets[j] in seen or buckets[j] + a[i] > target:
                continue
            seen.add(buckets[j])
            buckets[j] += a[i]
            if visit(i + 1):
                return True
            buckets[j] -= a[i]
        return False
    return visit(0)
