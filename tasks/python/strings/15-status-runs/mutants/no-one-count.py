def compress_statuses(s: str) -> str:
    parts = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        parts.append(s[i] + (str(j - i) if j - i > 1 else ""))
        i = j
    return "".join(parts)
