class Dictionary:

    def __init__(self, initial_size=4):
        self._data = [None] * initial_size

    def __len__(self):
        return len(self._data)

    def increase_array(self):
        if self.count_items() > len(self._data) - 3:
            self._data.extend([None] * len(self._data)) # need to finish off
            self._data.clear()
            self.set()


    def count_items(self):
        count = 0
        for lists in self._data:
            if lists is not None:
                for tupes in lists:
                    if tupes[0] is not None:
                        count += 1

        return count

    def get_index(self, key):
        index = hash(key) % len(self._data)
        return index

    def set(self, key, value):
        index = self.get_index(key)

        for tupes in self._data[index] or []:
            if tupes[0] == key:
                self._data[index].remove(tupes)

        if self._data[index] is None:
            self._data[index] = list()

        self._data[index].append((key, value))

        return self._data



    def get(self, key):
        index = self.get_index(key)
        for tupes in self._data[index]:
            if tupes[0] == key:
                return tupes[1]


    def contains(self, key):
        return key in [x[0] for x in (
                self._data[self.get_index(key)] or []
        )]

    def delete(self, key):
        index = self.get_index(key)

        for tupes in self._data[index] or []:
            if tupes[0] == key:
                self._data[index].remove(tupes)

    def print_list(self):
        print(self._data)


test = Dictionary()
test.set("wirld", 9)
test.set("a", 10)
test.set("b", 25)
test.set("c", 2)
test.set("d", 12)
test.set("e", 13)
test.set("f", 14)
test.print_list()
# print(test.contains("a"))
# print(test.get("d"))
print(test.__len__())
print(test.count_items(not None))










    # def delete(self, key):
    #     for items in self._data[key]:
    #         if items[key] == key:
    #             del self._data





# do we need to have a separate function to manage list size??
# need a linked list to store collisions - more than 1 bit of information at the same index in the list
# set list size - lookup
# if it gets two a few away from max length, double the length of list, to avoid collisions