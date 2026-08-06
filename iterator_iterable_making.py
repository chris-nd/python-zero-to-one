"Conception d'itérable et itérateur"

from collections.abc import Iterable, Iterator
import sys

s = "Je fais unMOOC sur Python"

# Implémentation d'un Itérateur qui ne
# peut être parcouru qu'une seule fois
class PhraseIterateur:
    "Classe objet de type Phrase qui est un itérateur"
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.mots:
            raise StopIteration
        return self.mots.pop(0)

# Application du protocole d'itération avec la boucle for
p1 = PhraseIterateur(s)
print("L'objet p1 est itérable :", isinstance(p1, Iterable))
print("L'objet p1 est un itérateur :", isinstance(p1, Iterator))
print("Les mots de la phrase sont :", [mot for mot in p1])

try:
    print("Deuxième itération :", [mot for mot in p1])
except StopIteration as e:
    print("Fin de l'itération:", e)

# Implementation d'un itérable qui
# peut être parcouru plusieurs fois
class PhraseIterable:
    "Classe objet de type Phrase qui est un itérable"
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def __iter__(self):
        return IterPhrase(self.mots)

class IterPhrase:
    "Classe objet de type IterPhrase qui est un itérateur"
    def __init__(self, mots):
        self.mots = mots[:]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.mots:
            raise StopIteration
        return self.mots.pop(0)

p2 = PhraseIterable(s)
print("\nL'objet p2 est itérable :", isinstance(p2, Iterable))
print("L'objet p2 est un itérateur :", isinstance(p2, Iterator))
print("Les mots de la phrase sont :", [mot for mot in p2])
print("Deuxième itération :", [mot for mot in p2])

# Implementation d'un itérable avec une fonction
# génératrice qui crée des itérateurs
class PhraseIterable2:
    "Classe objet de type Phrase qui est un itérable"
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def __iter__(self):
        for m in self.mots:
            yield m

p3 = PhraseIterable2(s)
print("\nL'objet p3 est itérable :", isinstance(p3, Iterable))
print("L'objet p3 est un itérateur :", isinstance(p3, Iterator))
print("Les mots de la phrase sont :", [mot for mot in p3])
print("Deuxième itération :", [mot for mot in p3])
print("Type de l'itérateur de p3 :", type(iter(p3)))

print("\nTaille de p1 :", sys.getsizeof(p1), "\bKo")
print("Taille de p2 :", sys.getsizeof(p2), "\bKo")
print("Taille de p3 :", sys.getsizeof(p3), "\bKo")
