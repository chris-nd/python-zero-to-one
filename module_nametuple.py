"Implementation d'un tuple nommé"

import sys
from collections import namedtuple


p1 = dict(x=1, y=2)
print("\np1:", p1)

p2 = dict([("x", 3), ("y", 4)])
print("\np2:", p2)

class Point:
    "Implementation d'un type objet Point"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"(x={self.x}, y={self.y})"

p3 = Point(5, 6)
print("\np3:", p3)

# Réécriture sous forme de tuple nommé

# En faisant ceci, le nom de la sous-classe d'objet tuple créée
# avec namedtuple est "Point" et utilise un nom de référence différent
TuplePoint = namedtuple("Points", ["x", "y"])

print("\nType de TuplePoint:", type(TuplePoint))
print("Nom de la sous-classe d'objet tuple créée avec namedtuple est:", TuplePoint.__name__)

# En faisant ceci, le nom de la sous-classe d'objet tuple créée avec
# namedtuple est "Points" et utilise un nom de référence identique.
# Il est préférable d'utiliser le même nom pour la classe et la référence
Points = namedtuple("Points", ["x", "y"])

print("\nType de Points:", type(Points))
print("Nom de la sous-classe d'objet tuple créée avec namedtuple est:", Points.__name__)

p4 = Points(7, 8)

print("\nEst ce que `Points` est un type? =>", "OUI" if isinstance(Points, type) else "NON")
print("Est ce que `p4` est un type? =>", "OUI" if isinstance(p4, type) else "NON")
print("Est ce que `p4` est un tuple? =>", "OUI" if isinstance(p4, tuple) else "NON")
print("\nTuplePoint:", p4)

# Accéder aux champs ou attrubits de la sous classe TuplePoint
print("\nAccès aux champs par index:")
print("p4[0] =", p4[0])
print("p4[1] =", p4[1])
print("\nAccès aux champs par nom:")
print("p4.x =", p4.x)
print("p4.y =", p4.y)

# l'objet p4 est immutable, donc on ne peut pas le modifier après sa création étant une
# instance d'une sous classe objet TuplePoint ayant hérité de la classe objet tuple
try:
    p4.x = 10
    p4.y = 12
except AttributeError as e:
    print("Erreur:", e)


# Coût mémoire de la création d'un objet point
# à l'aide d'un dict(record), une classe ou un nametuple

print("\nCoût mémoire:")
print(f"p1(dict): {sys.getsizeof(p1)/1024:.2f}Ko") # p1(dict): 0.18Ko
print(f"p2(dict): {sys.getsizeof(p2)/1024:.2f}Ko") # p2(dict): 0.18Ko
print(f"p3(class): {sys.getsizeof(p3)/1024:.2f}Ko") # p3(class): 0.05Ko
print(f"p4(namedtuple): {sys.getsizeof(p4)/1024:.2f}Ko") # p4(namedtuple): 0.06Ko

# Redéfinir certaines méthodes spéciales d'une
# sous classe tuple créer à l'aide de namedtuple

class Point2(namedtuple("Point2", ["x", "y"])):
    "Implémentation de l'héritage de la classe namedtuple"

    def __init__(self, x, y):
        super().__init__(x, y)

    def __eq__(self, other):
        if not isinstance(other, Point2):
            return False
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self) -> int:
        # Le hash des objet de type Point2 dépendra des attributs x et y
        return hash((self.x, self.y))
