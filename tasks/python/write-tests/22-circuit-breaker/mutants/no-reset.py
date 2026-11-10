class Breaker:

    def __init__(self, threshold, cooldown):
        self.threshold = threshold
        self.cooldown = cooldown
        self.failures = 0
        self.until = None

    def call(self, operation, now):
        if self.until is not None and now < self.until:
            raise RuntimeError('open')
        probing = self.until is not None
        try:
            value = operation()
        except ValueError:
            self.failures += 1
            if probing or self.failures >= self.threshold:
                self.until = now + self.cooldown
            raise
        self.until = None
        return value
