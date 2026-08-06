"Variables et attributs"

# Variable globale: Elle est référencée directement
# par son nom et la règle LEGB s'applique à ces
# variables via le mécanisme de liaison lexicale
a = 1

def f():
    a = 2

class C:
    a = 3

print(a)
