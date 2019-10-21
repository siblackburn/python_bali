'''
With each iteration the largest "bubble" goes to the top
starts with the first 2 numbers and 2 points
if the one on the left is the largest, move it to the right
move the pointers forward, then repeat
The result at the end of the first iteration is that the largest number is at the top. Leave that one alone
Then Repeat the whole process again
'''


def bubble_sort(l):
    pointer_1 = 0
    pointer_2 = 1
    count = 0
    while count <= len(l):
        while pointer_2 < len(l):
            if l[pointer_1] > l[pointer_2]:
                temp = l[pointer_1]
                l[pointer_1] = l[pointer_2]
                l[pointer_2] = temp
            else:
                pointer_1 += 1
                pointer_2 += 1
        pointer_1 = 0
        pointer_2 = 1
        count += 1

    return l

test_list = [7,4,1,-1,3,2,5,0,29]
output = bubble_sort(test_list)
print(output)

print(len(test_list))
