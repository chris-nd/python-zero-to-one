def insert_item(liste: list, pos, item):
    liste.insert(pos, item)
    return liste

print(insert_item([1, 2, 4, 5], 2, 3))