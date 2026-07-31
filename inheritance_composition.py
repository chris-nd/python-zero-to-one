"Implémentation de la relation d'héritage et de composition"

class Tige:
    "Implémentation d'un type objet Tige"
    def implicite(self):
        "Méthode  appelée implicitement depuis cette classe"
        print('Tige.implicite')
    def redefinie(self):
        "Méthode appelée lorsqu'elle est redéfinie dans une sous-classe"
        print('Tige.redefinie')
    def modifiee(self):
        "Méthode  appelée lorsqu'elle est modifiée(surchargée) dans une sous-classe"
        print('Tige.modifiee')

# La classe Rose utilise la classe Tige via la composition au lieu de l'héritage 
# parce que Rose n'est pas un type de Tige, mais une rose est composé d'une tige
class Rose:
    "Implémentation d'un type objet Rose"
    # Pour chaque objet de la classe Rose
    # on va créer un objet de la classe Tige
    # et le conserver dans un champ.
    def __init__(self):
        self.externe = Tige()

    # le reste est presque comme tout à l'heure
    # sauf qu'il faut definir implicite
    def implicite(self):
        "Méthode  appelée implicitement depuis cette classe"
        self.externe.implicite()

    # on redéfinit complètement redefinie
    def redefinie(self):
        "Méthode appelée lorsqu'elle est redéfinie dans une sous-classe"
        print('Rose.redefinie')

    def modifiee(self):
        "Méthode  appelée lorsqu'elle est modifiée(surchargée) dans une sous-classe"
        self.externe.modifiee()
        print('Rose.modifiee apres Tige')
