import copy

#Shallow copy
source = [
    [1, 2, 3],  # une liste
    {1, 2, 3},  # un ensemble
    (1, 2, 3),  # un tuple
    '123',      # un string
    123,        # un entier
]

# une copie simple renvoie ceci
shallow_copy = copy.copy(source)
# -> shallow2 = source[:]
# revient à faire la même chose avec une liste

# Deep copy
deep_copy = copy.deepcopy(source)

# voir ci-dessous si ceci parait peu clair
# rappel au sujet de zip et enumerate
for i, (source_item, copy_item) in enumerate(zip(source, shallow_copy)):
    compare = source_item is copy_item
    print(f"source[{i}] is shallow_copy[{i}] -> {compare}")

# ceci est essentiellement équivalente à
for i in range(len(source)):
    compare = source[i] is shallow_copy[i]
    print(f"source[{i}] is shallow_copy[{i}] -> {compare}")

# Vérification des references après une deep copy
for i, (source_item, deep_item) in enumerate(zip(source, deep_copy)):
    compare = source_item is deep_item
    print(f"source[{i}] is deep_copy[{i}] -> {compare}")

# Observation après modification de la source
print("avant, source      ", source)
print("avant, shallow_copy", shallow_copy)
source[0].append(4)
print("après, source      ", source)
print("après, shallow_copy", shallow_copy)

print("avant, source      ", source)
print("avant, shallow_copy", shallow_copy)
source[0] = 'remplacement'
print("après, source      ", source)
print("après, shallow_copy", shallow_copy)

# Copie et référence circulaire
l = [None]
l[0] = l
print(l)

print(copy.copy(l))
print(copy.deepcopy(l))