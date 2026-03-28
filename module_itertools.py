import itertools
import string

# Catégories d'outils/de fonctionnalités 
# pour construire des itérateurs complexes

# Les Itérateurs Infinis
# Les Combinatoires Mathématiques
# Les Utilitaires de parcours

# Exemples d'utlilitaires de parcours
# On enchaîne un tuple et une liste sans les copier
for x in itertools.chain((1, 2), [3, 4]):
    print(x) # Affiche 1, 2, 3, 4

support = string.ascii_lowercase # "abcdef..."

# On parcourt de l'indice 3 à 8 sans créer de sous-chaîne en mémoire
for x in itertools.islice(support, 3, 8):
    print(x) # Affiche d, e, f, g, h