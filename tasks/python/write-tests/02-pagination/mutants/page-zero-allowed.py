def paginate(items: list, page: int, per_page: int) -> list:
    if page < 0 or per_page < 1:
        raise ValueError("page and per_page must be positive")
    start = max(page - 1, 0) * per_page
    return items[start:start + per_page]
