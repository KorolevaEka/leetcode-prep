def is_mirror_code(code: str) -> bool:
    s = code.lower()
    return s == s[::-1]
