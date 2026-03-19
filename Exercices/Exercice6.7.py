def sublist(liste, n):
    sublist = []
    for i in range(0, len(liste), n):
        sublist.append(liste[i:i+n])
    return sublist

print(sublist([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

# Approche pythonique
# def sublist(liste, n):
#     return [liste[i:i+n] for i in range(0, len(liste), n)]

# print(sublist([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))