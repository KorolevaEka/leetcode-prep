def compress_statuses(s: str) -> str:
    parts = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j].lower() == s[i].lower():
            j += 1
        parts.append(f"{s[i]}{j - i}")
        i = j
    return "".join(parts)
