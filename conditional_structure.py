# Structure conditionnelle: if...else

print("Êtes-vous majeur?")

# Conversion de l'entrée utilisateur en entier
age = int(input("Entrez votre âge: "))

if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")


# Structure conditionnelle: if...elif...else

print("Quel est votre niveau d'études?")

niveau = input("Entrez votre niveau "
               "(primaire, secondaire, universitaire): ").lower()

if niveau == "primaire":
    print("Vous êtes au niveau primaire.")
elif niveau == "secondaire":
    print("Vous êtes au niveau secondaire.")
elif niveau == "universitaire":
    print("Vous êtes au niveau universitaire.")
else:
    print("Niveau d'études non reconnu.")

# Expression conditionnelle (opérateur ternaire)

majeur = "majeur" if age >= 18 else "mineur"

# Opérateur logique
print("Connexion utilisateur")

# Exemple simple d'authentification utilisateur
utilisateur_connecte = input("Entrez votre nom d'utilisateur: ")
mot_de_passe = input("Entrez votre mot de passe: ")

if utilisateur_connecte == "Admin" and mot_de_passe == "admin123":
    print("Bienvenue, administrateur!")
else:
    print("Nom d'utilisateur ou mot de passe incorrect.")

# Notation avec 'or'

print("Vérification d'accès")
role = input("Entrez votre rôle (admin, modérateur, utilisateur): ").lower()
if role == "admin" or role == "modérateur":
    print("Accès accordé.")
else:
    print("Accès refusé.")

# Utilisation de 'not'

print("Vérification de l'état du compte")

compte_actif = input("Votre compte est-il actif? (oui/non): ").lower

if not (compte_actif == "oui"):
    print("Votre compte est inactif. Veuillez contacter le support.")
else:
    print("Votre compte est actif. Vous pouvez continuer.")
