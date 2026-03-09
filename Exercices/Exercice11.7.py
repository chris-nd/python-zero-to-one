def numLine(filePath):
    with open(filePath, encoding="UTF-8") as flp:
        for line, text in enumerate(flp.readlines()):
            print(f"{line + 1} - {text}", end="")

numLine("Exercices/Fichiers/fichier_11_7.txt")

# 2ème approche pythonique
# def numLine(filePath):
#     with open(filePath, encoding="UTF-8") as flp:
#         for line, text in enumerate(flp, start=1):
#             print(f"{line} - {text.split()}")

# numLine("Exercices/Fichiers/fichier_11_7.txt")