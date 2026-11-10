from collections import deque


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
    ready = deque(n for n, c in missing.items() if c == 0)
    order = []
    while ready:
        name = ready.popleft()
        order.append(name)
        for nxt in dependents[name]:
            missing[nxt] -= 1
            if missing[nxt] == 0:
                ready.append(nxt)
    if len(order) != len(prereqs):
        raise ValueError("cycle")
    return order
