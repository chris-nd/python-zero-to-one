"Variables et attributs"

# Variable globale
a = 1

class C:
    # Variable de classe qui est accessible par
    # référencement de la classe ou d'objet de la classe
    a = 2

    def f(self):
        # Variable accessible via la règle LEGB
        print(a)
        # Variable accessible par référence d'objet
        # en utilisant le mécanisme de la résolution
        # d'attribut le long de l'arbre d'héritage
        # selon la MRO
        print(C.a)

ins = C()
ins.f()
