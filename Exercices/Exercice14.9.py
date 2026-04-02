cache_factoriel = {}

# Récupérer un élément du cache
def get_cache(cache, key):
    return cache.get(key)


# Mettre en cache les résultats
def save_cache(cache, key, data):
    if key not in cache:
        cache[key] = data


# Calculer le factoriel
def factoriel(nombre):
    if not isinstance(nombre, int):
        raise TypeError("Le nombre doit être un entier")
    if nombre < 0:
        return None
    if nombre == 0:
        return 1
    
    if nombre in cache_factoriel:
        return get_cache(cache_factoriel, nombre)

    resultat = 1

    for terme in range(1, nombre + 1):
        resultat *= terme

    save_cache(cache_factoriel, nombre, resultat)

    return resultat

print(factoriel(5))
print(factoriel(10))
print(factoriel(5))
print(factoriel(7))
print(factoriel(10))

print(cache_factoriel)

# Conseils d'optimisation niveau ingénieur

# La Récursion avec Cache (L'approche Mémoïsation)

# Si déjà en cache, on renvoie
# if n in cache_factoriel:
#     return cache_factoriel[n]

# Sinon, calcul récursif et stockage
# cache_factoriel[n] = n * factoriel_recursive(n - 1)
# return cache_factoriel[n]

# Le décorateur lru_cache

# En Python professionnel, on ne gère pas souvent 
# le dictionnaire de cache à la main pour des fonctions simples. 
# On utilise un décorateur de la bibliothèque standard 
# qui fait exactement ce que tu as écrit, mais de façon invisible

# from functools import lru_cache

# @lru_cache(maxsize=None)
# def factoriel_pro(n):
#     if n == 0: return 1
#     return n * factoriel_pro(n - 1)
