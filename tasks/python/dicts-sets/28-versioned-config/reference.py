from bisect import bisect_right


class VersionedConfig:
    def __init__(self):
        self.times = {}
        self.values = {}

    def _add(self, key, value, t):
        self.times.setdefault(key, []).append(t)
        self.values.setdefault(key, []).append(value)

    def set(self, key, value, t: int) -> None:
        self._add(key, value, t)

    def delete(self, key, t: int) -> None:
        self._add(key, None, t)

    def get(self, key, t: int):
        times = self.times.get(key)
        if not times:
            return None
        i = bisect_right(times, t)
        return self.values[key][i - 1] if i else None
