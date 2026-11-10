class TtlCache:
    def __init__(self, ttl: float):
        self.ttl = ttl
        self.items: dict = {}

    def set(self, key, value, now: float) -> None:
        entry = self.items.get(key)
        if entry is not None and now < entry[1]:
            self.items[key] = (value, entry[1])
        else:
            self.items[key] = (value, now + self.ttl)

    def get(self, key, now: float):
        entry = self.items.get(key)
        if entry is None:
            return None
        value, expires = entry
        if now >= expires:
            del self.items[key]
            return None
        return value
