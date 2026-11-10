from collections import Counter

def chain_starts(text, words):
    if not words:
        return []
    w = len(words[0])
    need = Counter(words)
    out = []
    for offset in range(w):
        left = offset
        seen = Counter()
        size = 0
        for right in range(offset, len(text) - w + 1, w):
            word = text[right:right + w]
            if word not in need:
                seen.clear()
                size = 0
                left = right + w
                continue
            seen[word] += 1
            size += 1
            while seen[word] > need[word]:
                seen[text[left:left + w]] -= 1
                left += w
                size -= 1
            if size == len(words):
                out.append(left)
    return out
