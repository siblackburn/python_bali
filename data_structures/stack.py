class Stack():

    def __init__(self):
        self._data = list()

    #push complexity: O(1)
    def push(self, item):
        self._data.append(item)

    # pop complexity: O(1) if implemented as a python list. Because we can directly access the index
    def pop(self):
        item = self._data[len(self._data) -1] #could also use pop
        del self._data[len(self._data) -1] # deletes the specified item at the index. We haven't used 'remove' because it's a little more memory intensive
        return item

    # peek complexity: O(1)
    def peek(self, item):
        # same as pop method, but doesn't remove from list. Peeks at the top of the stack, but no delete
        return self._data[-1]

    # len complexity: O(n)
    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return self._data
