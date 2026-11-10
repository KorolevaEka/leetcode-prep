class Bookings:

    def __init__(self):
        self.items = []

    def book(self, start, end):
        if start >= end:
            raise ValueError('interval')
        if any((max(start, a) < min(end, b) for a, b in self.items)):
            return False
        self.items.append((start, end))
        return True

    def cancel(self, start, end):
        if (start, end) not in self.items:
            self.items.clear()
            return True
        self.items.remove((start, end))
        return True
