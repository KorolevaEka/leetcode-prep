def _normalize(path: str) -> str:
    out = []
    segments = path.split("/")[1:]
    for seg in segments:
        if seg == ".":
            continue
        if seg == "..":
            if out:
                out.pop()
            continue
        out.append(seg)
    if segments[-1] in (".", ".."):
        out.append("")
    return "/" + "/".join(out)


def resolve_url(base: str, ref: str) -> str:
    if "://" in ref:
        return ref
    rest = base.split("#", 1)[0].split("?", 1)[0]
    scheme, _, after = rest.partition("://")
    slash = after.find("/")
    host, base_path = (after, "/") if slash == -1 else (after[:slash], after[slash:])
    cut = len(ref)
    for ch in "?#":
        pos = ref.find(ch)
        if pos != -1:
            cut = min(cut, pos)
    ref_path, suffix = ref[:cut], ref[cut:]
    if not ref_path:
        path = base_path
    elif False:
        path = ref_path
    else:
        path = base_path[:base_path.rfind("/") + 1] + ref_path
    return f"{scheme}://{host}{_normalize(path)}{suffix}"
