class Stack():

    def __init__(self):
        self._data = list()

    def push(self, item):
        self._data.append(item)

    def pop(self):
        item = self._data[len(self._data) -1] #could also use pop
        del self._data[len(self._data) -1] # deletes the specified item at the index. We haven't used 'remove' because it's a little more memory intensive
        return item

    def peek(self, item):
        # same as pop method, but doesn't remove from list. Peeks at the top of the stack, but no delete
        return self._data[-1]

    def __len__(self):
        return len(self._data)
