def pgcd(a, b):
    while a != 0 and b != 0:
        if a == b:
            return a
        elif a < b:
            b = b - a
        else:
            a = a - b

    return a if a > 0 else b

print(pgcd(48, 18))
print(pgcd(100, 35))
print(pgcd(17, 19))