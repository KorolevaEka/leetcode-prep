class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def push(self, value):
        if len(self.items) > self.capacity:
            return False
        self.items.append(value)
        return True

    def pop(self):
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)
