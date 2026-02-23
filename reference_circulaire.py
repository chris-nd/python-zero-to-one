# Créer une liste à un élément
infini_1 = [None]

# Remplacer cet élément par ... la liste elle-même !
infini_1[0] = infini_1

print(infini_1)
# → [[...]]
# Au lieu de [[[[[[... infiniment ]]]]]]

# Comparaisons avec références circulaires

infini_1 = [None]
infini_1[0] = infini_1 # l'élément pointe vers la liste elle-même
infini_1 == infini_1  # → True

# Comparaison avec objet similaire

infini_2 = [None]
infini_2[0] = infini_2

# ⚠️ Provoque une erreur
infini_1 == infini_2
# → RecursionError: maximum recursion depth exceeded in comparison

# Références circulaires dans structures complexes

# Collection de points
collection_de_points = [
    {'x': 10, 'y': 20},
    {'x': 30, 'y': 50},
]

# Ajouter une référence circulaire
for point in collection_de_points:
    point['points'] = collection_de_points
    # Chaque point référence maintenant toute la collection !

print(collection_de_points)
# → [{'x': 10, 'y': 20, 'points': [...]},
#    {'x': 30, 'y': 50, 'points': [...]}]

# Depuis un point, accéder à tous les autres points
point = collection_de_points[0]

# Accéder à tous les points de la collection
tous_les_points = point['points']

# Accéder à un autre point spécifique
autre_point = point['points'][1]



