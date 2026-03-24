def calc(liste):
    if not liste:
        return "Liste vide"

    minimum = min(liste)
    maximum = max(liste)
    moyenne = sum(liste)/len(liste)

    return minimum, maximum, moyenne

print(calc([1, 2, 3, 4, 5]))