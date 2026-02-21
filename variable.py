# Variables et types de données en Python utilisant des affectations simples

texte = "Bonjour" # Ceci est une chaîne de caractères
nombre = 42 # Ceci est un entier
flottant = 3.14 # Ceci est un nombre à virgule flottante
booleen = True # Ceci est un booléen
liste = [1, 2, 3] # Ceci est une liste
tuple_exemple = (4, 5, 6) # Ceci est un tuple
ensemble = {7, 8, 9} # Ceci est un ensemble
dictionnaire = {'a': 1, 'b': 2} # Ceci est un dictionnaire

# Obtenir les identifiants uniques des variables
id(texte) # Obtenir l'identifiant unique de la variable texte
id(nombre) # Obtenir l'identifiant unique de la variable nombre
id(flottant) # Obtenir l'identifiant unique de la variable flottant
id(booleen) # Obtenir l'identifiant unique de la variable booleen
id(liste) # Obtenir l'identifiant unique de la variable liste
id(tuple_exemple) # Obtenir l'identifiant unique de la variable tuple_exemple
id(ensemble) # Obtenir l'identifiant unique de la variable ensemble
id(dictionnaire) # Obtenir l'identifiant unique de la variable dictionnaire

# Affectation multiple
a, b, c = 10, 20, 30 # Affectation multiple de valeurs aux variables a, b et c
print(a, b, c) # Afficher les valeurs de a, b et c

# Affectation parallèle
x = y = z = 100 # Affectation parallèle de la même valeur aux variables x, y et z
print(x, y, z) # Afficher les valeurs de x, y et z


# Les entiers entre -5 et 256 partagent le même identifiant unique
print(id(-5)) # Obtenir l'identifiant unique de la valeur entière -5
print(id(256)) # Obtenir l'identifiant unique de la valeur entière 256


# Les chaînes de caractères identiques partagent le même identifiant unique jusqu'à une 20 caractères
texte2 = "Bonjour"
print(id(texte2)) # Obtenir l'identifiant unique de la valeur flottante 3.14
print(id(texte)) # Obtenir l'identifiant unique de la variable texte2 (même valeur que texte)

print(id(None)) # Obtenir l'identifiant unique de la valeur None
print(id(True)) # Obtenir l'identifiant unique de la valeur booléenne True
print(id(False)) # Obtenir l'identifiant unique de la valeur booléenne False