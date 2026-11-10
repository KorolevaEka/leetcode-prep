def insert_window(windows, new):
    a, b = new
    out = []
    placed = False
    for x, y in windows:
        if y <= a:
            out.append((x, y))
        elif x > b:
            if not placed:
                out.append((a, b))
                placed = True
            out.append((x, y))
        else:
            a = min(a, x)
            b = max(b, y)
    if not placed:
        out.append((a, b))
    return out
