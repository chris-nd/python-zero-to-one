def fibonacci(n):
    liste = []
    for i in range(n):
        if i <= 1:
            liste.append(i)
            continue

        liste.append(liste[-1] + liste[-2])
        
    return liste
        

print(fibonacci(10))