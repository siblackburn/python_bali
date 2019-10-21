'''
This sorting technique works by counting the number of times each number occurs,
 assigning it to it's relative index, and then calculating it's final index
'''

def count_sort(l):
    sort_array = [0] * len(l)  # to store the number that's taken from the index position of count_array
    count_array = [0] * 100 # to store the count at each index (e.g. 2 numbers at index 4)

    '''
    insert each number from the list into the correponding index position in count_array
    The number stored at each index of the array will be the number of times that number had occurred
    '''
    for i in l:
        count_array[i] +=1


    '''
    For each index in count_array, insert the index number into the sort_array, for as long as the number of times you inserted it is less than the number stored at that index
    Because this extends the array, then need to pop off the empty spaces (0's that would appear at the end of the array)
    '''
    position_count = 0

    for numbers in range(0,len(count_array)):
        while count_array[numbers] >0:
            sort_array.insert(position_count, numbers)
            sort_array.pop()
            count_array[numbers] -=1
            position_count +=1

    return sort_array

test_list = [5,4,4,3,3,2,1,22,45,65]
output = count_sort(test_list)
print(output)
print(len(test_list))