"Création d'exceptions personnalisées"

s = "Je fais un MOOC sur Python"

class Phrase:
    "Classe objet de type Phrase"
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        if not ma_phrase:
            raise PhraseVideError("La phrase est vide", 0)
        self.mots = ma_phrase.split()

# Dans 99,9% des cas, la classe d'exception 
# personnalisée est vide, sans bloc de code
class PhraseVideError(Exception):
    "Exception levée lorsque la phrase est vide"
    pass

# e référence l'instance qui a levé l'exception.
# args fait référence aux arguments passés à l'objet exception
try:
    p = Phrase("")
except PhraseVideError as e:
    print("Erreur :", e)
    print(f"\n{e.args}")
