# Algo : Créez une matrice n×n remplie de zéros.
# Début:
# créer une Matrice vide => Matrice = []
# pour chaque ligne(row) allant de 1 à n lignes:
#   créer la ligne dans la matrice (ligne vide)
#   pour chaque colonne(col) allant de 1 à n colonnes:
#       créer la colonne dans la ligne <=> générer une cellule(cell) vide
#       remplir la celluke par la valeur
# renvoyer la matrice de nxn remplie de 0
# Fin:

# Code de base
# def get_matrix(n, val):
#     matrix = []
#     for row in range(n):
#         matrix.append([])
#         for _ in range(n):
#             matrix[row].append(val)
#     return matrix


# print(get_matrix(3, 0))
# print(get_matrix(5, 0))


# Simplification avec une compréhension de liste
def get_matrix(n, val):
    return [[val for _ in range(n)] for _ in range(n)]


print(get_matrix(3, 0))
print(get_matrix(5, 0))
