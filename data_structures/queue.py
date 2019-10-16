class Queue:
    
    def __init__(self):
        self._data = list()
    
    def enqueue(self, item):
        self._data.append(item)
            
    def dequeue(self):
        item = self._data[0]
        del self._data[0]
        return item
    
    def __len__(self):
        return len(self._data)