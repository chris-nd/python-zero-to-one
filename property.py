"Implémentation des properties"

class Temperature1:
    "Implémentation simple d'un type objet température1 en kelvin"
    def __init__(self, kelvin):
        self.kelvin = kelvin


    def __repr__(self):
        return f"{self.kelvin}K"


t1 = Temperature1(20)
print(t1) # 20K
print(t1.kelvin) # 20


class Temperature2:
    """ 
    Implémentation d'un type objet température2 en kelvin 
    avec contrôle d'accès à la valeur via des getters et setters 
    """

    # Définition de la fonction d'initialisation: "constructeur"
    def __init__(self, kelvin):
        self.set_kelvin(kelvin)

    # Définition d'un mutateur: "setter"
    def set_kelvin(self, kelvin):
        "Modifie la valeur de la température en kelvin"
        self._kelvin = max(0, kelvin)


    # Défition d'un accesseur: "Getter"
    def get_kelvin(self):
        "Renvoie la valeur de la température en kelvin"
        return self._kelvin

    # Redéfinition de la repésentation des types objets temperature2
    def __repr__(self):
        return f"{self._kelvin}K"


t2 = Temperature2(-30)
print(t2) # 0K
print(t2.get_kelvin()) # 0


# Implémentation phytonique
class Temperature3:
    """
    Implémentation d'un type objet température3 en kelvin avec 
    contrôle d'accès à la valeur via des getters et setters privé 
    """
    def __init__(self, kelvin):
        self.kelvin = kelvin

    # je définis bel et bien mes accesseurs de type getter et setter
    # mais _get_kelvin commence avec un _
    # car il n'est pas censé être appelé par l'extérieur
    def _get_kelvin(self):
        return self._kelvin

    # idem
    def _set_kelvin(self, kelvin):
        self._kelvin = max(0, kelvin)

    # une fois que j'ai ces deux éléments je peux créer une property
    kelvin = property(_get_kelvin, _set_kelvin)

    # et toujours la façon d'imprimer
    def __repr__(self):
        return f"{self._kelvin}K"


t3 = Temperature3(200)
print(t3) # 200K
print(t3.kelvin) # 200
t3.kelvin = -30
print(t3) # 0K
print(t3.kelvin) # 0


class Temperature:
    """
    Implémentation d'un type objet température 
    en kelvin avec un mécanisme de properties
    """
    ## les constantes de conversion
    # kelvin / celsius
    K = 273.16
    # fahrenheit / celsius
    RF = 5 / 9
    KF = (K / RF) - 32

    def __init__(self, kelvin=None, celsius=None, fahrenheit=None):
        """
        Création à partir de n'importe quelle unité
        Il faut préciser exactement une des trois unités
        """
        # on passe par les properties pour initialiser
        if kelvin is not None:
            self.kelvin = kelvin
        elif celsius is not None:
            self.celsius = celsius
        elif fahrenheit is not None:
            self.fahrenheit = fahrenheit
        else:
            self.kelvin = 0
            raise ValueError("need to specify at least one unit")

    # pour le confort
    def __repr__(self):
        return f"<{self.kelvin:g}K == {self.celsius:g}℃ " \
               f"== {self.fahrenheit:g}F>"

    def __str__(self):
        return f"{self.kelvin:g}K"

    # Getter
    def _get_kelvin(self):
        return self._kelvin

    # Setter
    # l'attribut 'kelvin' n'a pas de conversion à faire,
    # mais il vérifie que la valeur est positive
    def _set_kelvin(self, kelvin):
        # Validation de donnée
        if kelvin < 0:
            raise ValueError(f"Kelvin {kelvin} must be positive")
        self._kelvin = kelvin

    # la property qui définit l'attribut `kelvin`
    kelvin = property(_get_kelvin, _set_kelvin)


    # les deux autres properties font la conversion, puis
    # sous-traitent à la property kelvin pour le contrôle de borne
    def _set_celsius(self, celsius):
        # using .kelvin instead of ._kelvin to enforce
        self.kelvin = celsius + self.K

    def _get_celsius(self):
        return self._kelvin - self.K

    celsius = property(_get_celsius, _set_celsius)

    def _set_fahrenheit(self, fahrenheit):
        # using .kelvin instead of ._kelvin to enforce
        self.kelvin = (fahrenheit + self.KF) * self.RF

    def _get_fahrenheit(self):
        return self._kelvin / self.RF - self.KF

    fahrenheit = property(_get_fahrenheit, _set_fahrenheit)


t = Temperature(celsius=0)
print(t) # <0K == 0℃ == 32F>
print(t.fahrenheit) # 32
t.celsius += 100
print(t) # <100K == 100℃ == 212F>

try:
    t = Temperature(fahrenheit = -1000)
except ValueError as e:
    print(f"OOPS, {type(e)}, {e}")


# comme on n'a pas défini de deleter, on ne peut pas faire ceci
try:
    del t.kelvin
except ValueError as e:
    print(f"OOPS, {type(e)}, {e}")
