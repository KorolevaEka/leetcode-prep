def camel_to_snake(name: str) -> str:
    out = []
    for ch in name:
        if ch.isupper():
            out.append("_")
        out.append(ch.lower())
    return "".join(out)
