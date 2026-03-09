def replaceWord(filePath):

    with open(filePath, "r", encoding="utf8") as flpOld:
        old_file = flpOld.read()

    with open(filePath, "w", encoding="utf8") as flpNew:
        flpNew.write(old_file.replace("Python", "Java"))

replaceWord("Exercices/Fichiers/fichier_11_8.txt")

# 2ème approche
# def replaceWord(filePath):
#     with open(filePath, "r+", encoding="utf8") as flp:
#         content = flp.read()
#         flp.seek(0)
#         flp.write(content.replace("Python", "Java"))
#         flp.truncate()

# replaceWord("Exercices/Fichiers/fichier_11_8.txt")