def reverse_dict(dic):
    keys = list(dic.keys())
    values = list(dic.values())

    return dict(zip(values, keys))

print(reverse_dict({"a": 1, "b": 2, "c": 3}))

# 2ème approche pythonique
# def reverse_dict_pro(dic):
#     return {valeur: cle for cle, valeur in dic.items()}

# print(reverse_dict({"a": 1, "b": 2, "c": 3}))