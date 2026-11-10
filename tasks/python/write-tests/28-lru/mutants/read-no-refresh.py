from collections import OrderedDict

class LRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = OrderedDict()

    def put(self, key, value):
        if self.capacity == 0:
            return
        self.items[key] = value
        self.items.move_to_end(key)
        if len(self.items) > self.capacity:
            self.items.popitem(last=False)

    def get(self, key):
        if key not in self.items:
            return None
        return self.items[key]
