import heapq


def run_order(deps):
    names = set(deps)
    for pre in deps.values():
        names.update(pre)
    dependents = {n: [] for n in names}
    missing = {n: 0 for n in names}
    for name, pre in deps.items():
        missing[name] = len(pre)
        for p in set(pre):
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
    if len(order) != len(names):
        raise ValueError("cycle")
    return order
