class Queue:
    
    def __init__(self):
        self._data = list()

    #enqueue complexity: O(1).
    def enqueue(self, item):
        self._data.append(item)

    # dequeue complexity: O(1)
    def dequeue(self):
        item = self._data[0]
        del self._data[0]
        return item

    # len complexity: O(n)
    def __len__(self):
        return len(self._data)