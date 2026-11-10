from collections import deque

def window_peaks(values, k):
    if not values:
        return []
    q = deque()
    out = []
    for i, x in enumerate(values):
        while q and q[0] <= i - k:
            q.popleft()
        while q and values[q[-1]] >= x:
            q.pop()
        q.append(i)
        if i >= k - 1:
            out.append(values[q[0]])
    return out
