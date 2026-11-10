import json

def json_field(text, key):
    return json.loads(text).get(key)
