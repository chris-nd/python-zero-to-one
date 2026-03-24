def unpacking(seq):
    liste = []
    for item in seq:
        if isinstance(item, tuple):
            liste.extend(unpacking(item))
        else:
            liste.append(item)

    return tuple(liste)

print(unpacking((1, (2, 3), (4, (5, 6)))))
