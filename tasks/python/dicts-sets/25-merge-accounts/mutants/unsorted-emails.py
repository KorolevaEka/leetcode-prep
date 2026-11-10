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
    for e in parent:
        groups.setdefault(find(e), []).append(e)
    return sorted(groups.values())
