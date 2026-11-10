from collections import deque

def shortest_burst(values, target):
    prefix = [0]
    for x in values:
        prefix.append(prefix[-1] + x)
    q = deque()
    best = len(values) + 1
    for i, s in enumerate(prefix):
        while q and s - prefix[q[0]] > target:
            best = min(best, i - q.popleft())
        while q and prefix[q[-1]] >= s:
            q.pop()
        q.append(i)
    return best if best <= len(values) else -1
