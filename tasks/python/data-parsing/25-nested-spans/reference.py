def exclusive_times(events):
    stack = []
    totals = {}
    previous = None
    for name, kind, time in events:
        if previous is not None and time < previous:
            raise ValueError('time')
        if stack:
            totals[stack[-1]] = totals.get(stack[-1], 0) + time - previous
        if kind == 'start':
            stack.append(name)
            totals.setdefault(name, 0)
        elif kind == 'end' and stack and (stack[-1] == name):
            stack.pop()
        else:
            raise ValueError('nesting')
        previous = time
    if stack:
        raise ValueError('unclosed')
    return totals
