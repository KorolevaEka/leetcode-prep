def search_docs(docs: dict[str, str], query: str) -> list[str]:
    words = set(query.split())
    if not words:
        return []
    return sorted(i for i, text in docs.items() if words <= set(text.split()))
