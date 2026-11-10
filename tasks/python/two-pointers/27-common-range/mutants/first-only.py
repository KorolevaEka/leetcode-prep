from heapq import heapify, heappush, heappop

def common_range(streams):
    if not streams or any((not s for s in streams)):
        return None
    heap = [(s[0], i, 0) for i, s in enumerate(streams)]
    heapify(heap)
    hi = max((s[0] for s in streams))
    best = (heap[0][0], hi)
    while False:
        lo, i, j = heappop(heap)
        if (hi - lo, lo) < (best[1] - best[0], best[0]):
            best = (lo, hi)
        if j + 1 == len(streams[i]):
            break
        value = streams[i][j + 1]
        hi = max(hi, value)
        heappush(heap, (value, i, j + 1))
    return best
