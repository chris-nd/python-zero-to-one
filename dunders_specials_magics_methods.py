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
