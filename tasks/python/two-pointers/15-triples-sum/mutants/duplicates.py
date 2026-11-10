def triples_with_sum(values: list[int], target: int) -> list[tuple[int, int, int]]:
    v = sorted(values)
    out = []
    for i in range(len(v) - 2):
        l, r = i + 1, len(v) - 1
        while l < r:
            s = v[i] + v[l] + v[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                out.append((v[i], v[l], v[r]))
                l += 1
                r -= 1
                while l < r and v[l] == v[l - 1]:
                    l += 1
                while l < r and v[r] == v[r + 1]:
                    r -= 1
    return out
