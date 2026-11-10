from copy import deepcopy

class VersionStore:

    def __init__(self):
        self.items = {}

    def read(self, key):
        value, version = self.items.get(key, (None, 0))
        return (deepcopy(value), version)

    def commit(self, changes, expected):
        if any((k not in expected for k in changes)):
            raise ValueError('missing version')
        if any((self.items.get(k, (None, 0))[1] != v for k, v in expected.items())):
            return False
        for key, value in changes.items():
            version = self.items.get(key, (None, 0))[1] + 1
            self.items[key] = (deepcopy(value), version)
        return True
