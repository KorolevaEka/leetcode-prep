def is_mirror_code(code: str) -> bool:
    s = code.replace("-", "").replace(" ", "").lower()
    return s == s[::-1]
