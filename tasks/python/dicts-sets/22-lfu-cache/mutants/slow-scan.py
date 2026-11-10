class LfuCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.vals = {}
        self.info = {}
        self.tick = 0

    def _use(self, key):
        self.tick += 1
        self.info[key] = (self.info.get(key, (0, 0))[0] + 1, self.tick)

    def get(self, key):
        if key not in self.vals:
            return None
        self._use(key)
        return self.vals[key]

    def put(self, key, value):
        if self.cap <= 0:
            return
        if key not in self.vals and len(self.vals) >= self.cap:
            victim = min(self.vals, key=lambda k: self.info[k])
            del self.vals[victim]
            del self.info[victim]
        self.vals[key] = value
        self._use(key)
