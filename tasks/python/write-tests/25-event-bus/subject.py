class EventBus:

    def __init__(self):
        self.callbacks = {}
        self.counter = 0

    def subscribe(self, callback):
        self.counter += 1
        self.callbacks[self.counter] = callback
        return self.counter

    def unsubscribe(self, token):
        if token not in self.callbacks:
            return False
        del self.callbacks[token]
        return True

    def publish(self, value):
        for callback in list(self.callbacks.values()):
            callback(value)
