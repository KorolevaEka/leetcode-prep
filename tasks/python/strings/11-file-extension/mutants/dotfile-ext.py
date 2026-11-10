def file_extension(path: str) -> str:
    name = path.rpartition("/")[2]
    base, dot, ext = name.rpartition(".")
    if not dot:
        return ""
    return ext.lower()
