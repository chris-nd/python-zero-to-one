def prime(n):
    if n < 2:
        return f"{n} n'est pas un nombre premier"
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"{n} n'est pas un nombre premier"
    
    return f"{n} est un nombre premier"

print(prime(2))
print(prime(17))
print(prime(25))
print(prime(97))
print(prime(100))
print(prime(1))