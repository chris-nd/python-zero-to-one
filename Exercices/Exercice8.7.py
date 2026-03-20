def average(liste):
    if not liste:
        return 0
    
    total = 0

    for i in liste:
        total += i

    return total / len(liste)

print(average([1, 2, 3, 4, 5]))
print(average([10, 20, 30]))

# 2 ème approche
# def average(liste):
#     if not liste:
#         return 0
#     return sum(liste) / len(liste)

# print(average([1, 2, 3, 4, 5]))
# print(average([10, 20, 30]))