from heapq import heappush, heappop

def skyline(buildings):
    events = {}
    for l, r, h in buildings:
        events.setdefault(l, []).append((-h, r))
        events.setdefault(r, [])
    heap = [(0, float('inf'))]
    out = []
    for x in sorted(events):
        for item in events[x]:
            heappush(heap, item)
        while heap[0][1] <= x:
            heappop(heap)
        height = -heap[0][0]
        if not out or out[-1][1] != height:
            out.append((x, height))
    return out
