def flat_list(liste):
    flat = []
    for l in liste:
        flat.extend(l)
    return flat

print(flat_list([[1, 2], [3, 4], [5, 6, 7]]))