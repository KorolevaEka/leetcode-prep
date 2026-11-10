def is_mirror_code(code: str) -> bool:
    s = code.replace("-", "").lower()
    return s == s[::-1]
