def _text(value: object) -> str:
    return "" if value is None else str(value)


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def render_table(headers: list[str], rows: list[list[object]]) -> str:
    widths = [max([len(h)] + [len(_text(r[i])) for r in rows]) for i, h in enumerate(headers)]
    lines = [
        "| " + " | ".join(h.ljust(w) for h, w in zip(headers, widths)) + " |",
        "|" + "|".join("-" * (w + 2) for w in widths) + "|",
    ]
    for row in rows:
        cells = [
            _text(v).ljust(w)
            for v, w in zip(row, widths)
        ]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)
