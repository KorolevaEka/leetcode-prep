def file_extension(path: str) -> str:
    name = path.rpartition("/")[2]
    base, dot, ext = name.rpartition(".")
    if not dot or not base:
        return ""
    return ext
