# def copyContent(f, copy):
#     content = []
#     with open(f, encoding="utf8") as fl:
#         content = fl.readlines()
#     with open(copy, "w", encoding="utf8") as fl:
#         for line in content:
#             fl.write(line)

# copyContent("Exercices/Fichiers/fichier_11_4.txt", "Exercices/Fichiers/copy_fichier_11_4.txt")

# 2ème approche
# def copyContent(source, copy):
#     with open(source, encoding="utf8") as src:
#         content = src.read()
#     with open(copy, "w", encoding="utf8") as destination:
#         destination.write(content)

# copyContent("Exercices/Fichiers/fichier_11_4.txt", "Exercices/Fichiers/copy_fichier_11_4.txt")

# 3ème approche
# def copyContent(source, copy):
#     with open(source, encoding="utf8") as src, \
#         open(copy, "w", encoding="utf8") as destination:
#         destination.write(src.read())

# copyContent("Exercices/Fichiers/fichier_11_4.txt", "Exercices/Fichiers/copy_fichier_11_4.txt")

# 4ème approche éfficace pour de grand fichier
# sans stocker en mémoire les lignes

def copyContent(source, copy):
    with open(source, encoding="utf8") as src, \
         open(copy, "w", encoding="utf8") as destination:
        for line in src:
            destination.write(line)

copyContent("Exercices/Fichiers/fichier_11_4.txt", "Exercices/Fichiers/copy_fichier_11_4.txt")