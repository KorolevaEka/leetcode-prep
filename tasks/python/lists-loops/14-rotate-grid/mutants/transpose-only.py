def rotate_grid(grid: list[list[str]]) -> list[list[str]]:
    return [list(row) for row in zip(*grid)]
