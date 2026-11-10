def min_day_cost(costs, days):
    n = len(costs)
    if days == 0:
        return 0 if n == 0 else -1
    if days < 0 or days >= n:
        return -1
    dp = [0] + [float('inf')] * n
    for _ in range(days):
        nxt = [float('inf')] * (n + 1)
        for end in range(1, n + 1):
            peak = 0
            for start in range(end - 1, -1, -1):
                peak = max(peak, costs[start])
                nxt[end] = min(nxt[end], dp[start] + peak)
        dp = nxt
    return dp[n]
