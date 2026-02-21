texte = "Bonjour tout le monde"

# Ces deux chaînes sont automatiquement concaténées
message = "abc" "def"
print(message)  # → "abcdef"

# Utile pour formatter du code long
long_message = (
    "Première partie "
    "Deuxième partie "
    "Troisième partie"
)

# Modifications de casse

print(texte.upper())  # Convertit en majuscules
print(texte.lower())  # Convertit en minuscules
print(texte.capitalize())  # Met en majuscule la première lettre
print(texte.title())  # Met en majuscule la première lettre de chaque mot
print(texte.swapcase())  # Inverse la casse des lettres

# Remplacement et suppression de caractères

print(texte.replace("jour", "soir"))  # Remplace "Bonjour" par "Bonsoir"
print(texte.replace("jour", "soir").replace("tout", "toute").replace("le monde", "la famille"))  # Chaînage de remplacements
print("   Supprime les espaces avant et après   ".strip())  # Supprime les espaces avant et après
print("  bonjour  ".lstrip())  # Supprime les espaces à gauche
print("  bonjour  ".rstrip())  # Supprime les espaces à droite
print("  bonjour  ".strip(" ukor"))  # Supprime les espaces à droite
print("  bonjour  ".lstrip(" ukor"))  # Supprime les espaces à droite
print("  bonjour  ".rstrip(" ukor"))  # Supprime les escapes à droite

# Division et jointure de chaînes

liste_caracteres = "b o n j o u r".split();  # Divise la chaîne en une liste de caractères
print(liste_caracteres)
print(type(liste_caracteres)) # Affiche le type de la variable (liste)
print("-".join(liste_caracteres))  # Joint les caractères avec un tiret entre eux

# Remplissage de chaînes

print("9".zfill(4))  # Remplit avec des zéros à gauche pour atteindre une longueur de 4
for i in range(1, 11):
    print(str(i).zfill(2))  # Affiche les nombres de 1 à 10 avec des zéros à gauche pour atteindre une longueur de 3

# Vérifications de type de chaîne

print("Bonjour".islower())  # Vérifie si la chaîne est en minuscules
print("BONJOUR".isupper())  # Vérifie si la chaîne est en majuscules
print("Bonjour".istitle())  # Vérifie si la chaîne est en format titre
print("12345".isdigit())  # Vérifie si la chaîne est composée uniquement de chiffres
print("12man".isdigit())  # Vérifie si la chaîne est composée uniquement de chiffres
print("a".isdigit())  # Vérifie si la chaîne est composée uniquement de chiffres

# Comptage des occurrences

print("Bonjour le monde".count("o"))  # Compte le nombre d'occurrences de "o"
print("Bonjour le jour".count("jour"))  # Compte le nombre d'occurrences de "jour"
print("Bonjour le jour".count(" jour"))  # Compte le nombre d'occurrences de " jour"

# Recherche de sous-chaînes

print("Bonjour".find("o"))  # Trouve la première occurrence de "o"
print("Bonjour".find("z"))  # Trouve la première occurrence de "z"
print("Bonjour le monde".find("le"))  # Trouve la première occurrence de "le"
print("Bonjour le monde".find("monde"))  # Trouve la première occurrence de "monde"
print("Bonjour le monde".find("jour"))  # Trouve la première occurrence de "jour"
print("Bonjour le jour".rfind("jour"))  # Trouve la première occurrence de "jour"


print("Bonjour le monde".index("o"))  # Trouve la première occurrence de "o"
print("Bonjour le monde".index("le"))  # Trouve la première occurrence de "le"
print("Bonjour le monde".index("monde"))  # Trouve la première occurrence de "monde"

print("Bonjour le monde".startswith("Bon"))  # Vérifie si la chaîne commence par "Bon"
print("image.png".endswith(".png"))  # Vérifie si la chaîne se termine par ".png"
print("document.pdf".endswith(".png"))  # Vérifie si la chaîne se termine par ".png"

