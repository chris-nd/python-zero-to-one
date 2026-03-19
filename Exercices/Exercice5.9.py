def rotatate_position(seq, k):
    Liste = []
    for n in seq[-k:]:
        Liste.append(n)
    for n in seq[:-k]:
        Liste.append(n)
    return Liste

print(rotatate_position([1, 2, 3, 4, 5], 2))

# Meilleur approche
# def rotatate_position(seq, k):
#     if not seq or k == 0:
#         return seq
    
#     k = k % len(seq)
    
#     return seq[-k:] + seq[:-k]

# print(rotatate_position([1, 2, 3, 4, 5], 2))