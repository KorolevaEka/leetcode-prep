from functools import cache

def collected_artifacts(grid):
    rows, cols = (len(grid), len(grid[0]))

    @cache
    def visit(row, a, b):
        reward = grid[row][a] + grid[row][b]
        if row == rows - 1:
            return reward
        return reward + max((visit(row + 1, a + da, b + db) for da in (-1, 0, 1) for db in (-1, 0, 1) if 0 <= a + da < cols and 0 <= b + db < cols))
    return visit(0, 0, cols - 1)
