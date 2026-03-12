def max_number(seq):
    state = seq[0]
    for n in seq:
        if state <= n:
            state = n
    return state

print(max_number((10, 5, 8)))
print(max_number((3, 9, 6)))
print(max_number((7, 7, 4)))
print(max_number((-5, -10, -3)))
        
