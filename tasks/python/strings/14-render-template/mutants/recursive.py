import re

_PLACEHOLDER = re.compile(r"\{\{ *([A-Za-z0-9_]+) *\}\}")


def render_template(tpl: str, values: dict[str, str]) -> str:
    for _ in range(10):
        new = _PLACEHOLDER.sub(lambda m: values.get(m.group(1), m.group(0)), tpl)
        if new == tpl:
            break
        tpl = new
    return tpl
