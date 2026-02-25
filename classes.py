class Phrase:
    
    def __init__(self, phrase):
        self.mots = phrase.split()

    def upper(self):
        self.mots = [mot.upper() for mot in self.mots]

    def __str__(self):
        return "\n".join(self.mots)


p = Phrase("je suis entrain de suivre un mooc sur python")

print(p.mots)

print(p)

