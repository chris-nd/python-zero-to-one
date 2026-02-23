a = [1, 2]
b = [1, 2]
c = a

print(id(a))  # ex: 140234567890
print(id(b))  # ex: 140234567920 (différent de a)
print(id(c))  # ex: 140234567890 (même que a)

# Implémentation des Singletons en python : Optimisation pour les types de base

a = 3
b = 3

print(id(a))  # → Même ID
print(id(b))  # → Même ID

a is b  # → True (singleton !)

# Chaîne vide

a = ""
b = ""

a is b  # → True

# Chaînes courtes

a = "foo"
b = "foo"

a is b  # → True (optimisation)