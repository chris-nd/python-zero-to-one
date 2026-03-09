def even_list(list_1, list_2):
    return [str(item_1) + str(item_2) for item_1 in list_1 for item_2 in list_2]

print(even_list([1, 2, 3], ["a", "b"]))

# 2ème approche
# def even_list(list_1, list_2):
#     liste = []
#     for item_1 in list_1:
#          for item_2 in list_2:
#             liste.append(str(item_1) + str(item_2))
#     return liste

# print(even_list([1, 2, 3], ['a', 'b']))
