def rotate_left(queue: list[str], k: int) -> list[str]:
    k %= len(queue)
    return queue[k:] + queue[:k]
