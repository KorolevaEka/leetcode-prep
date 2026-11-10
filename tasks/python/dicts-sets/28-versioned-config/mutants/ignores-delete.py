from bisect import bisect_right


class VersionedConfig:
    def __init__(self):
        self.times = {}
        self.values = {}

    def set(self, key, value, t):
        self.times.setdefault(key, []).append(t)
        self.values.setdefault(key, []).append(value)

    def delete(self, key, t):
        pass

    def get(self, key, t):
        times = self.times.get(key)
        if not times:
            return None
        i = bisect_right(times, t)
        return self.values[key][i - 1] if i else None
