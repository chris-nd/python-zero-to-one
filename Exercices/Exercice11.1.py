def writeText(string):
    with open("Exercices/Fichiers/fichier_11_1.txt", "w", encoding="utf8") as f:
        f.write(string)
        
writeText("Hello, World!")