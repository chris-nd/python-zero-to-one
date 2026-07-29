"""Parser des arguments en ligne de commande"""

from argparse import ArgumentParser


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

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("n", type=int, help="Entier pour lequel calculer le nombre de Fibonacci")
    args = parser.parse_args()
    print(fibonacci(args.n))
