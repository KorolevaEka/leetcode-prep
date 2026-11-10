class VersionedConfig:
    def __init__(self):
        self.hist = {}

    def set(self, key, value, t):
        self.hist.setdefault(key, []).append((t, value))

    def delete(self, key, t):
        self.hist.setdefault(key, []).append((t, None))

    def get(self, key, t):
        for ts, v in reversed(self.hist.get(key, [])):
            if ts <= t:
                return v
        return None
