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