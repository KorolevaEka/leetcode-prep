def typed_env(values, schema):
    out = {}
    for key, kind in schema.items():
        if key not in values:
            continue
        value = values[key]
        if kind == 'int':
            out[key] = int(value)
        elif kind == 'bool':
            flag = value.strip().lower()
            if flag not in ('true', 'false'):
                raise ValueError('bool')
            out[key] = bool(value)
        else:
            out[key] = value
    return out
