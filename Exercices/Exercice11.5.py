def addText(text, filePath):
    with open(filePath, "a", encoding="utf8") as f:
        f.write("\n" + text)

addText("Nouveau texte ajouté !", "Exercices/Fichiers/fichier_11_5.txt")