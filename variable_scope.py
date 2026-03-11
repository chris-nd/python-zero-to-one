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

# L’exception UnboundLocalError

def ma_fonction1():
    variable1 = "locale"
    print(variable1)

ma_fonction1()

variable2 = "globale"

def ma_fonction2():
    variable2 = "locale"
    print(variable2)

ma_fonction2()

# Variable globale
# On peut accéder en lecture à une variable globale sans précaution particulière
variable3 = "globale"

def ma_fonction3():
    print(variable3)

ma_fonction3()

# cet exemple ne fonctionne pas et lève UnboundLocalError
variable4 = "globale"

def ma_fonction4():
    # on référence la variable globale
    print(variable4)
    # et maintenant on crée une variable locale
    variable4 = "locale"

# on "attrape" l'exception
try:
    ma_fonction4()
except Exception as e:
    print(f"OOPS, exception {type(e)}:\n{e}")

# Une variable dans une fonction peut être ou bien locale 
# si elle est affectée dans la fonction ou bien globale 
# mais pas les deux à la fois

# Si vous avez une erreur UnboundLocalError, 
# c’est qu’à un moment donné il a eu cette confusion

# Pour résoudre ce conflit il faut explicitement
# déclarer la variable  comme globale
variable5 = "globale"

def ma_fonction5():
    global variable5
    # on référence la variable globale
    print("dans la fonction", variable5)
    # cette fois on modifie la variable globale
    variable5 = "changée localement"

ma_fonction5()
print("après la fonction", variable5)

