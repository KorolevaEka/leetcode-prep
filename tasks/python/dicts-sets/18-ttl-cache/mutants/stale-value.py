class TtlCache:
    def __init__(self, ttl: float):
        self.ttl = ttl
        self.items: dict = {}

    def set(self, key, value, now: float) -> None:
        self.items[key] = (value, now + self.ttl)

    def get(self, key, now: float):
        entry = self.items.get(key)
        return None if entry is None else entry[0]
