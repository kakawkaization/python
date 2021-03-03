class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def next(self):
        if self.offset >= len(self.wrapped):
            raise StopItrration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item
