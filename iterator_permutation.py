"Implémentation des permutations à l'aide de itertools"

from itertools import permutations

set_dt = {1, 2, 3}

print("Permutations of", permutations(set_dt))

for item in permutations(set_dt):
    print(item)

# Implémentation possible pour un itérateur de permutations
class Permutations:
    """
    Un itérateur qui énumère les permutations de n
    sous la forme d'une liste d'indices commençant à 0
    """
    def __init__(self, n):
        # le constructeur bien sûr ne fait (presque) rien
        self.n = n
        # au fur et à mesure des itérations
        # le compteur va aller de 0 à n-1
        # puis retour à 0 et comme ça en boucle sans fin
        self.counter = 0
        # on se contente d'allouer un iterateur de rang n-1
        # si bien qu'une fois qu'on a fini de construire
        # l'objet d'ordre n on a n objets Permutations en tout
        if n >= 2:
            self.subiterator = Permutations(n-1)

    # pour satisfaire le protocole d'itération
    def __iter__(self):
        return self

    # c'est ici bien sûr que se fait tout le travail
    def __next__(self):
        # pour n == 1
        # le travail est très simple
        if self.n == 1:
            # on doit renvoyer une fois la liste [0]
            # car les indices commencent à 0
            if self.counter == 0:
                self.counter += 1
                return [0]
            # et ensuite c'est terminé
            else:
                raise StopIteration

        # pour n >= 2
        # lorsque counter est nul,
        # on traite la permutation d'ordre n-1 suivante
        # si next() lève StopIteration on n'a qu'à laisser passer
        # car en effet c'est qu'on a terminé
        if self.counter == 0:
            self.subsequence = next(self.subiterator)
        #
        # on insère alors n-1 (car les indices commencent à 0)
        # successivement dans la sous-sequence
        #
        # naivement on écrirait
        # result = self.subsequence[0:self.counter] \
        #    + [self.n - 1] \
        #    + self.subsequence[self.counter:self.n-1]
        # mais c'est mettre le nombre le plus élevé en premier
        # et donc à itérer les permutations dans le mauvais ordre,
        # en commençant par la fin
        #
        # donc on fait plutôt une symétrie
        # pour insérer en commençant par la fin
        cutter = self.n-1 - self.counter
        result = self.subsequence[0:cutter] + [self.n - 1] \
                 + self.subsequence[cutter:self.n-1]
        # 
        # on n'oublie pas de maintenir le compteur et de
        # le remettre à zéro tous les n tours
        self.counter = (self.counter+1) % self.n
        return result

    # la longeur de cet itérateur est connue
    def __len__(self):
        import math
        return math.factorial(self.n)
