"""Introduction aux classes"""

class Phrase:
    "Création d'un type objet phrase"
    def __init__(self, phrase):
        self.mots = phrase.split()

    def upper(self):
        "Met tous les mots en majuscules"
        self.mots = [mot.upper() for mot in self.mots]

    def __str__(self):
        return "\n".join(self.mots)


p = Phrase("je suis entrain de suivre un mooc sur python")

print(p.mots)

print(p)

# Affichage des attributs de l'objet présent dans
# l'espace de nommage à l'aide de l'attribut spécial (dunder) __dict___
print(f"{Phrase.__dict__}\n")
print(f"{p.__dict__}\n")

# Affichage des attributs de l'objet présent dans l'espace de nommage
# à l'aide de la fonction builtin vars()
print(f"{vars(Phrase)}\n")
print(f"{vars(p)}\n")


class Matrix:
    "Implémentation d'une matrice carrée 2x2"

    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def determinant(self):
        "Renvoie le déterminant de la matrice"
        return self.a11 * self.a22 - self.a12 * self.a21

matrice = Matrix(1, 2, 2, 1)
print(matrice) # <__main__.Matrix object at 0x...>
print(f"Le déterminant de la matrice est : {matrice.determinant()}") #  Le déterminant de la matrice est : -3


class Matrix2:
    """Une deuxième implémentation, tout aussi
    sommaire, mais différente, de matrice carrée 2x2"""

    def __init__(self, a11, a12, a21, a22):
        "construit une matrice à partir des 4 coefficients"
        # on décide d'utiliser un tuple plutôt que de ranger
        # les coefficients individuellement
        self.a = (a11, a12, a21, a22)

    def determinant(self):
        "le déterminant de la matrice"
        return self.a[0] * self.a[3] - self.a[1] * self.a[2]

    def __repr__(self):
        "comment présenter un objet matrice dans un print()"
        return f"<<mat-2x2 {self.a}>>"

matrice = Matrix2(1, 2, 2, 1)
print("Determinant =", matrice.determinant())
print(matrice)


# Implémentation d'un enregistrement sous formme d'instance de classe

pierre = {
    "nom": "pierre",
    "age": 25,
    "email": "pierre@foo.com"
}

print(pierre, "\n")

class Person:
    "Crée une instance de la classe Person"

    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    def __repr__(self):
        "Renvoie une chaîne de caractères avec les informations de la personne sous forme canonique"
        return f"<<{self.nom}, {self.age} ans, email:{self.email}>>"

    def __str__(self):
        "Comment présenter une chaîne de caractères via la sortie standard avec print()"
        return f"Mon nom est {self.nom}, j'ai {self.age} ans, et mon email est {self.email}"

# Liste de personnes créer à partir de la classe Person
personnes = [
    Person("pierre", 25, "pierre@foo.com"),
    Person("marie", 30, "marie@foo.com"),
    Person("jean", 35, "jean@foo.com")
]

for personne in personnes:
    print(personne)
    print(repr(personne), "\b\n")

contacts = {personne.nom: personne for personne in personnes}

print(contacts)

print(contacts["pierre"])

# L'ajout d'attribut de méthode à un objet après implémentation

def sendmail(self, subject, body):
    "Envoie un email à la personne"
    print(f"Envoi d'un email à {self.email}")
    print(f"Sujet: {subject}")
    print(f"Message: {body}")

Person.sendmail = sendmail

contacts["pierre"].sendmail("Coucou", "Salut, comment ça va ?")

employee = Person("employé", 40, "employe@foo.com")

def call(self, phone_number):
    "Appelle la personne"
    print(f"Appel en cours vers {phone_number}")

Person.call = call
employee.call("123-456-7890")
