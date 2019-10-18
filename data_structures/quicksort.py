# class Quicksort():
#
#     def __init__(self, l=None, l_index=0, r_index=None, pivot=None):
#         self.l = l
#         self.l_index = l_index
#         self.r_index = r_index
#         self.pivot = pivot
#
#
#     def sort_func(self, l, l_index, r_index, pivot):
#         self.pivot = len(l) / 2
#         self.l_index = 0
#         self.r_index = len(l)
#         for items in range(l_index, pivot):
#             if items > pivot:
#                 l.insert(pivot + 1, l.pop(l[items]))
#         for i in range(pivot, r_index):
#             if i < pivot:
#                 l.insert(pivot - 1, l.pop(l[i]))
#
#         self.r_index = self.pivot
#         self.pivot = r_index / 2
#         self.l_index = 0
#
#         while self.pivot != self.l_index + 1:
#         self.sort_func()
#
#         else:
#         self.r_index = len(l)
#
#
#
#
# my_test = Quicksort()
# my_test.l = [1,5,2,7,3]
# my_test.sort_func()
# print(l)