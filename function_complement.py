def ma_fonction(dans_fonction):
    print('dans ma_fonction', dans_fonction , id(dans_fonction))
    
dans_appelant = ["texte"]
print('dans appelant   ', dans_appelant, id(dans_appelant))
ma_fonction(dans_appelant)

# on ne peut pas modifier un immuable dans une fonction
def increment(n):
    n += 1

compteur = 10
increment(compteur)
print(compteur)

# on peut par contre ajouter dans une liste
def insert(liste, valeur):
    liste.append(valeur)
    
liste = ["un"]
insert(liste, "texte")
print(liste)