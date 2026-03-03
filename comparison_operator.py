# Opérateurs de comparaison en Python

i = 5
j = 10

print(i == j)  # Égal à (False)
print(i != j)  # Différent de (True)
print(i < j)   # Inférieur à (True)
print(i <= j)  # Inférieur ou égal à (True)
print(i > j)   # Supérieur à (False)
print(i >= j)  # Supérieur ou égal à (False)

# Comparaison d'objets

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Égal à (True)
print(a is b)  # Identique (False)
c = a
print(a is c)  # Identique (True)

# Comparaison de valeurs entre -5 et 256

a = 10
b = 10
print(a == b)  # Égal à (True)
print(a is b)  # Identique (True)

# on peut comparer deux listes, mais ATTENTION
print([1, 2] <= [2, 3])  # Inférieur ou égal à (True)

# on ne peut pas par contre comparer deux nombres complexes
try:
    2j <= 3j
except Exception as e:
    print("OOPS", type(e), e)
