def truncate(msg: str, limit: int) -> str:
    if len(msg) <= limit:
        return msg
    return msg[:limit - 3] + "..."
