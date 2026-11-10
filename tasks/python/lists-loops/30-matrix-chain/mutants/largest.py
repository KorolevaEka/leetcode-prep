def matrix_cost(dims):
    n = len(dims) - 1
    if n < 2:
        return 0
    dp = [[0] * n for _ in range(n)]
    for width in range(2, n + 1):
        for i in range(n - width + 1):
            j = i + width - 1
            dp[i][j] = max((dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1] for k in range(i, j)))
    return dp[0][-1]
