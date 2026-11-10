import json

def json_types(text):
    out = []
    for x in json.loads(text):
        if x is None:
            kind = 'null'
        elif isinstance(x, bool):
            kind = 'bool'
        elif isinstance(x, (int, float)):
            kind = 'number'
        elif isinstance(x, str):
            kind = 'string'
        elif isinstance(x, list):
            kind = 'array'
        else:
            kind = 'object'
        out.append(kind)
    return out
