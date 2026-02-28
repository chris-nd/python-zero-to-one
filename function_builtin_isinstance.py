def factoriel(argument):
    # si on reçoit un entier
    if isinstance(argument, int):              # (*)
        return 1 if argument <= 1 else argument * factoriel(argument - 1)
    # convertir en entier si on reçoit une chaîne
    elif isinstance(argument, str):
        return factoriel(int(argument))
    # la liste des résultats si on reçoit un tuple ou une liste 
    elif isinstance(argument, (tuple, list)):  # (**)
        return [factoriel(i) for i in argument]
    # sinon on lève une exception
    else:
        raise TypeError(argument)
    
print("entier", factoriel(4))
print("chaine", factoriel("8"))
print("tuple", factoriel((4, 8)))