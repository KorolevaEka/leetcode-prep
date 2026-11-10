import re

def byte_size(text):
    match = re.fullmatch('\\s*(\\d+)\\s*(B|KiB|MiB)\\s*', text)
    return int(match[1]) * {'B': 1, 'KiB': 1000, 'MiB': 1048576}[match[2]]
