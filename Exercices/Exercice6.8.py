def rotate_circle(l, r):
    for _ in range(r):
        l.insert(0, l.pop())
    return l

print(rotate_circle([1, 2, 3, 4, 5], 2))

# Approche optimisée
# def rotate_circle(l, r):
#     if not l:
#         return l
    
#     r = r % len(l)  # Optimisation importante
#     return l[-r:] + l[:-r]

# print(rotate_circle([1, 2, 3, 4, 5], 2))     # [4, 5, 1, 2, 3]
# print(rotate_circle([1, 2, 3, 4, 5], 1000))  # Instantané !