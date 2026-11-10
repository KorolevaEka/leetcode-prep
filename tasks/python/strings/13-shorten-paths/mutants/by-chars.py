import os


def shorten_paths(paths: list[str]) -> list[str]:
    prefix = os.path.commonprefix(paths)
    return [p[len(prefix):] for p in paths]
