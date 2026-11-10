from bisect import bisect_left

def ticket_cost(days, costs):
    a = sorted(set(days))
    dp = [0] * (len(a) + 1)
    for i in range(len(a) - 1, -1, -1):
        dp[i] = min((c + dp[bisect_left(a, a[i] + span)] for span, c in zip((1, 7, 30), costs)))
    return dp[0]
