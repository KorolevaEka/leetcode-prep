def truncate(msg: str, limit: int) -> str:
    if len(msg) <= limit:
        return msg
    if limit < 3:
        return "." * limit
    return msg[:limit - 3] + "..."
