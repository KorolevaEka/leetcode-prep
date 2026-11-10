def integer_lines(text):
    out = []
    for line in text.splitlines():
        line = line.strip()
        if line and (not line.startswith('#')):
            out.append(abs(int(line)))
    return out
