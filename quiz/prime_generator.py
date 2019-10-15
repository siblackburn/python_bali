'''
- Write a function that generates the first n prime numbers
'''


def prime_n(x):
    for numbers in range(2, x):
        if x % numbers != 0:
            return True
        else:
            return False


prime_numbers = []

def primegen(n):
    prime_number_count = 0
    prime_start = 2
    while prime_number_count < n:
        if prime_n(prime_start) == True:
            prime_numbers.append(prime_start)
            prime_number_count += 1
            prime_start += 1
        else:
            prime_start += 1

user_input = primegen(10)
print(prime_numbers)