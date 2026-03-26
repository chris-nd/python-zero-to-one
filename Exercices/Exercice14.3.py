def merge(dic1, dic2):
    liste = []
    for item in dic1.items():
        liste.append(item)
    for item in dic2.items():
        liste.append(item)
    return dict(liste)

print(merge({"a": 1, "b": 2}, {"c": 3, "d": 4}))

# Les approches pythoniques
# 2ème approche
# def merge_update(dic1, dic2):
#     resultat = dic1.copy() # On copie pour ne pas modifier l'original
#     resultat.update(dic2)
#     return resultat

# print(merge({"a": 1, "b": 2}, {"c": 3, "d": 4}))

# 3ème approche
# def merge_unpack(dic1, dic2):
#     return {**dic1, **dic2}

# print(merge({"a": 1, "b": 2}, {"c": 3, "d": 4}))

# 4ème approche
# def merge_modern(dic1, dic2):
#     return dic1 | dic2

# print(merge({"a": 1, "b": 2}, {"c": 3, "d": 4}))