from heapq import heappush, heappop

def merge_streams(streams):
    heap = []
    for i, s in enumerate(streams):
        if s:
            heappush(heap, (s[0], i, 0))
    out = []
    while heap:
        value, i, j = heappop(heap)
        out.append(value)
        if j + 2 < len(streams[i]):
            heappush(heap, (streams[i][j + 1], i, j + 1))
    return out
