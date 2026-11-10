import difflib


def longest_common_chunk(a: str, b: str) -> str:
    m = difflib.SequenceMatcher(None, a, b, autojunk=False).find_longest_match(0, len(a), 0, len(b))
    return a[m.a:m.a + m.size]
