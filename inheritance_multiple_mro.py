class H:
    ...

h = H()
print(h.__class__) # <class '__main__.H'>
print(h.__bases__) # (<class 'object'>,)
print(type(h)) # <class '__main__.H'>

print(h) # <__main__.H object at 0x...>
print(H) # <class '__main__.H'>

print(H.mro()) # [<class '__main__.H'>, <class 'object'>]

# La résolution d'attribut
# en remontant l'arbre d'héritage
# basé sur la MRO (Method Resolution Order)

class SuperA: pass

class SuperB: pass

class child_C(SuperA, SuperB): pass

print(child_C.mro()) # [<class '__main__.child_C'>, <class '__main__.SuperA'>, <class '__main__.SuperB'>, <class 'object'>]

# Avec un arbre d'héritage reflétant un diagramme en diamant
# La remonté de l'arbre d'héritage se fait de bas en haut et de gauche à droite

class A: ...

class B(A): ...

class C(A): ...

class D(B, C): ...

print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
