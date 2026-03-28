from copy import copy

s = {1, 2, 3, 'a'} 

for i in s: 
    print(i) # 1, 2, 3, 'a'

print([x for x in s if type(x) is int]) # [1, 2, 3]

print(s) # {1, 2, 3, 'a'}

it = iter(s) # objet itérateur <set_iterator object at 0x...>

print(it) # <set_iterator object at 0x...>

next(it) # 1
next(it) # 2
next(it) # 3
next(it) # 'a'
# next(it) # RuntimeError: Set changed size during iteration
 
a = [1, 2] 
b = [3, 4]

iter(a) # <list_iterator object at 0x...>

z = zip(a, b) # <zip object at 0x...> qui est un iterateur

print(z) # <zip object at 0x...>
print(z is iter(z)) # True

print([i for i in z]) # [(1, 3), (2, 4)]
print(f"Type de z: {type(z)}")
print([i for i in z]) # []
print(next(z)) # RuntimeError: StopIteration

z = zip(a, b)
print([i for i in z]) # []

# Les limitations de la boucle for
try:
    ensemble = {'marc', 'albert'}
    for valeur in ensemble:
        if 'bert' not in valeur:
            ensemble.discard(valeur)
except RuntimeError as e:
    print(e)

# ATTENTION : Boucle infinie théorique
# liste = [1, 2, 3]
# for c in liste:
#     if c == 3:
#         liste.append(c) # On ajoute un élément, donc la boucle ne finit jamais

# 1ère solution pour contourner la limitation
ensemble = {'marc', 'albert'}
# On ne garde que ce qui nous intéresse
ensemble = {v for v in ensemble if 'bert' in v}

# 2ème solution pour contourner la limitation avec une shallow copy
ensemble = {'marc', 'albert'}

for valeur in copy(ensemble): # On itère sur la COPIE
    if 'bert' not in valeur:
        ensemble.discard(valeur) # On modifie l'ORIGINAL : OK !

# Aucune limitation à la modification des objets itérables contenus
liste = [[1], [2], [3]]
for sous_liste in liste:
    sous_liste.append(100) # On modifie l'objet CONTENU, pas la liste elle-même.




