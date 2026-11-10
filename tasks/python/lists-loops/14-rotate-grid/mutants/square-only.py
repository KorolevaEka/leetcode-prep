def rotate_grid(grid: list[list[str]]) -> list[list[str]]:
    n = len(grid)
    return [[grid[n - 1 - r][c] for r in range(n)] for c in range(n)]
