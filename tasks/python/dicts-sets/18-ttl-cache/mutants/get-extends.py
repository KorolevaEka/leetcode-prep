class TtlCache:
    def __init__(self, ttl: float):
        self.ttl = ttl
        self.items: dict = {}

    def set(self, key, value, now: float) -> None:
        self.items[key] = (value, now + self.ttl)

    def get(self, key, now: float):
        entry = self.items.get(key)
        if entry is None:
            return None
        value, expires = entry
        if now >= expires:
            del self.items[key]
            return None
        self.items[key] = (value, now + self.ttl)
        return value
