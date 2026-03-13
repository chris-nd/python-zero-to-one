def count_digit(n):
    return len(str(abs(n)))
    
print(count_digit(12345))
print(count_digit(0))
print(count_digit(9876543210))
