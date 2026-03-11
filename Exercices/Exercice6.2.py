def remove_item(liste, item):
    return [n for n in liste if n != item]

print(remove_item([1, 2, 3, 2, 4], 2))

# 2ème approche
# def remove_item(liste: list, item):
#     for _ in range(liste.count(item)):
#         if item in liste:
#             liste.remove(item)
#     return liste

# print(remove_item([1, 2, 3, 2, 4], 2))