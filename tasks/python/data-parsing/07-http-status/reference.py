def http_status(line):
    parts = line.strip().split(maxsplit=2)
    return (int(parts[1]), parts[2].strip() if len(parts) == 3 else '')
