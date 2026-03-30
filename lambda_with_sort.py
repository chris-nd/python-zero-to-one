import operator
coords = [(43, 7), (46, -7), (46, 0)]

# A. Via lambda
coords.sort(key=lambda x: x[1])
print(coords) # [(46, -7), (46, 0), (43, 7)]

# B. Via itemgetter (plus rapide)
coords.sort(key=operator.itemgetter(1))
print(coords) # [(46, -7), (46, 0), (43, 7)]