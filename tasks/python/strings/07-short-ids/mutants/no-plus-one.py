def _common(a: str, b: str) -> int:
    n = min(len(a), len(b))
    k = 0
    while k < n and a[k] == b[k]:
        k += 1
    return k


def shortest_prefixes(names: list[str]) -> list[str]:
    order = sorted(range(len(names)), key=lambda i: names[i])
    result = [""] * len(names)
    for pos, i in enumerate(order):
        need = 0
        if pos > 0:
            need = max(need, _common(names[order[pos - 1]], names[i]))
        if pos + 1 < len(order):
            need = max(need, _common(names[i], names[order[pos + 1]]))
        result[i] = names[i][:need]
    return result
