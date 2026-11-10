import json

def parse_ndjson(text):
    values = []
    errors = []
    for number, line in enumerate(text.splitlines(), 0):
        if not line.strip():
            continue
        try:
            values.append(json.loads(line))
        except json.JSONDecodeError:
            errors.append(number)
    return (values, errors)
