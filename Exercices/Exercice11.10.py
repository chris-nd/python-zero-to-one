def reverseLineOrder(filePath):
    with open(filePath, encoding="utf8") as flp:
        content = flp.readlines()
    with open(filePath, "w", encoding="utf8") as flp:
        flp.writelines(reversed(content))

reverseLineOrder("Exercices/Fichiers/fichier_11_10.txt")

# Ma première approche
# def reverseLineOrder(filePath):
#     with open(filePath, encoding="utf8") as flp:
#         content = flp.read()
#     with open(filePath, "w", encoding="utf8") as f:
#         f.write("\n".join(content.split("\n")[::-1]))

# reverseLineOrder("Exercices/Fichiers/fichier_11_10.txt")