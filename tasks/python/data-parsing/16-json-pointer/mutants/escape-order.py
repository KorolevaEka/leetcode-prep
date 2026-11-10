import re

def json_pointer(data, pointer):
    if pointer == '':
        return data
    if not pointer.startswith('/'):
        raise ValueError('prefix')
    node = data
    for raw in pointer[1:].split('/'):
        if re.search('~(?![01])', raw):
            raise ValueError('escape')
        key = raw.replace('~0', '~').replace('~1', '/')
        if isinstance(node, dict) and key in node:
            node = node[key]
        elif isinstance(node, list) and re.fullmatch('0|[1-9][0-9]*', key) and (int(key) < len(node)):
            node = node[int(key)]
        else:
            raise ValueError('missing')
    return node
