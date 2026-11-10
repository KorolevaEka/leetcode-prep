def paired_actions(n):
    out = []

    def visit(text, opened, closed):
        if closed == n:
            out.append(text)
            return
        if opened < n:
            visit(text + '(', opened + 1, closed)
        if closed < opened:
            visit(text + ')', opened, closed + 1)
    visit('', 0, 0)
    return out
