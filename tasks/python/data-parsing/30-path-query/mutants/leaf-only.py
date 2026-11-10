def select_json(document, path):
    tokens = path.split('/') if path else []
    found = set()
    visited = set()

    def visit(node, where, i):
        if (where, i) in visited:
            return
        visited.add((where, i))
        if i == len(tokens):
            found.add(where) if not isinstance(node, (dict, list)) else None
            return
        token = tokens[i]
        children = list(node.items()) if isinstance(node, dict) else list(enumerate(node)) if isinstance(node, list) else []
        if token == '**':
            visit(node, where, i + 1)
            for key, value in children:
                visit(value, where + (key,), i)
        else:
            for key, value in children:
                if token == '*' or str(key) == token:
                    visit(value, where + (key,), i + 1)
    visit(document, (), 0)
    out = []

    def emit(node, where):
        if where in found:
            out.append((where, node))
        children = node.items() if isinstance(node, dict) else enumerate(node) if isinstance(node, list) else []
        for key, value in children:
            emit(value, where + (key,))
    emit(document, ())
    return out
