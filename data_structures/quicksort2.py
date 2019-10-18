class Quicksort2():

    def __init__(self, l=None, l_index=0, pivot=1, r_index=2):
        self.l = l
        self.l_index = l_index
        self.pivot = pivot
        self.r_index = r_index


    def qs(self, l):
        pivot = 2
        l_index = 0
        r_index = 5

        while l_index < pivot:
            if l[l_index] < l[pivot]:
                while r_index > pivot:
                    if l[r_index] < l[pivot]:
                        self.swap(l[l_index], l[r_index])
                else:
                    l.insert(pivot + 1, l.pop(l[l_index]))

                r_index -= 1
        l_index += 1

        return l

    def swap(self, x, y):
        x, y = y, x

l = [1,3,4,7,2,5]
my_test = Quicksort2()
print(my_test.qs(l))



