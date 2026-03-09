from random import shuffle, sample

def shuffleList(liste):
    shuffle(liste)
    return liste

print(shuffleList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 2èeme approche
# def shuffleList(liste):
#     return sample(liste, len(liste))

# print(shuffleList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))