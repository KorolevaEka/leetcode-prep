def max_cleanup(rewards):
    a = [1] + rewards + [1]
    n = len(a)
    dp = [[0] * n for _ in a]
    for width in range(2, n):
        for left in range(n - width):
            right = left + width
            dp[left][right] = max((dp[left][k] + dp[k][right] + a[left] * a[k] * a[right] for k in range(left + 1, right)))
    return dp[0][-1]
