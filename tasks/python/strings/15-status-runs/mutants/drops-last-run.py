def compress_statuses(s: str) -> str:
    out = []
    prev = ""
    count = 0
    for ch in s:
        if ch == prev:
            count += 1
        else:
            if prev:
                out.append(f"{prev}{count}")
            prev, count = ch, 1
    return "".join(out)
