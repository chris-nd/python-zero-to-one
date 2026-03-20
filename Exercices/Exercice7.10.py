def calculer_impot(revenu):
    # Définir les tranches (limite_superieure, taux)
    tranches = [
        (10000, 0.00),    # 0 à 10 000 : 0%
        (27000, 0.10),    # 10 001 à 27 000 : 10%
        (75000, 0.30),    # 27 001 à 75 000 : 30%
        (float('inf'), 0.45)  # Plus de 75 000 : 45%
    ]
    
    impot = 0
    precedent = 0
    
    for limite, taux in tranches:
        if revenu > precedent:
            # Montant imposable dans cette tranche
            montant_tranche = min(revenu, limite) - precedent
            
            # Calcul de l'impôt pour cette tranche
            impot += montant_tranche * taux
            
            precedent = limite
        else:
            break
    
    return impot

# Tests
print(f"Revenu 15 000€ → Impôt : {calculer_impot(15000):.2f}€")
print(f"Revenu 30 000€ → Impôt : {calculer_impot(30000):.2f}€")
print(f"Revenu 50 000€ → Impôt : {calculer_impot(50000):.2f}€")
print(f"Revenu 100 000€ → Impôt : {calculer_impot(100000):.2f}€")