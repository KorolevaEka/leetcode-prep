class RollingStats:

    def __init__(self, capacity):
        self.capacity = capacity
        self.values = []

    def add(self, value):
        self.values.append(value)
        if len(self.values) > self.capacity:
            self.values.pop(0)

    def snapshot(self):
        if not self.values:
            return None
        a = sorted(self.values)
        n = len(a)
        return (n, a[0], a[-1], sum(a) / n, (a[(n - 1) // 2] + a[n // 2]) / 2)
