# Scénario 1

# Deux listes identiques en valeur
a = [1, 2]
b = [1, 2]

# Les valeurs sont égales
print('==', a == b)  # → True

# Mais ce sont des objets différents en mémoire
print('is', a is b)  # → False

# Scénario 2

# Une seule liste
a = [1, 2]

# b référence le même objet que a
b = a

# Les valeurs sont égales
print('==', a == b)  # → True

# ET c'est le même objet
print('is', a is b)  # → True

# Bonne pratique

undef = None

# ✅ RECOMMANDÉ : pythonique et efficace
if undef is None:
    print('indéfini')

# ❌ MOINS BON : fonctionne mais moins idiomatique
if undef == None:
    print('indéfini')

# Performance

# Liste gigantesque
huge_list = list(range(1_000_000))

# is : instantané (compare adresses)
huge_list is huge_list  # O(1)

# == : doit parcourir toute la liste
huge_list == huge_list  # O(n)

