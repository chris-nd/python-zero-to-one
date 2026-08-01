import builtins

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

# Exemple du fonctionnement de l'algorithme de `linéarisation` C3 de la MRO
# D B A Object C A Object
# D B Object C A Object
# D B C A Object

print(D.mro())
# [<class '__main__.D'>,
# <class '__main__.B'>,
# <class '__main__.C'>,
# <class '__main__.A'>,
# <class 'object'>]

class LeftTop:

    def attribut(self):
        return "attribut(LeftTop)"

class LeftMiddle(LeftTop):
    pass

class Left(LeftMiddle):
    pass

class Middle:
    pass

class Right:
    def attribut(self):
        return "attribut(Right)"

class Class(Left, Middle, Right):
    pass

instance = Class()

print("\nLe nom de la classe de l'instance 'instance' est :", instance.__class__)
print("\nLe nom de la classe 'Class' est :", Class.__name__)
print("\nLes classes de base de la classe 'Class' sont :", Class.__bases__)
print("\nLes classes de base de la classe parente de l'instance" \
      " 'instance' sont :", instance.__class__.__bases__)

# Class Left LeftMiddle LeftTop Object Middle Object Right Object
# Class Left LeftMiddle LeftTop Middle Right Object

print("\nL'ordre de résolution des méthodes est :", Class.mro(), "=>", instance.attribut())
print(instance.attribut() == "attribut(LeftTop)")
print(instance.attribut() == "attribut(Right)")

# Pour court-circuité la résolution d'attribus via la mro
class Class2(Left, Middle, Right):

    def attribut(self):
        return Right.attribut(self)

instance2 = Class2()
print(instance2.attribut())

O = object
class F1(O): pass
class E1(O): pass
class D1(O): pass
class C1(D1, F1): pass
class B1(E1, D1): pass
class A1(B1, C1): pass

print(A1.mro())

# Cas où la linéarisation C3 de la mro ne fonctionne pas
class X: pass
class Y: pass
class XY(X, Y): pass
class YX(Y, X): pass

# on essaie de créer une sous-classe de XY et YX
try:
    class Class3(XY, YX): pass 
# mais ce n'est pas possible
except Exception as e:
    print(f"OOPS, {type(e)}, {e}")


# La super classe object
print("builtins.object == object:", builtins.object == object)
