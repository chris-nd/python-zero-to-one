tuple1 = ()
tuple2 = (1, 2, 3)
tuple3 = (1,)
tuple4 = (1) # This is a integer, not an tuple
tuple5 = (True, 2.4, 31)
tuple6 = True, 2.4, 31

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4))
print(type(tuple5))
print(type(tuple6))

tuple1 = (1, 2,)
tuple2 = (3, 4,)

# Addition crée un NOUVEAU tuple
resultat = tuple1 + tuple2
print(resultat)  # → (1, 2, 3, 4)

tuple1 = (1, 2,)
tuple1 += (3, 4,)  # Crée un NOUVEAU tuple
print(tuple1)  # → (1, 2, 3, 4)

# Construire des tuples élaborés

# 1. Construire une liste pas à pas
liste = list(range(10))    # [0, 1, 2, ..., 9]
liste[9] = 'Inconnu'       # Modifier
del liste[2:5]             # Supprimer des éléments

# 2. Convertir en tuple
mon_tuple = tuple(liste)
print(mon_tuple)  # → (0, 1, 5, 6, 7, 8, 'Inconnu')

# Attention : ne pas écraser les noms prédéfinis

liste = range(10)

# ❌ ERREUR : écrase la fonction tuple()
#tuple = tuple(liste)  
# tuple est maintenant un objet, pas une fonction

# Plus tard...
# autre_tuple = tuple(range(100))  
# TypeError: 'tuple' object is not callable

# Tuple unpacking

couple = (100, 'spam')

# ❌ Pas pythonique
gauche = couple[0]
droite = couple[1]

# ✅ Pythonique - avec parenthèses
(gauche, droite) = couple

# ✅ Pythonique - sans parenthèses (plus courant)
gauche, droite = couple

(tuple_unpacking1, tuple_unpacking2) = [1, 2]
print(tuple_unpacking1)
print(tuple_unpacking2)

tuple_unpacking1, tuple_unpacking2 = 1, 2
print(tuple_unpacking1)
print(tuple_unpacking2)

Liste = list(range(10))
print(Liste)

# Dans la suite de Fibonacci
n = 10
for i in range(2, n + 1):
    f2, f1 = f1, f1 + f2

# Unpacking en profondeur

structure = ['abc', [(1, 2), ([3], 4)], 5]

# Extraire le 3 situé en profondeur
(a, (b, ((trois,), c)), d) = structure
print('trois', trois)  # → trois 3

# Ou plus lisible
(a, (b, ([trois], c)), d) = structure
print('trois', trois)  # → trois 3

# Alternative (moins pythonique)
trois = structure[1][1][0][0]

# Extended unpacking

reference = [1, 2, 3, 4, 5]

# *b capture tout ce qui est entre a et c
a, *b, c = reference # Une seule variable avec * par niveau d'unpacking
print(f"a={a} b={b} c={c}")

reference = range(20)
a, *b, c = reference
print(f"a={a} b={b} c={c}")

data = ['Jean', 'Dupont', '061234567', '12', 'rue du four', '57000', 'METZ']

# On ne s'intéresse qu'aux deux premiers
prenom, nom, *_ = data
print(f"prenom={prenom} nom={nom}")

entree = [1, 2, 3]

# La dernière affectation gagne
a, a, a = entree
print(f"a = {a}")  # → a = 3

# Ignore premier et dernier éléments
_, milieu, _ = entree
print('milieu', milieu)  # → milieu 2

# Ou avec un nom plus explicite
ignored, ignored, right = entree
print('right', right)  # → right 3

# Extended unpacking en profondeur

tree = [1, 2, [(3, 33, 'three', 'thirty-three')],
        ([4, 44, ('forty', 'forty-four')])]

# Extended unpacking à plusieurs niveaux
*_, ((_, *x3, _),), (*_, x4) = tree #Une seule *variable par niveau d'imbrication.
print(f"x3={x3}, x4={x4}")
# → x3=['three'], x4=('forty', 'forty-four')

extended_tuple_unpacking1, *extended_tuple_unpacking2 = Liste
print(extended_tuple_unpacking1)
print(extended_tuple_unpacking2)

*extended_tuple_unpacking1, extended_tuple_unpacking2 = Liste
print(extended_tuple_unpacking1)
print(extended_tuple_unpacking2)

# Plusieurs variables dans une boucle for

entrees = [(1, 2), (3, 4), (5, 6)]

for a, b in entrees:
    print(f"a={a} b={b}")

# la fonction zip

villes = ["Paris", "Nice", "Lyon"]
populations = [2*10**6, 4*10**5, 10**6]

# zip() crée des tuples à partir de listes parallèles
print(list(zip(villes, populations)))
# → [('Paris', 2000000), ('Nice', 400000), ('Lyon', 1000000)]

for ville, population in zip(villes, populations):
    print(population, "habitants à", ville)

for i, j, k in zip(range(3), range(100, 103), range(200, 203)):
    print(f"i={i} j={j} k={k}")

# Premier argument : 2 éléments
# Deuxième argument : 4 éléments
for units, tens in zip([1, 2], [10, 20, 30, 40]):
    print(units, tens)

# Sortie (seulement 2 itérations) :
# 1 10
# 2 20

# La fonction enumerate()

villes = ["Paris", "Nice", "Lyon"]

for i, ville in enumerate(villes):
    print(i, ville)

# Mauvais : manipulation d'indices
for i in range(len(villes)):
    print(i, villes[i])

# Mauvais : utilisation détournée de zip
for i, ville in zip(range(len(villes)), villes):
    print(i, ville)

