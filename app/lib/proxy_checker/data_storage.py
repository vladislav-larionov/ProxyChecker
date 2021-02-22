class DataStorage:
    def __init__(self, data):
        self.data = set(data)
        self.total = len(self.data)

    def next(self):
        return self.data.pop()

    def has_next(self):
        return len(self.data) != 0

    def add(self, data):
        self.data.add(data)

    def size(self):
        return len(self.data)
