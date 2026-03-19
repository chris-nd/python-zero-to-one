def sub_seq(seq, n):
    Liste = []
    for i in range(len(seq) - n + 1):
        Liste.append(seq[i:i+n])
    return Liste

print(sub_seq([1, 2, 3, 4], 2))

# Approche plus pythonique
# def sub_seq(seq, n):
#     return [seq[i:i+n] for i in range(len(seq) - n + 1)]
