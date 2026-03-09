def countWord(filePath):
    with open(filePath, encoding="UTF8") as flp:
        return len(flp.read().split())

count = countWord("Exercices/Fichiers/fichier_11_6.txt")
print(f"il y'a {count} mot{"s" if count > 1 else ""} dans le fichier")