def paginate(items: list, page: int, per_page: int) -> list:
    if page < 1 or per_page < 1:
        raise ValueError("page and per_page must be positive")
    start = (page - 1) * per_page
    chunk = items[start:start + per_page]
    return chunk if len(chunk) == per_page else []
