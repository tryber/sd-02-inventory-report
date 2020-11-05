from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable
        self.position = 0

    def __next__(self):
        try:
            current_value = self._iterable[self.position]
        except IndexError:
            self.position = 1
            return self._iterable[self.position - 1]
        else:
            self.position += 1
            return current_value

    def __previous__(self):
        try:
            self.position -= 1
            current_value = self._iterable[self.position]
        except IndexError:
            self.position = len(self._iterable) - 1
            return self._iterable[self.position]
        else:
            return current_value
