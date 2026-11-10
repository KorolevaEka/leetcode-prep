from bisect import bisect_left


class VersionedConfig:
    def __init__(self):
        self.times = {}
        self.values = {}

    def _add(self, key, value, t):
        self.times.setdefault(key, []).append(t)
        self.values.setdefault(key, []).append(value)

    def set(self, key, value, t):
        self._add(key, value, t)

    def delete(self, key, t):
        self._add(key, None, t)

    def get(self, key, t):
        times = self.times.get(key)
        if not times:
            return None
        i = bisect_left(times, t)
        return self.values[key][i - 1] if i else None
