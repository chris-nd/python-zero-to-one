# 1ère approche
def concacte_tuple(*seq):
    s = ()
    for i in seq:
        s += i
    return s

print(concacte_tuple((1, 2), (3, 4), (5, 6)))

# 2ème approche plus pythonique
# def concacte_tuple(seq):
#     return sum(seq, ())

# print(concacte_tuple((1, 2), (3, 4), (5, 6)))