def readContentFile(f):
    with open(f, encoding="utf-8") as fl:
        return fl.read()

print(readContentFile("Exercices/Fichiers/fichier_11_2.txt"))