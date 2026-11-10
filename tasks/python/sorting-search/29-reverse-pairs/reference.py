def drop_pairs(values):

    def sort(a):
        if len(a) < 2:
            return (a, 0)
        left, x = sort(a[:len(a) // 2])
        right, y = sort(a[len(a) // 2:])
        count = x + y
        j = 0
        for v in left:
            while j < len(right) and v > 2 * right[j]:
                j += 1
            count += j
        out = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        return (out + left[i:] + right[j:], count)
    return sort(values)[1]
