def quicksort2(l):
    high_list = []
    low_list = []
    pivot = round(len(l)/2)

    if len(low_list) <= 1:
        break

    for item in l:
        if item <= pivot:
            low_list.append(item)
        else:
            high_list.append(item)

    recursive_list = quicksort2(low_list) + pivot + quicksort2(high_list)

    return recursive_list


l = [1,3,4,7,2,5]
my_test = quicksort2(l)
print(my_test)



