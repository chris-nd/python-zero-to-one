def triangle(seq):
    a, b, c = seq
    # Vérifier si c'est un triangle valide
    if a + b <= c or a + c <= b or b + c <= a:
        return "Triangle invalide"
    
    for c in seq:
        counter = seq.count(c)
        if counter == 1:
            continue
        elif counter == 2:
            return "Isocele"
        elif counter == 3:
            return "Equilatéral"
    return "Scalène"

print(triangle((3, 3, 3)))       
print(triangle((3, 4, 5)))       
print(triangle((5, 5, 3)))       
print(triangle((1, 2, 10)))       
