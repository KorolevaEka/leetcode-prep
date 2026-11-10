def is_anagram(a: str, b: str) -> bool:
    return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())
