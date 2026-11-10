import heapq


def run_order(deps):
    prereqs = {name: set(pre) for name, pre in deps.items()}
    for pre in list(prereqs.values()):
        for p in pre:
            prereqs.setdefault(p, set())
    dependents = {name: [] for name in prereqs}
    missing = {}
    for name, pre in prereqs.items():
        missing[name] = len(pre)
        for p in pre:
            dependents[p].append(name)
    ready = [n for n, c in missing.items() if c == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        name = heapq.heappop(ready)
        order.append(name)
        for nxt in dependents[name]:
            missing[nxt] -= 1
            if missing[nxt] == 0:
                heapq.heappush(ready, nxt)
    return order
