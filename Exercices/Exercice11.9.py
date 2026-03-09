def mergeFile(sources, destination):
    for src in sources:
        with open(src, encoding="utf8") as source,\
            open(destination, "a", encoding="utf8") as newFile:
            newFile.write(source.read() + "\n")

files = ("Exercices/Fichiers/fichier_11_9_1.txt",
         "Exercices/Fichiers/fichier_11_9_2.txt",
         "Exercices/Fichiers/fichier_11_9_3.txt",)

newFile = "Exercices/Fichiers/fichier_11_9.txt"

mergeFile(files, newFile)
