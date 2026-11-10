def merge_accounts(accounts):
    parent = {}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for emails in accounts:
        for e in emails:
            parent.setdefault(e, e)
        for e in emails[1:]:
            parent[find(e)] = find(emails[0])
    groups = {}
    for emails in accounts:
        for e in emails:
            groups.setdefault(find(e), []).append(e)
    return sorted(sorted(g) for g in groups.values())
