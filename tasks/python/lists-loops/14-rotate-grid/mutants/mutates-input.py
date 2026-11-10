def rotate_grid(grid: list[list[str]]) -> list[list[str]]:
    for row in grid:
        row.reverse()
    return [list(row) for row in zip(*grid)]
