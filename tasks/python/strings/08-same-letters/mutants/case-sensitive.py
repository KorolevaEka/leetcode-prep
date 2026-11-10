def is_anagram(a: str, b: str) -> bool:
    return sorted(a.replace(" ", "")) == sorted(b.replace(" ", "").lower())
