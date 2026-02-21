from collections import defaultdict

dictionnaire = {
    "nom": "Dupont",
    "age": 30,
    "ville": "Paris"
}

print(dictionnaire["nom"])

dictionnaire["ville"] = "Los Angeles"

print(dictionnaire["ville"])

dictionnaire["zip"] = "75000"

liste = [("Chris", 18), ("Lea", 17)]

dic = dict(liste)

print(dic)

print(dict(anna = 30, lisa = 35, lola = 28))

print(dic.get("Chris"))
print(dic.get("Bob", "Inconnu"))

keys = dictionnaire.keys() 
values = dictionnaire.values()
items = dictionnaire.items()

print(type(keys), keys)
print(type(values), values)
print(type(items), items)

del dictionnaire["zip"]

print("zip" in dictionnaire)

for k in dictionnaire:
    print(k, end=", ")

for key in dictionnaire.keys():
    print(key, end=", ")

for value in dictionnaire.values():
    print(value)

for key, value in dictionnaire.items():
    print(f"{key:>10}:{value:^20}")

dictionnaire.update({"nom": "Durand", "zip": 95000})

print(dictionnaire)

tuples = [
    (1, 2),
    (2, 1),
    (1, 3),
    (2, 4),
]

resultat = {}
for x, y in tuples:
    if x not in resultat:
        resultat[x] = []  # Initialisation manuelle
    resultat[x].append(y)

annuaire = {'alice': 30, 'eric': 70, 'bob': 42, 'jean': 25}

print(annuaire.setdefault('eric', 50))

print(annuaire.setdefault('inconnu', 50))

print(annuaire)

# Module defaultdict

resultat = defaultdict(list)

for x, y in tuples:
    resultat[x].append(y)

for key, value in resultat.items():
    print(key, value)

compteurs = defaultdict(int)

phrase = "une phrase dans laquelle on veut compter les caractères"

for c in phrase:
    compteurs[c] += 1

print(sorted(compteurs.items()))

# Gérer des enregistrements

# Liste de dictionnaires
personnes = [
    {'nom': 'Pierre',  'age': 25, 'email': 'pierre@example.com'},
    {'nom': 'Paul',    'age': 18, 'email': 'paul@example.com'},
    {'nom': 'Jacques', 'age': 52, 'email': 'jacques@example.com'},
]

# Modifier un champ (anniversaire de Pierre)
personnes[0]['age'] += 1

# Parcourir
for personne in personnes:
    for info, valeur in personne.items():
        print(f"{info} -> {valeur}")

#Dictionnaire de dictionnaires (avec index)

# Dictionnaire par compréhension
index_par_nom = {personne['nom']: personne for personne in personnes}

print(index_par_nom['Pierre'])

index_par_nom['Pierre']['age'] += 1

print(index_par_nom['Pierre']['age'])

for nom, record in index_par_nom.items():
    print(f"Nom : {nom} -> enregistrement : {record}")

# Utiliser des classes

class Personne:
    # Constructeur
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    # Méthode pour affichage lisible
    def __repr__(self):
        return f"{self.nom} ({self.age} ans) sur {self.email}"
    
personnes2 = [
    Personne('Pierre',  25, 'pierre@example.com'),
    Personne('Paul',    18, 'paul@example.com'),
    Personne('Jacques', 52, 'jacques@example.com'),
]

# Afficher un élément
print(personnes2[0]) # → Pierre (25 ans) sur pierre@example.com

# Noter : personne.nom au lieu de personne['nom']
index2 = {personne.nom: personne for personne in personnes2}

# Utilisation
print(index2['Pierre']) # → Pierre (25 ans) sur pierre@example.com

# Modifier l'âge
index2['Pierre'].age += 1
