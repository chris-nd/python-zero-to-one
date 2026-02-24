# Sur des variables

# la variable a n'est pas définie
try:
    print('a=', a)
except NameError as e:
    print("a n'est pas définie")

# on la définit
a = 10

# aucun souci ici, l'exception n'est pas levée
try:
    print('a=', a)
except NameError as e:
    print("a n'est pas définie")

# maintenant on peut effacer la variable
del a

# c'est comme si on ne l'avait pas définie
# dans la cellule précédente
try:
    print('a=', a)
except NameError as e:
    print("a n'est pas définie")

# Sur des listes

l = list(range(12))
print(l)

# on considère une slice dans cette liste
print('slice=', l[2:10:3])

# voyons ce que ça donne si on efface cette slice
del l[2:10:3]
print("après del", l)

# Sur les dictionnaires

# partons d'un dictionaire simple
d = dict(foo='bar', spam='eggs', a='b')
print(d)

# on peut enlever une clé avec del
del d['a']
print(d)

# Passge d'arguments multiples

print('l', l)
print('d', d)

del l[3:], d['spam']

print('l', l)
print('d', d)