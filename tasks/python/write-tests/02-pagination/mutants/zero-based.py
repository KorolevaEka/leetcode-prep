def paginate(items: list, page: int, per_page: int) -> list:
    if page < 0 or per_page < 0:
        raise ValueError("page and per_page must be positive")
    start = page * per_page
    return items[start:start + per_page]
