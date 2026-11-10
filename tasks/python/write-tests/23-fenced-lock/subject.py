class LeaseLock:

    def __init__(self):
        self.lease = None
        self.counter = 0

    def acquire(self, owner, now, ttl):
        if self.lease and now < self.lease[2]:
            return None
        self.counter += 1
        self.lease = (owner, self.counter, now + ttl)
        return self.counter

    def release(self, owner, token, now):
        if not self.lease or self.lease[:2] != (owner, token) or now >= self.lease[2]:
            return False
        self.lease = None
        return True
