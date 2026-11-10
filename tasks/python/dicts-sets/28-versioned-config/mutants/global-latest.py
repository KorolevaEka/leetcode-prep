class VersionedConfig:
    def __init__(self):
        self.values = {}

    def set(self, key, value, t):
        self.values.setdefault(key, []).append((t, value))

    def delete(self, key, t):
        self.values.setdefault(key, []).append((t, None))

    def get(self, key, t):
        hist = self.values.get(key)
        if not hist:
            return None
        return hist[-1][1]
