class Phrase:
    ma_phrase = "Hello, world"

    def initiate(self, ma_phrase):
        self.ma_phrase = ma_phrase


p1 = Phrase() # Crée une instance de la classe Phrase

print(Phrase) # <class '__main__.Phrase'>
print(p1) # <__main__.Phrase object at 0x...>

print(Phrase.__dict__) # {'ma_phrase': 'Hello, world'}
print(vars(Phrase)) # {'ma_phrase': 'Hello, world'}
print(vars(p1)) # {}

print(p1.ma_phrase) # Hello, world
print(Phrase.ma_phrase) # Hello, world

Phrase.mots = Phrase.ma_phrase.split()
print(Phrase.mots) # ['Hello,', 'world']
print(p1.ma_phrase) # Hello, world

print(vars(Phrase)) # {'ma_phrase': 'Hello, world', 'mots': ['Hello,', 'world']}
print(vars(p1)) # {}

p2 = Phrase() # Crée une instance de la classe Phrase
p2.initiate("Good morning") # Initialise l'instance p2 avec la phrase "Good morning"

print(p2.ma_phrase) # Good morning
print(vars(p2)) # {'ma_phrase': 'Good morning'}

class Matrix2:
    "Une implémentation sommaire de matrice carrée 2x2"

    def __init__(self, a11, a12, a21, a22):
        "construit une matrice à partir des 4 coefficients"
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def determinant(self):
        "renvoie le déterminant de la matrice"
        return (self.a11 * self.a22) - (self.a12 * self.a21)


matrice = Matrix2(1, 2, 2, 1)
print(matrice) # <__main__.Matrix2 object at 0x...>
print(matrice.determinant()) # -3

class SecondMatrix2:
    """Une deuxième implémentation, tout aussi
    sommaire, mais différente, de matrice carrée 2x2"""

    def __init__(self, a11, a12, a21, a22):
        "construit une matrice à partir des 4 coefficients"
        # on décide d'utiliser un tuple plutôt que de ranger
        # les coefficients individuellement
        self.a = (a11, a12, a21, a22)

    def determinant(self):
        "le déterminant de la matrice"
        return (self.a[0] * self.a[3]) - (self.a[1] * self.a[2])

    def __repr__(self):
        "comment présenter une matrice dans un print()"
        return f"<<mat-2x2 {self.a}>>"


matrice2 = SecondMatrix2(1, 2, 2, 1)
print("Determinant =", matrice2.determinant())
print("Matrice =", matrice2)


class Personne:
    """Une personne possède un nom, un âge et une adresse e-mail"""

    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    def __repr__(self):
        # comme nous avons la chance de disposer de python-3.6
        # utilisons un f-string
        return f"<<{self.nom}, {self.age} ans, email:{self.email}>>"


personnes = [
    # on se fie à l'ordre des arguments dans le créateur
    Personne('pierre', 25, 'pierre@foo.com'),

    # ou bien on peut être explicite
    Personne(nom='paul', age=18, email='paul@bar.com'),

    # ou bien on mélange
    Personne('jacques', 52, email='jacques@cool.com'),
]
for personne in personnes:
    print(personne)

index_par_nom = {personne.nom: personne for personne in personnes}
pierre = index_par_nom['pierre']
print(pierre)


# pour une implémentation réelle voyez la bibliothèque smtplib
# https://docs.python.org/3/library/smtplib.html

def sendmail(self, subject, body):
    "Envoie un mail à la personne"
    print(f"To: {self.email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")


Personne.sendmail = sendmail
pierre.sendmail("Coucou", "Salut ça va ?")
