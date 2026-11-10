def shorten_paths(paths: list[str]) -> list[str]:
    if not paths:
        return []
    parts = [p.split("/") for p in paths]
    dirs = [p[:-1] for p in parts]
    n = 0
    for comps in zip(*dirs):
        if len(set(comps)) != 1:
            break
        n += 1
    return ["/".join(p[n:]) for p in parts]
