#!/usr/bin/env python3

from argparse import ArgumentParser

# Un shebang est une directive d'interpréteur dont la ligne
# commençe par #!, suivie du chemin vers l'interpréteur Python.

# Utilisé par le système d'exploitation pour savoir
# quel interpréteur utiliser pour exécuter le script

# Il est aussi appelé sha-bang, hashbang, hash-pling, pound-bang etc ...

# chmod +x shebang.py: Permet de modifier le mode d'accès au fichier
# et de lui attribuer les permissions d'exécution.
# <path>/shebang.py <arg> : Pour exécuter le script avec un argument 
# passer en ligne de commande.


def fibonacci(n):
    "retourne le nombre de fibonacci pour l'entier n"
    # pour les deux premières valeurs de n, on peut renvoyer n
    if n <= 1:
        return n
    # sinon on initialise f2 pour n-2 et f1 pour n-1
    f2, f1 = 0, 1
    # et on itère n-1 fois pour additionner
    for _ in range(2, n + 1):
        f2, f1 = f1, f1 + f2
    # le résultat est dans f1
    return f1

if "__main__" == __name__:
    parser = ArgumentParser()
    parser.add_argument("n", type=int, help="Le nombre de Fibonacci à calculer")
    args = parser.parse_args()
    print(fibonacci(args.n))
