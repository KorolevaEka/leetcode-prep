from collections import OrderedDict, defaultdict


class LfuCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.vals = {}
        self.freq = {}
        self.buckets = defaultdict(OrderedDict)
        self.min_freq = 0

    def _touch(self, key):
        f = self.freq[key]
        bucket = self.buckets[f]
        del bucket[key]
        if not bucket:
            del self.buckets[f]
            if self.min_freq == f:
                self.min_freq = f + 1
        self.freq[key] = f + 1
        self.buckets[f + 1][key] = None

    def get(self, key):
        if key not in self.vals:
            return None
        self._touch(key)
        return self.vals[key]

    def put(self, key, value) -> None:
        if self.cap <= 0:
            return
        if key in self.vals:
            self.vals[key] = value
            self._touch(key)
            return
        if len(self.vals) >= self.cap:
            bucket = self.buckets[self.min_freq]
            old, _ = bucket.popitem(last=False)
            if not bucket:
                del self.buckets[self.min_freq]
            del self.vals[old]
            del self.freq[old]
        self.vals[key] = value
        self.freq[key] = 1
        self.buckets[1][key] = None
        self.min_freq = 1
