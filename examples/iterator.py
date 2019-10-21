class MyDataStructure(object):

    def __init__(self):
        self._data = [1, 2, 3, 4]

    def __iter__(self):
        for i in self._data:
            yield i


my_data_structure = MyDataStructure()
for i in my_data_structure:
    print(i)