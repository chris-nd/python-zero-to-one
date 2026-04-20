from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict, astuple

# Les Classes
class Chien:
    name = "Milou"

    def aboyer(self):
        print(f"Le chien {self.name} aboie")

chien = Chien()
chien.aboyer()

# Classe avec fonction d'initialisation (Constructeur)
class Cours:
    "Classe d'assistance pour la gestion des cours"
    def __init__(self, titre: str, etudiants: int, duree: float):
        self.titre = titre
        self.etudiants = etudiants
        self.duree = duree

    def afficher_info(self):
        "Affiche les informations sur le cours"
        print(f"Titre : {self.titre}")
        print(f"Etudiants : {self.etudiants}")
        print(f"Temps : {self.duree}min")

    def ajouter_etudiant(self):
        "Ajoute un nouvel étudiant"
        self.etudiants += 1

cours1 = Cours("Apprendre la POO avec Python", 1, 90)
cours1.afficher_info()

# Encapsulation
cours1.etudiants = -50 # N'a pas de sens et cun contrôle d'accès aux données (états)

class CoursEncapsulation:
    "Classe d'assistance pour la gestion des cours"
    def __init__(self, titre: str, etudiants: int, duree: float):
        self.titre = titre
        self.etudiants = etudiants
        self.duree = duree
        self._protege = 10
        self.__prive = 15

    def afficher_info(self):
        "Affiche les informations sur le cours"
        print(f"Titre : {self.titre}")
        print(f"Etudiants : {self.etudiants}")
        print(f"Temps : {self.duree}min")

    def ajouter_etudiant(self):
        "Ajoute un nouvel étudiant"
        self.etudiants += 1

cours2 = CoursEncapsulation("Apprendre la POO avec Python", 1, 90)
print(cours2._protege)

try:
    print(cours2.__prive)
except AttributeError as e:
    print(f"OOP: {e}")

print(cours2._CoursEncapsulation__prive)

# Getters & Setters
class CoursGettersSetters:
    "Classe d'assistance pour la gestion des cours"
    def __init__(self, titre: str, etudiants: int, duree: float):
        self.titre = titre
        self.__etudiants = etudiants
        self._duree = duree

    def get_etudiants(self):
        return self.__etudiants

    def set_etudiants(self, nombre):
        if nombre > 0:
            self.__etudiants = nombre
        else:
            raise ValueError("Le nombre doit être positive")

    def afficher_info(self):
        "Affiche les informations sur le cours"
        print(f"Titre : {self.titre}")
        print(f"Etudiants : {self.__etudiants}")
        print(f"Temps : {self._duree}min")


cours3 = CoursGettersSetters("Apprendre la POO avec Python", 1, 90)
print(cours3.get_etudiants())
print(cours3.set_etudiants(10))
print(cours3.get_etudiants())


# Property
class CoursProperty:
    "Classe d'assistance pour la gestion des cours"
    def __init__(self, titre: str, etudiants: int, duree: float):
        self.titre = titre
        self.__etudiants = etudiants
        self._duree = duree

    @property
    def etudiants(self):
        return self.__etudiants

    @etudiants.setter
    def etudiants(self, nombre):
        if nombre > 0:
            self.__etudiants += nombre
        else:
            raise ValueError("Le nombre doit être positive")

    def afficher_info(self):
        "Affiche les informations sur le cours"
        print(f"Titre : {self.titre}")
        print(f"Etudiants : {self.__etudiants}")
        print(f"Temps : {self._duree}min")


cours4 = CoursProperty("Apprendre la POO avec Python", 200, 90)
print(cours4.etudiants)
cours4.etudiants = 20
print(cours4.etudiants)


# L'héritage simple
class Employee:
    "Classe pour la création d'un employé"

    def __init__(self, name: str, salary: float):
        self._name = name
        self._salary = salary

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    name = property(_get_name, _set_name)

    def _get_salary(self):
        return self._salary

    def _set_salary(self, salary):
        self._salary = salary

    salary = property(_get_salary, _set_salary)

    def take_break(self):
        print(f"{self.name} part en pause")


alice = Employee("Alice", 3500)

print(alice.name)
print(alice.salary)
alice.take_break()

class Developer(Employee):
    def __init__(self, name: str, salary: float, code_editor: str):
        super().__init__(name, salary)
        self.code_editor = code_editor

    def to_code(self):
        print(f"{self.name} code")


class GraphycDesigner(Employee):
    def __init__(self, name: str, salary: float, design_software: str):
        super().__init__(name, salary)
        self.design_software = design_software

    def to_design(self):
        print(f"{self.name} crée")

bob = Developer("Bob", 50_000, "Vs Code")
charlie = GraphycDesigner("Charlie", 50_000, "Figma")

