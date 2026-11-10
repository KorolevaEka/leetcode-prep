from collections import OrderedDict


class LfuCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.d = OrderedDict()

    def get(self, key):
        if key not in self.d:
            return None
        self.d.move_to_end(key)
        return self.d[key]

    def put(self, key, value):
        if self.cap <= 0:
            return
        if key in self.d:
            self.d.move_to_end(key)
        elif len(self.d) >= self.cap:
            self.d.popitem(last=False)
        self.d[key] = value
