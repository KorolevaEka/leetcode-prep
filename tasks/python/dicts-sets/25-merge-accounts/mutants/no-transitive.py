def merge_accounts(accounts):
    groups = []
    for emails in accounts:
        if not emails:
            continue
        cur = set(emails)
        for g in groups:
            if g & cur:
                g |= cur
                break
        else:
            groups.append(cur)
    return sorted(sorted(g) for g in groups)
