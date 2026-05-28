class Phrase:
    nb_i = 0
    def __init__(self):
        Phrase.nb_i += 1
    # Méthode statique
    @staticmethod
    def num():
        return Phrase.nb_i


class PhraseSansCase(Phrase):

    nb_i = 0

    def __init__(self):
        PhraseSansCase.nb_i += 1
    # Méthode statique
    @staticmethod
    def num():
        return f"PhraseSansCase {Phrase.nb_i}"
