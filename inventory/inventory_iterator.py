from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, file_parsed):
        self.file_parsed = file_parsed
        self.pos = 0

    def __next__(self):
        try:
            item = self.file_parsed[self.pos]
        except IndexError:
            raise StopIteration()
        else:
            self.pos += 1
            return item
