# def get_keys(dic1, dic2):
#     return [key for key in dic1.keys() if key in dic2]

# print(get_keys({"a": 1, "b": 2, "c": 3}, {"b": 5, "c": 6, "d": 7}))

# 2ème approche avec les opérateurs d'opération sur les ensembles
def get_keys(dic1, dic2):
    return dic1.keys() ^ dic2.keys()

print(get_keys({"a": 1, "b": 2, "c": 3}, {"b": 5, "c": 6, "d": 7}))