def rotate_left(queue: list[str], k: int) -> list[str]:
    return queue[k:] + queue[:k]
