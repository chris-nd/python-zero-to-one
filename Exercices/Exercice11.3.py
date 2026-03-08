# def countLine(f):
#     line = 0
#     with open(f, encoding="utf8") as fl:
#         for _ in fl:
#             line += 1
#         return line
    
# print(countLine("Exercices/Fichiers/fichier_11_3.txt"))

# Une approche plus phytonique
def countLine(f):
    with open(f, encoding="utf8") as fl:
        return sum(1 for _ in fl)
    
print(countLine("Exercices/Fichiers/fichier_11_3.txt"))
