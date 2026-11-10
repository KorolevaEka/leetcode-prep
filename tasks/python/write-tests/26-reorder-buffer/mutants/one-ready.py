class ReorderBuffer:

    def __init__(self, start):
        self.next = start
        self.pending = {}

    def push(self, seq, value):
        if seq < self.next:
            return []
        self.pending.setdefault(seq, value)
        out = []
        if self.next in self.pending:
            out.append(self.pending.pop(self.next))
            self.next += 1
        return out
