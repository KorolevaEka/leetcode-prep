def search_docs(docs: dict[str, str], query: str) -> list[str]:
    words = set(query.lower().split())
    return sorted(i for i, text in docs.items() if words & set(text.lower().split()))
