def command_words(text):
    out = []
    token = ''
    active = False
    quote = None
    i = 0
    while i < len(text):
        ch = text[i]
        i += 1
        if ch == '\\' and quote != "'":
            if i == len(text):
                raise ValueError('escape')
            token += text[i]
            i += 1
            active = True
        elif quote:
            if ch == quote:
                quote = None
            else:
                token += ch
        elif ch in '\\"\'':
            quote = ch
            active = True
        elif ch in ' \t\n':
            if active:
                out.append(token)
                token = ''
                active = False
        else:
            token += ch
            active = True
    if quote:
        raise ValueError('quote')
    if active:
        out.append(token)
    return out
