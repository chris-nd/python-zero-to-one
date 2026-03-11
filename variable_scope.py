a, b, c = 1, 1, 1

def g():
     b, c = 2, 4
     b = b + 10
     def h():
         c = 5
         print(a, b, c)
     h()
g()

print(a, b, c)

# on détruit la variable i si elle existe
if 'i' in locals(): 
    del i

# La variable 'i' n'est pas définie
try:
    i
except NameError as e:
    print('OOPS', e)

# si à présent on fait une boucle
# avec i comme variable de boucle
for i in [0]:
    pass

# alors maintenant i est définie
print(i)

# une façon très scabreuse de calculer la longueur de l
def length(l):
    for i, x in enumerate(l):
        pass
    return i + 1

print(length([1, 2, 3]))

# ceci provoque une UnboundLocalError
try:
    length([])
except Exception as e:
    print('OOPS', e)

# on veut chercher le premier de ces nombres qui vérifie une condition
candidates = [3, -15, 1, 8]

# pour fixer les idées disons qu'on cherche un multiple de 5, peu importe
def checks(candidate):
    return candidate % 5 == 0

# plutôt que de faire ceci
for item in candidates:
    if checks(item):
        break
print('trouvé solution', item)

# il vaut mieux faire ceci
solution = None
for item in candidates:
    if checks(item):
        solution = item
        break

print('trouvé solution', solution)

# la fonction length de tout à l'heure
def length1(l):
    for i, x in enumerate(l):
        pass
    return i + 1

# une version plus robuste 
def length2(l):
    # on initialise i explicitement
    # pour le cas où l est vide
    i = -1
    for i, x in enumerate(l):
        pass
    # comme cela i est toujours déclarée
    return i + 1

# ceci provoque une UnboundLocalError
try:
    length1([])
except Exception as e:
    print('OOPS', e)

# ceci fonctionne
print(length2([]))

# en Python 3, les variables de compréhension ne fuitent pas
liste = [j**2 for j in range(3)]

try:
    print(j)
except NameError as e:
    print('OOPS', e)