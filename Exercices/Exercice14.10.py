from collections import defaultdict

def find_anagramme(liste):
    if not isinstance(liste, list):
        raise TypeError("Le paramètre doit être une liste")

    if not liste:
        return None
    
    if len(liste) == 1:
        return liste
    
    dic = defaultdict(list)

    for mot in liste:
        signature = "".join(sorted(mot))
        dic[signature].append(mot)
    
    return dict(dic)

print(find_anagramme(["listen", "silent", "enlist", "hello", "world"]))
