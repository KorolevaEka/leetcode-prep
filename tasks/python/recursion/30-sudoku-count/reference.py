def sudoku_count(board):
    a = [row[:] for row in board]
    rows = [set() for _ in a]
    cols = [set() for _ in a]
    boxes = [set() for _ in a]
    empty = []
    for r in range(4):
        for c in range(4):
            x = a[r][c]
            b = r // 2 * 2 + c // 2
            if not x:
                empty.append((r, c))
                continue
            if x in rows[r] or x in cols[c] or x in boxes[b]:
                return 0
            rows[r].add(x)
            cols[c].add(x)
            boxes[b].add(x)

    def visit(i):
        if i == len(empty):
            return 1
        r, c = empty[i]
        b = r // 2 * 2 + c // 2
        count = 0
        for x in range(1, 5):
            if x not in rows[r] and x not in cols[c] and (x not in boxes[b]):
                rows[r].add(x)
                cols[c].add(x)
                boxes[b].add(x)
                count += visit(i + 1)
                rows[r].remove(x)
                cols[c].remove(x)
                boxes[b].remove(x)
        return count
    return visit(0)
