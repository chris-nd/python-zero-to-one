def permutation_list(liste):
    if len(liste) <= 1:
        return [liste]
    
    result = []
    
    for i in range(len(liste)):
        element = liste[i]
        
        reste = liste[:i] + liste[i+1:]
        
        for p in permutation_list(reste):
            result.append([element] + p)
    
    return result

print(permutation_list([1, 2, 3]))