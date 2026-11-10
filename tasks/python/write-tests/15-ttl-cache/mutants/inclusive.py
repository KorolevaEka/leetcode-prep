class Cache:

    def __init__(self):
        self.items = {}

    def put(self, key, value, now, ttl):
        self.items[key] = (value, now + ttl)

    def get(self, key, now):
        item = self.items.get(key)
        return item[0] if item is not None and now <= item[1] else None
