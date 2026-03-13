import math

def factorial(n):
    multiple = 1
    for number in range(2, n + 1):
        multiple *= number
    return multiple

print(factorial(100))

# def factorial(n):
#     return math.factorial(n)

# print(factorial(100))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1 
#     return n * factorial(n - 1)

# print(factorial(100))