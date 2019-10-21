'''
Function to define what the pivot is. Take the existing list, defines a midpoint, a low, and a high. Chooses the median value of these 3
'''

# def pivot_number(l, low, high):
#     mid = round((low + high) // 2)
#     if l[low] < l[mid] < l[high-1]:
#         pivot = mid
#     elif l[high-1] < l[mid]:
#         pivot = high
#     else:
#         pivot = low
#
#     return pivot
#
# test_list = [9,8,22,2,1]
# output = pivot_number(test_list, 0, len(test_list))
# print(output)


def partition_function(l, low, high):
    low = 0
    high = 5
    pivot = 2

    for item_low in range(low, pivot):
        if l[item_low] > l[pivot]:
            swap(l, item_low, pivot)
            low += 1

    for item_high in range(pivot, high):
        if l[item_high] < pivot:
            swap(l, l[item_high], pivot)
            high -= 1

    return pivot

def quick_sort(l, low, high):
    if low < high:
        partition_index = partition_function(1,low,high)
        quick_sort(l, low, partition_index -1)
        quick_sort(l, partition_index + 1, high)


def swap(list, i1, i2):
    temp = list[i1]
    list[i1] = list[i2]
    list[i2] = temp


test_list = [9,8,7,2,5]
output = quick_sort(test_list, 0, len(test_list))
print(output)

