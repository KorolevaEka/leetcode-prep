import re

_NUM = r"(0|[1-9][0-9]*)"
_VERSION = re.compile(rf"v?{_NUM}\.{_NUM}\.{_NUM}(-[0-9A-Za-z.]+)?")


def is_valid_version(s: str) -> bool:
    return _VERSION.match(s) is not None
