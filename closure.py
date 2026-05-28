# Une variable libre en python est une variable qui est ni local ni gloabal,
# ce qui en fait une variable englobante

# Les closures(fonctions de fermeture ou de clôture) en python
# sont des fonctions qui référence des variables libres

def plus_n(y):
    def closure(x):
        return x + y
    return closure

plus3 = plus_n(3)
print(plus3(10))
print(plus_n(3)(10))

# __closure__ est un attribut(un tuple) de fonction
# qui contient des références vers des variables libres
print(plus3.__closure__) # Affiche la fermeture
print(plus3.__closure__[0].cell_contents) # Affiche le contenu de la variable libre
