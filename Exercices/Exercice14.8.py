# Aplatir un dictionnaire

# Entrée : dic -> dict
# Sortie : flat -> dict
# Contraintes:
#   Cas normal: dict imbriqué
#   Cas limite: dict est vide
#   Cas limite: dict est déjà aplati
#   Cas d'erreur: dict n'est pas une structure valide

# Décomposition

# Vérifier si dict n'est pas une structure valide
# Verifier si dict est vide
# Aplatir dict
# Renvoyer dict aplati

# Pseudo-code
# DEBUT

# SI dic n'est pas un dict
#   Lever une exception
# SI dic est vide
#   Renvoyer {}
# Pour chaque clé et valeur dans dic allant de 1 à n entrées
#   SI valeur est un dict
#       Appliquer la récursivité sur valeur
#       Créer une entrée dans flat_dic avec la clé composé et la valeur du plus haut niveau d'imbrication
#   SINON
#       Créer une entrée dans flat_dic avec la clé simple
#   Renvoyer flat_dic

# Aplatir un dictionnaire
def flat_dict(dic: dict, parent_key='', sep='.') -> dict:
    # Vérifier si dict n'est pas une structure valide
    if not isinstance(dic, dict):
        raise TypeError("Type invalide")
    
    # Verifier si dict est vide
    if not dic:
        return {}
    
    flat = {}

    # Aplatir dict
    for key, value in dic.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flat.update(flat_dict(value, new_key))
        else:
            flat[new_key] = value
    return flat

print(flat_dict({"a": {"b": 1, "c": 2}, "d": 3}))