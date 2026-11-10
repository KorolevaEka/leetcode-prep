def is_anagram(a: str, b: str) -> bool:
    return sorted(a.lower()) == sorted(b.replace(" ", "").lower())
