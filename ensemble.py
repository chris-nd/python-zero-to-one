heteroclite = {'marc', 12, 'pierre', (1, 2, 3), 'pierre'}
print(heteroclite)

heteroclite2 = set(['marc', 12, 'pierre', (1, 2, 3), 'pierre'])
print(heteroclite2)

print(type({})) # on ne peut pas créer un ensemble vide en extension

# Pour créer un ensemble vide
ensemble_vide = set()
print(type(ensemble_vide))

# Ou également, moins élégant mais que l’on trouve parfois dans du vieux code
autre_ensemble_vide = set([])
print(type(autre_ensemble_vide))

# Un élément dans un ensemble doit être globalement immuable
# Le type set étant lui-même mutable, on ne peut pas créer un ensemble d’ensembles
# Et c’est une des raisons d’être du type frozenset

# la fonction frozenset

frozen_set = frozenset(ensemble_vide)
print(type(frozen_set))

print((1, 2, 3) in heteroclite)

print(len(heteroclite))

ensemble = {1, 2, 1}
print(ensemble)

# pour nettoyer
ensemble.clear()
print(ensemble)

# ajouter un element
ensemble.add(1)
print(ensemble)

# ajouter tous les elements d'un autre *ensemble*
ensemble.update({2, (1, 2, 3), (1, 3, 5)})
print(ensemble)

# enlever un element avec discard
ensemble.discard((1, 3, 5))
print(ensemble)

# discard fonctionne même si l'élément n'est pas présent
ensemble.discard('foo')
print(ensemble)

# enlever un élément avec remove
ensemble.remove((1, 2, 3))
print(ensemble)

# contrairement à discard, l'élément doit être présent,
# sinon il y a une exception
try:
    ensemble.remove('foo')
except KeyError as e:
    print("remove a levé l'exception", e)

# pop() ressemble à la méthode éponyme sur les listes
# sauf qu'il n'y a pas d'ordre dans un ensemble
while ensemble:
    element = ensemble.pop()
    print("element", element)
print("et bien sûr maintenant l'ensemble est vide", ensemble)

# Opérations classiques sur les ensembles

A2 = set([0, 2, 4, 6])
print('A2', A2)
A3 = set([0, 6, 3])
print('A3', A3)

# Union
print(A2 | A3)

# Intersection
print(A2 & A3)

# Différence
print(A2 - A3)

# Différence
print(A3 - A2)

# Différence Symétrique
# AΔB=(A−B)∪(B−A)
A2 ^ A3

# Comparaisons

superset = {0, 1, 2, 3}
print('superset', superset)
subset =  {1, 3}
print('subset', subset)

# égalité
print(heteroclite == heteroclite2)

# inclusion
print(subset <= superset)

print(subset < superset)

print(heteroclite < heteroclite2)

# Ensemble disjoints
print(heteroclite.isdisjoint(A3)) # Return True if two sets have a null intersection

