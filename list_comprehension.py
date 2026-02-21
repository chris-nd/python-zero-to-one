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