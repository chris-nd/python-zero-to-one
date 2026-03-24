# 1ère approche moins sécurisée
def find_index(liste, number):
    return liste.index(number)

print(find_index((10, 20, 30, 40, 50), 30))

# 2ème approche pour plus de sécurité
# Rajouter une vérification rendre laa fonction plus robuste :
# def find_index(elements, number):
#     if number in elements:
#         return elements.index(number)
#     else:
#         return -1  # Ou un message d'erreur personnalisé