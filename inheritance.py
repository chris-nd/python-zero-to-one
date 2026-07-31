"Implémentation du concept d'héritance en Python"

from collections.abc import Iterable, Hashable

class Animal:
    "Implémentation d'un type objet animal"
    def __init__(self, name):
        self.name = name


# Héritage simple
class Mammifere(Animal):
    "Implémentation d'un type objet mammifère"
    def __init__(self, name):
        Animal.__init__(self, name)

# Instenciation d'un objet `requin`` de type `Animal`
requin = Animal('requin')

# Instenciation d'un objet `baleine`` de type `Mammifere`
baleine = Mammifere('baleine')

# Test
print("l'objet baleine est-il un mammifère ?", isinstance(baleine, Mammifere))
print("l'objet baleine est-il un animal ?", isinstance(baleine, Animal))


class Phrase:
    "Implémentation d'un type objet phrase"

    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def nb_lettres(self):
        "Renvoie le nombre de lettres dans la phrase"
        return len(self.ma_phrase)

    def __len__(self):
        return len(self.mots)

    def __contains__(self, mot):
        return mot in self.mots

    def __str__(self):
        return self.ma_phrase


p = Phrase("Bonjour, le monde!")
print(len(p)) # 3
print("monde" in p) # True
print(p) # Bonjour, le monde!


# Héritage simple
class PhraseSansCasse(Phrase):
    "Implémentation d'un type objet phrase-sans-casse"

    def __init__(self, ma_phrase):
        # soit comme ceci
        Phrase.__init__(self, ma_phrase)
        # soit comme cela
        # super().__init__(ma_phrase)
        self.mots_lower = {mot.lower() for mot in ma_phrase.split()}

    def __contains__(self, mot):
        return mot.lower() in self.mots_lower


p2 = PhraseSansCasse("Bonjour, le monde!")
print(p2) # Bonjour, le monde!
print("monde" in p2) # True
print("BONJOUR" in p2) # True

# Le type objet base ou classe parente d'une classe dérivé
print(PhraseSansCasse.__bases__) # (<class '__main__.Phrase'>,)
print(Phrase.__bases__) # (<class 'object'>,)
print(str.__bases__) # <class 'object'>
print(int.__bases__) # <class 'object'>
print(float.__bases__) # <class 'object'>
print(bool.__bases__) # <class 'int'>
print(range.__bases__) # <class 'object'>

# Équivalent de la surcharge en C++
print(isinstance('ab', Iterable))
print(isinstance([1, 2], Iterable))

# Un objet qui a des méthodes __iter__() et __next__() est considéré comme un itérable
class Foo:
    "Implémentation d'un itérable de type objet Foo"
    def __iter__(self):
        return self
    def __next__(self):
        return

foo = Foo()
isinstance(foo, Iterable)

print(tuple.__bases__)
print(isinstance (([1], [2]), Hashable))
