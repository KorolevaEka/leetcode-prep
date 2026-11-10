from urllib.parse import urljoin


def resolve_url(base: str, ref: str) -> str:
    return urljoin(base, ref)
