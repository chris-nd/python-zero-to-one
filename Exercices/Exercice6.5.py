def remove_occurence(liste):
    for i in liste:
        counter = liste.count(i)
        if counter >= 2:
            for _ in range(counter - 1):
                liste.remove(i)
    return liste

print(remove_occurence([1, 2, 2, 3, 4, 3, 5, 1]))