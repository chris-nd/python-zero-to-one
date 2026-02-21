import math

# Concatenation de chaînes avec f-string

a = 5
b = 10

# Utilisation de f-strings pour la concaténation et le calcul
texte_f_string = f"La somme de {a} et {b} est égale à {a + b}."
print(texte_f_string)  # Affiche: La somme de 5 et 10 est égale à 15.

# Pour les versions de Python antérieures à 3.6, on peut utiliser la méthode format()

age = 25
# Utilisation de la méthode format() pour insérer des variables dans une chaîne
texte_format = "J'ai {} ans.".format(age)
print(texte_format)  # Affiche: J'ai 25 ans.
texte_format_indexed = "J'ai {age} ans et je vis à {ville}.".format(
    age=age, ville="Paris")  # Utilisation d'index pour insérer plusieurs variables
print(texte_format_indexed)  # Affiche: J'ai 25 ans et je vis à Paris.
texte_format_indexed2 = "J'ai {} ans et je vis à {}.".format(
    age, "Paris")  # Utilisation d'index pour insérer plusieurs variables
print(texte_format_indexed2)  # Affiche: J'ai 25 ans et je vis à Paris.
texte_format_indexed3 = "J'ai {0} ans, {0} ce n'est pas très vieux.".format(
    age)  # Utilisation d'index numériques pour insérer plusieurs variables
print(texte_format_indexed3)  # Affiche: J'ai 25 ans et je vis à Paris.

# Utilisation de l'opérateur % pour la formatation de chaînes
prenom, nom = "Chris", "Ndouassi"
print("%s %s" % (prenom, nom))  # Affiche: Chris Ndouassi

# Utilisation d'un dictionnaire avec l'opérateur %
name = {'prenom': prenom, 'nom': nom}
print("%(prenom)s %(nom)s" % name)  # Affiche: Chris Ndouassi

# Formatage avancé avec f-strings
print(f"bla {2*math.pi=:.2f} bla")  # Affiche: bla 2*pi=6.28 bla
print(f"bla {2*math.pi:.2f} bla")  # Affiche: bla 6.28 bla
print(f"bla {math.pi=:.3f} bla")  # Affiche: bla pi=3.142 bla
print(f"bla {math.pi:.3f} bla")  # Affiche: bla 3.142 bla

integer = 42
# Affiche: Le nombre hexadécimal de 42 est 0x2a
print(f"Le nombre hexadécimal de {integer} est {integer:#x}")
# Affiche: Le nombre hexadécimal de 42 est 2a
print(f"Le nombre hexadécimal de {integer} est {integer:x}")
# Affiche: Le nombre hexadécimal de 42 est 0x2a
print(f"Le nombre en octet de {integer} est {integer:#o}")
# Affiche: Le nombre hexadécimal de 42 est 2a
print(f"Le nombre en octet de {integer} est {integer:o}")
# Affiche: Le nombre binaire de 42 est 0b101010
print(f"Le nombre binaire de {integer} est {integer:#b}")
# Affiche: Le nombre binaire de 42 est 101010
print(f"Le nombre binaire de {integer} est {integer:b}")

print(f"{integer:04d}")  # Affiche: x:0042
print(f"{integer:4d}")  # Affiche: x:0042
print(f"{integer:>4d}")  # Affiche: x:  42
print(f"{integer:<4d}")  # Affiche: x:42
print(f"{integer:^4d}")  # Affiche: xÒ: 42

# Affichage formaté des données en colonnes de largeur fixe
comptes = [
    ('Apollin', 'Dupont', 127),
    ('Myrtille', 'Lamartine', 25432),
    ('Prune', 'Soc', 827465),
]

for prenom, nom, solde in comptes:
    print(f"{prenom:<10} -- {nom:^12} -- {solde:>8} €")
