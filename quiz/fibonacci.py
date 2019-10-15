sequence_length = int(input("how many fibonacci numbers do you want?"))

fib_numbers = [1,1]

while len(fib_numbers) < sequence_length:
    new_numbers = fib_numbers[-2] + fib_numbers[-1]
    fib_numbers.append(new_numbers)

print(fib_numbers)


