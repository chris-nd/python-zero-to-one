def prime_number(n):
    prime = []
    for nombre in range(2, n + 1):
        is_prime = True

        for diviseur in range(2, nombre):
            if nombre % diviseur == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(nombre)
                
    return prime

print(prime_number(11))


