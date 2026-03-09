def word_size(liste):
    return [len(word) for word in liste.split()]

print(word_size("Python est un langage de programmation"))