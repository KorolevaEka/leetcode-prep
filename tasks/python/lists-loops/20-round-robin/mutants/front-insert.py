from collections import deque

def finish_order(durations: list[int], quantum: int) -> list[int]:
    queue = deque((i, d) for i, d in enumerate(durations))
    order = []
    while queue:
        i, left = queue.popleft()
        if left <= quantum:
            order.append(i)
        else:
            queue.appendleft((i, left - quantum))
    return order
