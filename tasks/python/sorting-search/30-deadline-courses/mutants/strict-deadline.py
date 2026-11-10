from heapq import heappush, heappop

def max_courses(courses):
    heap = []
    total = 0
    for duration, deadline in sorted(courses, key=lambda x: x[1]):
        total += duration
        heappush(heap, -duration)
        if total >= deadline:
            total += heappop(heap)
    return len(heap)
