from copy import deepcopy

def apply_patch(document, operations):
    result = deepcopy(document)
    for op in operations:
        kind = op['op']
        path = op['path']
        if kind not in ('add', 'replace', 'remove'):
            raise ValueError('operation')
        if not path:
            if kind == 'remove':
                raise ValueError('root')
            result = deepcopy(op['value'])
            continue
        node = result
        for key in path[:-1]:
            if isinstance(node, dict) and key in node:
                node = node[key]
            elif isinstance(node, list) and type(key) is int and (0 <= key < len(node)):
                node = node[key]
            else:
                raise ValueError('path')
        key = path[-1]
        if isinstance(node, dict) and isinstance(key, str):
            if kind == 'remove' and key not in node:
                raise ValueError('missing')
            if kind == 'remove':
                del node[key]
            else:
                node[key] = deepcopy(op['value'])
        elif isinstance(node, list) and type(key) is int:
            bound = len(node) + (kind == 'add')
            if not 0 <= key < bound:
                raise ValueError('index')
            if kind == 'add':
                node.insert(key, deepcopy(op['value']))
            elif kind == 'remove':
                node.pop(key)
            else:
                node[key] = deepcopy(op['value'])
        else:
            raise ValueError('target')
    return result
