import re

def parse_json(text):
    i = 0

    def space():
        nonlocal i
        while i < len(text) and text[i] in ' \t\r\n':
            i += 1

    def string():
        nonlocal i
        i += 1
        out = ''
        escapes = {'"': '"', '\\': '\\', '/': '/', 'b': '\x08', 'f': '\x0c', 'n': '\n', 'r': '\r', 't': '\t'}
        while i < len(text):
            ch = text[i]
            i += 1
            if ch == '"':
                return out
            if ord(ch) < 32 or 55296 <= ord(ch) <= 57343:
                raise ValueError('control')
            if ch == '\\':
                if i == len(text):
                    raise ValueError('escape')
                ch = text[i]
                i += 1
                if ch == 'u':
                    digits = text[i:i + 4]
                    if len(digits) != 4 or any((c not in '0123456789abcdefABCDEF' for c in digits)):
                        raise ValueError('unicode')
                    value = int(digits, 16)
                    i += 4
                    if 55296 <= value <= 57343:
                        raise ValueError('surrogate')
                    ch = chr(value)
                elif ch in escapes:
                    ch = escapes[ch]
                else:
                    raise ValueError('escape')
            out += ch
        raise ValueError('string')

    def value():
        nonlocal i
        space()
        if i == len(text):
            raise ValueError('missing')
        ch = text[i]
        if ch == '"':
            return string()
        if ch in '[{':
            obj = ch == '{'
            end = '}' if obj else ']'
            result = {} if obj else []
            i += 1
            space()
            if i < len(text) and text[i] == end:
                i += 1
                return result
            while True:
                space()
                if obj:
                    if i == len(text) or text[i] != '"':
                        raise ValueError('key')
                    key = string()
                    space()
                    if key in result:
                        raise ValueError('duplicate')
                    if i == len(text) or text[i] != ':':
                        raise ValueError('colon')
                    i += 1
                    result[key] = value()
                else:
                    result.append(value())
                space()
                if i < len(text) and text[i] == end:
                    i += 1
                    return result
                if i == len(text) or text[i] != ',':
                    raise ValueError('separator')
                i += 1
        for token, item in [('true', True), ('false', False), ('null', None)]:
            if text.startswith(token, i):
                i += len(token)
                return item
        m = re.match('-?(?:0|[1-9][0-9]*)', text[i:])
        if not m:
            raise ValueError('number')
        i += len(m[0])
        return int(m[0])
    result = value()
    space()
    if i != len(text):
        raise ValueError('trailing')
    return result
