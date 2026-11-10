def rotate_left(queue: list[str], k: int) -> list[str]:
    if not queue:
        return []
    k %= len(queue)
    return queue[-k:] + queue[:-k] if k else list(queue)