print(bob.name)
print(bob.salary)
print(bob.code_editor)
bob.to_code()

print(charlie.name)
print(charlie.salary)
print(charlie.design_software)
charlie.to_design()


# L'héritage multiple
class DevFrontEnd:
    def to_code(self):
        print("le Dev Frontend code")

class DevBackEnd:
    def to_code(self):
        print("le Dev Backend code")

class DevFullStack(DevFrontEnd, DevBackEnd):
    def to_code(self):
        print("le Dev Fullstack code")

chris = DevFullStack()
chris.to_code()


# Le polymorphisme
class Animal():
    def parler(self):
        pass

class Dog(Animal):
    def parler(self):
        return "Waf Waf"

class Chat(Animal):
    def parler(self):
        return "Miaou"

animaux = [Dog(), Chat()]

for animal in animaux:
    print(animal.parler())


# L'abstraction
class Forme(ABC):

    @abstractmethod
    def surface(self):
        pass

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        super().__init__()
        self.longueur = longueur
        self.largeur = largeur

    def surface(self):
        return self.longueur * self.largeur

rectangle = Rectangle(10, 6)
print(rectangle.longueur)
print(rectangle.largeur)
print(rectangle.surface())

class MethodePaiement(ABC):
    @abstractmethod
    def payer(self):
        pass

class CarteCredit(MethodePaiement):
    def payer(self, montant):
        print(f"Paiement {montant} par carte")

class PayPal(MethodePaiement):
    def payer(self, montant):
        print(f"Paiement {montant} par paypal")

class Crypto(MethodePaiement):
    def payer(self, montant):
        print(f"Paiement {montant} par crypto")

paiements = [CarteCredit(), PayPal(), Crypto()]

for paiement in paiements:
    paiement.payer(1000)


# La composition
# Quand l'héritage parait trop rigide ou pas pertinent
class Appareil:
    pass

class Smartphone(Appareil):
    # Un smartphone est un appareil
    pass

class Ordinateur(Appareil):
    # Un smartphone est un appareil
    def __init__(self):
        super().__init__()
        # Un clavier un composant d'un ordinateur ou
        # Un ordinateur à un clavier
        self.clavier = Clavier()

class Clavier:
    pass


class Moteur:
    def demarrer(self):
        print("Le moteur demarre")

class Voiture:
    def __init__(self):
        self.moteur = Moteur()

    def rouler(self):
        self.moteur.demarrer()
        print("La voiture roule")

voiture = Voiture()
voiture.rouler()

class Adresse:
    def __init__(self, rue, ville):
        self.rue = rue
        self.ville = ville

    def afficher(self):
        return f"{self.rue}, {self.ville}"

class Utilisateur:
    def __init__(self, name, adresse):
        self.name = name
        self.adresse = adresse

    def afficher_infos(self):
        print(f"Utilisateur : {self.name}, Addresse : {self.adresse.afficher()}")

adresse = Adresse("5 rue Blanche", "Soisy-sous-montmorency")
user = Utilisateur("Chris", adresse)
user.afficher_infos()

# DUNDERS(Méthodes Spéciale)
class Livre:
    def __init__(self, titre, auteur):
        self.titre, self.auteur = titre, auteur

    def __str__(self):
        return f"{self.titre} de {self.auteur}"

    def __repr__(self):
        return f"Livre(titre='{self.titre}', auteur='{self.auteur}')"

livre = Livre("1984", "George Orwell")
print(livre)
print(repr(livre))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vecteur(self.x + other.x, self.y + other.y)

    # def __str__(self):
    #     return f"x = {self.x}, y = {self.y}"

    def __repr__(self):
        return f"Vecteur(x={self.x}, y={self.y})"

v1 = Vecteur(1, 2)
v2 = Vecteur(3, 4)

print(v1 + v2)

class MaListe:
    def __init__(self, donnees):
        self.donnees = donnees

    def __len__(self):
        return len(self.donnees)
    
    def __getitem__(self, key):
        return self.donnees[key]

liste = MaListe([1, 2, 3, 4, 5])
print(len(liste))
print(liste[2])


# Les dataclasses
class Joueur:
    def __init__(self, nom, numero_maillot):
        self.nom = nom
        self.numero_maillot = numero_maillot

joueur = Joueur("Ronaldo", 7)
print(joueur.nom)
print(joueur.numero_maillot)
print(joueur)

@dataclass
class Player:
    nom: str
    numero_maillot: int

player = Player("Messi", 10)
print(player.nom)
print(player.numero_maillot)
print(player)
print(type(p1))


@dataclass()
class Book:
    titre: str
    auteur: str

book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")

print(book1 == book2)
print(asdict(book1))
print(astuple(book2))
