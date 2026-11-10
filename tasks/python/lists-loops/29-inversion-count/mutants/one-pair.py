def inversion_count(ids):

    def merge(a):
        if len(a) < 2:
            return (a, 0)
        left, x = merge(a[:len(a) // 2])
        right, y = merge(a[len(a) // 2:])
        out = []
        i = j = 0
        count = x + y
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
                count += 1
        return (out + left[i:] + right[j:], count)
    return merge(ids)[1]
