dic = {}

def ajouter(nom, tel):
    dic[nom] = tel

def rechercher(nom):
    return(f"{nom} -> {dic.get(nom)}")

def supprimer(nom):
    return dic.pop(nom, "Contact non trouvé")

ajouter("chris", "3456")
ajouter("loïc", "123456")
ajouter("léa", "23456")

print(dic)

print(rechercher("léa"))
print(supprimer("loïc"))