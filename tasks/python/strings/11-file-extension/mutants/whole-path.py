def file_extension(path: str) -> str:
    name = path
    base, dot, ext = name.rpartition(".")
    if not dot or not base:
        return ""
    return ext.lower()
