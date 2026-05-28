class Phrase:

    nb_i = 0

    def __init__(self):
        Phrase.nb_i += 1

    # Méthode statique
    @classmethod
    def num(cls):
        return cls.nb_i


class PhraseSansCase(Phrase):

    nb_i = 0

    def __init__(self):
        PhraseSansCase.nb_i += 1

    # Méthode statique
    @classmethod
    def num(cls):
        return f"PhraseSansCase {cls.nb_i}"
