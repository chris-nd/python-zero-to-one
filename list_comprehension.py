# Créez une liste ne contenant que les nombres positifs

liste = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
nomnbres_positifs = [i for i in liste if i > 0]
print(nomnbres_positifs)

# Créez une liste contenant le double des nombres positifs
liste = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
nomnbres_positifs = [i * 2 for i in liste if i > 0]
print(nomnbres_positifs)

# Créez une liste contenant les nombres inversés
nombres = range(10)
nomnbres_inverse = [i if i % 2 == 0 else -i for i in nombres]
print(nomnbres_inverse)

# Compréhension :
[n + p for n in [2, 4] for p in [10, 20, 30]]

# Équivalent "bavard" :
resultat = []
for n in [2, 4]:          # 1er for
    for p in [10, 20, 30]: # 2ème for
        resultat.append(n + p)

print(resultat) # [12, 22, 32, 14, 24, 34]

# La compréhension "de compréhension" ([[... for ...] for ...])
n = 3
matrix = [[(i, j) for i in range(1, j + 1)] for j in range(1, n + 1)]
print(matrix)

# Équivalent "bavard" :
res_exterieur = []
for j in range(1, n + 1):     # On commence par le j (extérieur)
    res_interieur = []
    for i in range(1, j + 1): # Puis on remplit la sous-liste avec i
        res_interieur.append((i, j))
    res_exterieur.append(res_interieur)

print(res_exterieur)
