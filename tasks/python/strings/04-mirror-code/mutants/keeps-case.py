def is_mirror_code(code: str) -> bool:
    s = code.replace("-", "")
    return s == s[::-1]
