def produit(liste):
    if not liste:
        return 1
    
    produit = 1

    for i in liste:
        produit *= i

    return produit

print(produit([1, 2, 3, 4, 5]))
print(produit([10, 20, 30]))