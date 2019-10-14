'''
- Write a function that generates the first n prime numbers
'''

n_number = int(input("How many prime numbers do you want"))

prime_list = []

def prime_numbers(x):
    while len(prime_list) < n_number:
        for numbers in range(2, 1000):
            if numbers % == 0:
                prime_list.append(numbers)
    else:
        return prime_list


output = prime_numbers(n_number)
print(output)
