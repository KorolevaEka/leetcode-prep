import re


def mask_secrets(line: str, keys: list[str]) -> str:
    if not keys:
        return line
    names = "|".join(re.escape(k) for k in keys)
    pattern = rf"(?<![A-Za-z0-9_])({names})=[^\s]*"
    return re.sub(pattern, lambda m: m.group(1) + "=***", line, flags=re.IGNORECASE)
