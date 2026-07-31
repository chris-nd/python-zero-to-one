from dataclasses import dataclass

@dataclass
class Contact:
    """
    Implémentation d'une classe de données pour modéliser
    la représentation d'objet de type Contact
    """

    nom: str
    prenom: str
    age: int
    email: str

contact1 = Contact(nom="Doe", prenom="John", age=30, email="john.doe@example.com")
contact2 = Contact(nom="Smith", prenom="Jane", age=25, email="jane.smith@example.com")

print(contact1)
print(contact2)

# L'ajout explicite de (repr=False) indique que la fonction builtin repr a été redéfini
# et que la classe de données ne génère pas automatiquement sa représentation en chaîne
@dataclass(repr=False)
class Personne:
    """
    Implémentation d'une classe de données pour modéliser
    la représentation d'objet de type Personne
    """

    nom: str
    age: int
    telephone: str

    # Surchage de méthodes spéciales(dunder methods)

    def __repr__(self):
        return f"nom='{self.nom}', age={self.age}, telephone='{self.telephone}')"


personne1 = Personne(nom="Doe", age=30, telephone="123-456-7890")
personne2 = Personne(nom="Smith", age=25, telephone="098-765-4321")

print("\n", personne1, sep="")
print(personne2)

# Création d'instance immuable avec dataclass
@dataclass(frozen=True)
class Point:
    """
    Implémentation d'une classe de données immuable pour 
    modéliser la représentation d'objet de type Point
    """
    x: float
    y: float

p1, p2, p3 = Point(1, 1), Point(1, 1), Point(1, 1)

print(p1)
print(p2)

s = {p1, p2}
print(len(s))
print(p3 in s)

try:
    p1.x = 2
    p1.y = 3.2
except Exception as e:
    print(f"Erreur : {e}")
