from functools import cache

def collected_artifacts(grid):
    rows, cols = (len(grid), len(grid[0]))

    @cache
    def visit(row, a, b):
        reward = grid[row][a] + (grid[row][b] if a != b else 0)
        if row == rows - 1:
            return reward
        return reward + max((visit(row + 1, a + da, b + db) for da in (0,) for db in (0,) if 0 <= a + da < cols and 0 <= b + db < cols))
    return visit(0, 0, cols - 1)
