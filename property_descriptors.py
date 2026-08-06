" Contrôle d'accès et de modification d'attributs "

class Maison:
    def __init__(self, t):
        self._temperature = t

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, t):
        if 5 < t and t < 25:
            self._temperature = t
            return
        raise TemperatureError()

    # Implémentation de property
    temperature = property(get_temperature, set_temperature)


class TemperatureError(Exception):
    pass

maison = Maison(18)
print(maison.get_temperature())
maison.set_temperature(22)
print(maison.get_temperature())
maison.set_temperature(28)
try:
    print(maison.get_temperature())
except TemperatureError as e:
    print("Température invalide", e)

# Property
# C'est une manière de définir des attributs avec un accès contrôlé

maison2 = Maison(18)
print(maison2.temperature)
maison2.temperature = 22
print(maison2.temperature)
maison2.temperature = 28
try:
    print(maison2.temperature)
except TemperatureError as e:
    print("Température invalide", e)

# Descripteurs (protocol de descripteur)
# C'est une classe qui implémente 
# les méthodes spéciales __get__ et __set__

class Temperature2:
    def __get__(self, inst, instype):
        return inst._temperature

    def __set__(self, inst, t):
        if 5 < t and t < 25:
            inst._temperature = t
            return
        raise TemperatureError2()

class TemperatureError2(Exception):
    pass

class Maison2:

    def __init__(self, t):
        self.temperature = t

    temperature = Temperature2()

maison3 = Maison2(18)
print(maison3.temperature)
maison3.temperature = 22
print(maison3.temperature)
maison3.temperature = 28
try:
    print(maison3.temperature)
except TemperatureError2 as e:
    print("Température invalide", e)
