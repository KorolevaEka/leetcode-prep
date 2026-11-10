def count_exact_distinct(codes, k):
    def at_most(limit):
        if limit <= 0:
            return 0
        counts = {}
        left = 0
        total = 0
        for right, c in enumerate(codes):
            counts[c] = counts.get(c, 0) + 1
            if len(counts) > limit:
                counts[codes[left]] -= 1
                if counts[codes[left]] == 0:
                    del counts[codes[left]]
                left += 1
            total += right - left + 1
        return total

    return at_most(k) - at_most(k - 1)
