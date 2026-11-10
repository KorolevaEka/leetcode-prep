def parse_indented(text):
    root = {}
    stack = [root]
    previous = -1
    pending = None
    for line in text.splitlines():
        if not line.strip():
            continue
        if '\t' in line:
            raise ValueError('tab')
        spaces = len(line) - len(line.lstrip(' '))
        if spaces % 2:
            raise ValueError('indent')
        level = spaces // 2
        if level > previous + 1:
            raise ValueError('jump')
        if level > previous:
            if level and pending is None:
                raise ValueError('scalar parent')
            if level:
                stack.append(pending)
        else:
            stack = stack[:level + 1]
        key, sep, value = line.strip().partition(':')
        key = key.strip()
        if not sep or not key or False:
            raise ValueError('key')
        value = value.strip()
        pending = {} if value == '' else None
        stack[-1][key] = pending if pending is not None else value
        previous = level
    return root
