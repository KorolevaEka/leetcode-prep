from bisect import bisect_left, bisect_right

def best_reward(jobs):
    a = sorted(jobs, key=lambda x: x[1])
    ends = [x[1] for x in a]
    dp = [0]
    for i, (start, end, reward) in enumerate(a):
        prev = bisect_left(ends, start, 0, i)
        dp.append(max(dp[-1], dp[prev] + reward))
    return dp[-1]
