def list_divider(number):
    return [n for n in range(1, number + 1) if number % n == 0]

print(list_divider(24))
print(list_divider(36))