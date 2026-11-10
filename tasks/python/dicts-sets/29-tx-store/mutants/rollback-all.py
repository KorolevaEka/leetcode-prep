_GONE = object()


class TxStore:
    def __init__(self):
        self.base = {}
        self.layers = []

    def _top(self):
        return self.layers[-1] if self.layers else self.base

    def set(self, key, value):
        self._top()[key] = value

    def delete(self, key):
        if self.layers:
            self.layers[-1][key] = _GONE
        else:
            self.base.pop(key, None)

    def get(self, key):
        for layer in reversed(self.layers):
            if key in layer:
                v = layer[key]
                return None if v is _GONE else v
        return self.base.get(key)

    def begin(self):
        self.layers.append({})

    def rollback(self):
        if not self.layers:
            raise ValueError("no transaction")
        self.layers.clear()

    def commit(self):
        if not self.layers:
            raise ValueError("no transaction")
        top = self.layers.pop()
        if self.layers:
            self.layers[-1].update(top)
            return
        for k, v in top.items():
            if v is _GONE:
                self.base.pop(k, None)
            else:
                self.base[k] = v
