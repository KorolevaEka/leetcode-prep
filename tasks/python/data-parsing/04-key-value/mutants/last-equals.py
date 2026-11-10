def parse_pair(line):
    key, sep, value = line.rpartition('=')
    return (key.strip(), value.strip()) if sep and key.strip() else None
