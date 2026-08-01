class H:
    ...

h = H()

# La variable d'attribut spéciale __class__ contient le nom du type
# de l'objet ou de la classe qui a permi l'instanciation de l'objet
print(h.__class__) # <class '__main__.H'>

# La variable d'attribut spéciale __bases__ contient la liste des 
# classes parentes ou classes de bases dans un tuple
print(H.__bases__) # (<class 'object'>,)


print(type(h)) # <class '__main__.H'>

print(h) # <__main__.H object at 0x...>
print(H) # <class '__main__.H'>

# La méthode mro() est celle utilisée, qui définit l'odre
# de résolution d'attribut le long de l'arbre d'héritage
print(H.mro()) # [<class '__main__.H'>, <class 'object'>]

# La résolution d'attribut
# en remontant l'arbre d'héritage
# est basé sur la MRO (Method Resolution Order)

class SuperA: pass

class SuperB: pass

class child_C(SuperA, SuperB): pass

class child_D(SuperB, SuperA): pass

# L'ordre de résolution d'attribut par MRO dépend
# de l'ordre de déclaration des classes parentes
# dans la déclaration(signature ou prototype)
# de la classe fille

print(child_C.mro())
# [<class '__main__.child_C'>,
# <class '__main__.SuperA'>,
# <class '__main__.SuperB'>,
# <class 'object'>]

print(child_D.mro())
# [<class '__main__.child_D'>,
# <class '__main__.SuperB'>,
# <class '__main__.SuperA'>,
# <class 'object'>]

# Avec un arbre d'héritage reflétant un diagramme en diamant
# La remonté de l'arbre d'héritage se fait de bas en haut et de gauche à droite

class A: ...

class B(A): ...

class C(A): ...

class D(B, C): ...

# Exemple du fonctionnement de l'algorithme MRO
# D B A Object C A Object
# D B Object C A Object
# D B C A Object

print(D.mro())
# [<class '__main__.D'>,
# <class '__main__.B'>,
# <class '__main__.C'>,
# <class '__main__.A'>,
# <class 'object'>]
