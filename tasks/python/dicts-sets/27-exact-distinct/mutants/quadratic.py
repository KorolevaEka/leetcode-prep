def count_exact_distinct(codes, k):
    total = 0
    for i in range(len(codes)):
        seen = set()
        for j in range(i, len(codes)):
            seen.add(codes[j])
            if len(seen) == k:
                total += 1
            elif len(seen) > k:
                break
    return total
