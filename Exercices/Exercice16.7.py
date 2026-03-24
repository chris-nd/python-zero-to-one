def sort_tuple(seq):
    liste = []

    for value in seq:
        val = list(value)
        val.reverse()
        liste.append(val)
    liste.sort()

    for i, value in enumerate(liste):
        value.reverse()
        liste[i] = tuple(value)

    return liste

print(sort_tuple([("Alice", 25), ("Bob", 20), ("Charlie", 30)]))

# 2ème approche pythonique
# def sort_tuple(seq):
#     return sorted(seq, key=lambda x: x[1])

# print(sort_tuple([("Alice", 25), ("Bob", 20), ("Charlie", 30)]))