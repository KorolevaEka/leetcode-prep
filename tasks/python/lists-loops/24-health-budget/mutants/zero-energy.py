def initial_energy(grid):
    rows, cols = (len(grid), len(grid[0]))
    dp = [float('inf')] * (cols + 1)
    dp[cols - 1] = 1
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            dp[c] = max(0, min(dp[c], dp[c + 1]) - grid[r][c])
    return dp[0]
