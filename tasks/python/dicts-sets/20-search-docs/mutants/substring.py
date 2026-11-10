def search_docs(docs: dict[str, str], query: str) -> list[str]:
    words = query.lower().split()
    if not words:
        return []
    return sorted(i for i, text in docs.items() if all(w in text.lower() for w in words))
