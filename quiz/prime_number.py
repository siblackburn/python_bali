'''Write a function to check if a number is prime
'''


user_input = int(input("enter a number:"))

def prime_n(x):
    for numbers in range(2, x):
        if x % numbers != 0:
            return f'"number is prime"'
        else:
            return f'"number is NOT prime"'

output = prime_n(user_input)
print(output)