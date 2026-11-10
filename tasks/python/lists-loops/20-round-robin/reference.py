from collections import deque


def finish_order(durations: list[int], quantum: int) -> list[int]:
    queue = deque(enumerate(durations))
    order = []
    while queue:
        i, left = queue.popleft()
        if left <= quantum:
            order.append(i)
        else:
            queue.append((i, left - quantum))
    return order
