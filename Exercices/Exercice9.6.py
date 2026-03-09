def square(start, end):
    return [(number, number**2) for number in range(start, end + 1)]

print(square(1, 10))