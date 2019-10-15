def add_numbers(x, y):
    if user_input[0] == "+":
        return x + y
    else:
        return


user_input = input("enter an equation:")

add_position = user_input.find("+")
x = user_input[add_position + 2]
y = user_input[add_position + 4]

# print(add_position)
# print(x)
# print(y)

print(add_numbers(x, y))


