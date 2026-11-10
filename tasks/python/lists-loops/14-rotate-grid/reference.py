def rotate_grid(grid: list[list[str]]) -> list[list[str]]:
    return [[grid[r][c] for r in range(len(grid) - 1, -1, -1)] for c in range(len(grid[0]) if grid else 0)]
