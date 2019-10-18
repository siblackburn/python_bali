def qs(l):
    pivot = int(len(l) / 2)
    l_index = 0
    r_index = len(l)-1

    for item in range(l_index, pivot):
        if l[item] > l[pivot]:
            for item2 in range(pivot, r_index):
                if l[item2] < l[pivot]:
                    swap(l, item, item2)
            else:
                l.insert(pivot + 1, l.pop(item))

        else:
            for item2 in range(pivot, r_index):
                if l[item2] < l[pivot]:
                    for item in range(l_index, pivot):
                        if l[item] > l[pivot]:
                            swap(l, item, item2)
                    else:
                        l.insert(pivot - 1, l.pop(item2))

        l_index += 1
        r_index -= 1

    return l

def swap(list, i1, i2):
    temp = list[i1]
    list[i1] = list[i2]
    list[i2] = temp


test_list = [9,8,7,2,5]
output = qs(test_list)
print(output)

