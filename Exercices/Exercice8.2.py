def sum_number(n):
    sum = 0
    for number in range(1, n + 1):
        sum += number
    print(sum)

sum_number(100)

# def sum_number(n):
#     return sum(range(1, n + 1))

# print(sum_number(100))


# Avec la formule mathématique (plus rapide)
# def sum_number(n):
#     return n * (n + 1) // 2

# print(sum_number(100))

# Méthode de Gauss (mathématicien célèbre qui l'a découvert enfant) :
# Écrivons la somme deux fois, une à l'endroit, une à l'envers :
#   1  +   2  +   3  + ... +  99  + 100    (somme normale)
# 100  +  99  +  98  + ... +   2  +   1    (somme inversée)
# ─────────────────────────────────────
# 101  + 101  + 101  + ... + 101  + 101    (addition)