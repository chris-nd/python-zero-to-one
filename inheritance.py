class Animal:
    def __init__(self, name):
        self.name = name

class Mammifere(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

# pour créer un objet de type `Animal` (méthode __init__)
requin = Animal('requin')
# idem pour un Mammifere
baleine = Mammifere('baleine')

# bien sûr ici la réponse est 'True'
print("l'objet baleine est-il un mammifère ?", isinstance(baleine, Mammifere))

# ici c'est moins évident, mais la réponse est 'True' aussi
print("l'objet baleine est-il un animal ?", isinstance(baleine, Animal))

# Méthodes spéciales (dunders)

class Phrase:
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def nb_lettres(self):
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


class PhraseSansCasse(Phrase):
    def __init__(self, ma_phrase):
        self.mots_lower = {mot.lower() for mot in ma_phrase.split()}
        Phrase.__init__(self, ma_phrase)

    def __contains__(self, mot):
        return mot.lower() in self.mots_lower


p2 = PhraseSansCasse("Bonjour, le monde!")
print(p2) # Bonjour, le monde!
print("monde" in p2) # True
print("BONJOUR" in p2) # True
