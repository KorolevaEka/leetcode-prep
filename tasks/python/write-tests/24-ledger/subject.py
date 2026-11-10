class Ledger:

    def __init__(self, balances):
        self.balances = dict(balances)
        self.done = {}

    def balance(self, name):
        return self.balances[name]

    def transfer(self, id, source, target, amount):
        args = (source, target, amount)
        if id in self.done:
            if self.done[id] != args:
                raise ValueError('conflict')
            return False
        if amount <= 0 or source == target or source not in self.balances or (target not in self.balances):
            raise ValueError('arguments')
        if self.balances[source] < amount:
            raise ValueError('funds')
        self.balances[source] -= amount
        self.balances[target] += amount
        self.done[id] = args
        return True
