def word_route(board, word):
    if not word:
        return True
    if not board or not board[0]:
        return False
    rows, cols = (len(board), len(board[0]))

    def visit(r, c, i, used):
        if not (0 <= r < rows and 0 <= c < cols) or (r, c) in used or board[r][c] != word[i]:
            return False
        if i == len(word) - 1:
            return True
        used = used | {(r, c)}
        return any((visit(r + dr, c + dc, i + 1, used) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1)]))
    return any((visit(r, c, 0, set()) for r in range(rows) for c in range(cols)))
