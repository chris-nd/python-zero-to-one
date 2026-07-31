"Implementation d'une énumération"

from enum import Enum, IntEnum

class Flavour(Enum):
    "Implémentation d'un objet type Enum(Flavour) pour les parfums de glace"
    VANILLA = 1
    CHOCOLATE = 2
    STRAWBERRY = 3

vanilla = Flavour.VANILLA
chocolate = Flavour["CHOCOLATE"]
strawberry = Flavour["STRAWBERRY"]

print("Parfums de glace :")
print(f"- {vanilla.name}: {vanilla.value}")
print(vanilla)
print(repr(vanilla))
print(Flavour(1))

print(f"\n- {chocolate.name}: {chocolate.value}")
print(chocolate)
print(repr(chocolate))
print(Flavour(2))

print(f"\n- {strawberry.name}: {strawberry.value}")
print(strawberry)
print(repr(strawberry))
print(Flavour(3))

class HttpError(IntEnum):
    "Implémentation d'un objet type IntEnum(HttpError) pour les codes d'erreur HTTP"
    OK = 200
    REDIRECT = 301
    REDIRECT_TMP = 302
    NOT_FOUND = 404
    INTERNAL_ERROR = 500

    # avec un IntEnum on peut faire des comparaisons
    def is_redirect(self):
        "Renvoie True si le code d'erreur est une redirrection"
        return 300 <= self.value <= 399

code = HttpError.REDIRECT_TMP
print(
    f"Le code {code.value} est une redirection"
    if code.is_redirect() else f"Le code {code.value} n'est pas une redirection"
)

# Les énumérations sont itérables
class Couleur(IntEnum):
    "Implémentation d'un objet type IntEnum(Couleur) pour les couleurs de cartes"
    TREFLE = 0
    CARREAU = 1
    COEUR = 2
    PIQUE = 3

    def glyph(self):
        "Renvoie le symbole Unicode pour la couleur de carte"
        glyphs = {
            Couleur.TREFLE: '\u2663',
            Couleur.CARREAU: '\x1b[31;1m\u2666\x1b[39;0m',
            Couleur.COEUR: '\x1b[31;1m\u2665\x1b[39;0m',
            Couleur.PIQUE: '\u2660',
        }
        return glyphs[self]

for couleur in Couleur:
    print(f"Couleur {couleur} -> {couleur.glyph()}")
