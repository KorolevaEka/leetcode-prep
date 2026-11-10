def kth_matrix(matrix, k):
    lo, hi = (matrix[0][0], matrix[-1][-1])
    while lo < hi:
        mid = (lo + hi) // 2
        count = 0
        col = len(matrix[0]) - 1
        for row in matrix:
            while col >= 0 and row[col] >= mid:
                col -= 1
            count += col + 1
        if count < k:
            lo = mid + 1
        else:
            hi = mid
    return lo
