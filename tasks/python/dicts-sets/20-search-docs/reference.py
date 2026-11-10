def search_docs(docs: dict[str, str], query: str) -> list[str]:
    words = set(query.lower().split())
    if not words:
        return []
    index: dict[str, set[str]] = {}
    for doc_id, text in docs.items():
        for word in set(text.lower().split()):
            index.setdefault(word, set()).add(doc_id)
    found = None
    for word in words:
        ids = index.get(word, set())
        found = ids if found is None else found & ids
    return sorted(found)
