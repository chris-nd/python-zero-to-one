def cadrant(points):
    x , y = points
    if x == 0 and y == 0:
        return "Origine"
    elif x == 0:
        return "Sur l'axe Y"
    elif y == 0:
        return "Sur l'axe X"
    elif x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"
    elif x < 0 and y < 0:
        return "Q3"
    elif x > 0 and y < 0:
        return "Q4"

print(cadrant((3, 4)))
print(cadrant((-2, 5)))
print(cadrant((-3, -4)))
print(cadrant((5, -2)))
print(cadrant((0, 0)))
print(cadrant((0, 5)))