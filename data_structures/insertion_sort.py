'''

Take the first item, designate it as "sorted" at the start, regardless of what it is
Take the 2nd item and move it to the sorted section. Is it smaller than the first item? If so, move it to the left of the first item
Then get 3rd item, move to sorted section, compare it the each number in sorted section to compare
Keep going till all numbers are in the sorted section

'''


def insertion_sort(l):
    sorted_count = 1
    other_count = 1
    for x in range(sorted_count, len(l)):
        for i in range(0, other_count):
            if l[x] < l[i]:
                l.insert(i, l.pop(x))
        other_count +=1

    sorted_count += 1
    return l



test_list = [22,24,9,4,1,3,2,99,101]
output = insertion_sort(test_list)
print(output)
print(len(test_list))
# 3412

#4132
#1432

#3
#1342

#2
#1324
#1234
#
# sorted_count = 1
#     for x in range(sorted_count, len(l)):
#         if l[x] < l[sorted_count-1]:
#             l.insert(sorted_count-1, l.pop(x))
#     sorted_count += 1
#
#     return l