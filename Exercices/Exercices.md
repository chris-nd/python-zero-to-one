# Exercices pratiques Python

## 1. Notions de variable, d'objet et typage dynamique

**Exercice 1.1 (Facile)**
Créez un programme qui échange les valeurs de deux variables sans utiliser de variable temporaire.

- Données de test : a = 5, b = 10

**Exercice 1.2 (Facile)**
Écrivez un programme qui vérifie le type de différentes variables et affiche leur type.

- Données de test : 42, 3.14, "hello", True, None

**Exercice 1.3 (Facile)**
Créez un programme qui assigne la même valeur à trois variables différentes en une seule ligne, puis modifiez l'une d'elles et affichez toutes les valeurs.

- Données de test : valeur initiale = 100

**Exercice 1.4 (Moyen)**
Écrivez un programme qui démontre la différence entre l'affectation d'objets mutables et immutables.

- Données de test : créez deux variables pointant vers le même entier, puis deux variables pointant vers la même liste

**Exercice 1.5 (Moyen)**
Créez un programme qui utilise les fonctions id() pour démontrer quand deux variables pointent vers le même objet en mémoire.

- Données de test : testez avec des entiers, des chaînes et des listes

**Exercice 1.6 (Moyen)**
Écrivez un programme qui convertit une variable d'un type à un autre et gère les conversions impossibles.

- Données de test : "123", "12.5", "hello", 45, 3.14

**Exercice 1.7 (Moyen)**
Créez un programme qui utilise plusieurs affectations en cascade et affiche les résultats.

- Données de test : a = b = c = d = 0, puis modifiez-les individuellement

**Exercice 1.8 (Difficile)**
Écrivez un programme qui explore le comportement du cache des petits entiers de Python.

- Données de test : comparez les id() d'entiers entre -5 et 256, puis au-delà

**Exercice 1.9 (Difficile)**
Créez un programme qui démontre la différence entre copie superficielle et référence pour différents types d'objets.

- Données de test : entiers, listes, listes de listes

**Exercice 1.10 (Difficile)**
Écrivez un programme qui trace toutes les modifications de type d'une variable au cours de son cycle de vie.

- Données de test : commencez avec 0, puis transformez-le successivement en float, string, list, etc.

---

## 2. Les types numériques

**Exercice 2.1 (Facile)**
Créez un programme qui effectue les quatre opérations de base sur deux nombres.

- Données de test : 15, 4

**Exercice 2.2 (Facile)**
Écrivez un programme qui calcule le reste et le quotient d'une division entière.

- Données de test : 17, 5

**Exercice 2.3 (Facile)**
Créez un programme qui élève un nombre à une puissance donnée.

- Données de test : base = 2, exposant = 10

**Exercice 2.4 (Moyen)**
Écrivez un programme qui vérifie si un nombre est pair ou impair sans utiliser l'opérateur modulo.

- Données de test : 7, 12, 0, -5

**Exercice 2.5 (Moyen)**
Créez un programme qui arrondit un nombre à n décimales.

- Données de test : 3.14159265, n = 2, 4, 6

**Exercice 2.6 (Moyen)**
Écrivez un programme qui convertit des températures entre Celsius, Fahrenheit et Kelvin.

- Données de test : 0°C, 100°C, 32°F, 212°F

**Exercice 2.7 (Moyen)**
Créez un programme qui calcule la racine carrée d'un nombre sans utiliser de module.

- Données de test : 16, 25, 2, 10

**Exercice 2.8 (Difficile)**
Écrivez un programme qui génère les n premiers nombres de la suite de Fibonacci.

- Données de test : n = 10, 15, 20

**Exercice 2.9 (Difficile)**
Créez un programme qui détermine si un nombre est premier.

- Données de test : 2, 17, 25, 97, 100, 1

**Exercice 2.10 (Difficile)**
Écrivez un programme qui calcule le PGCD de deux nombres.

- Données de test : (48, 18), (100, 35), (17, 19)

---

## 3. Codage, jeux de caractères et Unicode

**Exercice 3.1 (Facile)**
Créez un programme qui affiche le code Unicode d'un caractère donné.

- Données de test : 'A', 'é', '€', '你'

**Exercice 3.2 (Facile)**
Écrivez un programme qui convertit un code Unicode en caractère.

- Données de test : 65, 233, 8364, 20320

**Exercice 3.3 (Facile)**
Créez un programme qui affiche une chaîne dans différents encodages.

- Données de test : "Héllo Wörld"

**Exercice 3.4 (Moyen)**
Écrivez un programme qui compte le nombre d'octets nécessaires pour encoder une chaîne en UTF-8.

- Données de test : "Hello", "Café", "你好"

**Exercice 3.5 (Moyen)**
Créez un programme qui vérifie si une chaîne contient uniquement des caractères ASCII.

- Données de test : "Hello", "Café", "Test123", "émoji 😀"

**Exercice 3.6 (Moyen)**
Écrivez un programme qui remplace tous les caractères accentués par leur équivalent non accentué.

- Données de test : "été", "naïveté", "coïncidence"

**Exercice 3.7 (Moyen)**
Créez un programme qui affiche tous les caractères Unicode dans une plage donnée.

- Données de test : plage de 65 à 90, plage de 8364 à 8370

**Exercice 3.8 (Difficile)**
Écrivez un programme qui détecte l'encodage probable d'une séquence d'octets.

- Données de test : b'Hello', b'\xc3\xa9t\xc3\xa9'

**Exercice 3.9 (Difficile)**
Créez un programme qui encode une chaîne en base64 manuellement.

- Données de test : "Hello", "Python"

**Exercice 3.10 (Difficile)**
Écrivez un programme qui compte le nombre de caractères de différentes catégories Unicode dans une chaîne.

- Données de test : "Hello World 123!", "Café au lait", "Test_2024!"

---

## 4. Les chaînes de caractères

**Exercice 4.1 (Facile)**
Créez un programme qui inverse une chaîne de caractères.

- Données de test : "Python", "Hello World"

**Exercice 4.2 (Facile)**
Écrivez un programme qui compte le nombre de voyelles dans une chaîne.

- Données de test : "Hello", "Programming", "AEIOUaeiou"

**Exercice 4.3 (Facile)**
Créez un programme qui met en majuscule la première lettre de chaque mot.

- Données de test : "hello world", "python programming"

**Exercice 4.4 (Moyen)**
Écrivez un programme qui vérifie si une chaîne est un palindrome.

- Données de test : "radar", "hello", "kayak", "A man a plan a canal Panama"

**Exercice 4.5 (Moyen)**
Créez un programme qui supprime tous les espaces d'une chaîne.

- Données de test : "  Hello  World  ", "Python Programming"

**Exercice 4.6 (Moyen)**
Écrivez un programme qui compte le nombre d'occurrences d'une sous-chaîne dans une chaîne.

- Données de test : chaîne = "banana", sous-chaîne = "ana"

**Exercice 4.7 (Moyen)**
Créez un programme qui remplace tous les espaces par des underscores.

- Données de test : "Hello World", "Python is fun"

**Exercice 4.8 (Difficile)**
Écrivez un programme qui vérifie si deux chaînes sont des anagrammes.

- Données de test : ("listen", "silent"), ("hello", "world"), ("triangle", "integral")

**Exercice 4.9 (Difficile)**
Créez un programme qui compresse une chaîne en comptant les caractères consécutifs.

- Données de test : "aabbcccc", "aaabbbcccaaa", "abcdef"

**Exercice 4.10 (Difficile)**
Écrivez un programme qui trouve la plus longue sous-chaîne sans caractères répétés.

- Données de test : "abcabcbb", "bbbbb", "pwwkew"

---

## 5. Les séquences

**Exercice 5.1 (Facile)**
Créez un programme qui accède au premier et au dernier élément d'une séquence.

- Données de test : [1, 2, 3, 4, 5], "Python"

**Exercice 5.2 (Facile)**
Écrivez un programme qui extrait une sous-séquence.

- Données de test : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], indices de 2 à 7

**Exercice 5.3 (Facile)**
Créez un programme qui inverse une séquence.

- Données de test : [1, 2, 3, 4, 5], "abcdef"

**Exercice 5.4 (Moyen)**
Écrivez un programme qui trouve l'élément maximum et minimum d'une séquence.

- Données de test : [3, 7, 1, 9, 2, 5]

**Exercice 5.5 (Moyen)**
Créez un programme qui vérifie si un élément existe dans une séquence.

- Données de test : séquence = [1, 2, 3, 4, 5], éléments à chercher = 3, 7

**Exercice 5.6 (Moyen)**
Écrivez un programme qui concatène deux séquences.

- Données de test : [1, 2, 3] et [4, 5, 6], "Hello" et "World"

**Exercice 5.7 (Moyen)**
Créez un programme qui répète une séquence n fois.

- Données de test : [1, 2], n = 3; "AB", n = 4

**Exercice 5.8 (Difficile)**
Écrivez un programme qui extrait tous les éléments d'une séquence à des indices pairs.

- Données de test : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

**Exercice 5.9 (Difficile)**
Créez un programme qui effectue une rotation d'une séquence de k positions.

- Données de test : [1, 2, 3, 4, 5], k = 2 (gauche et droite)

**Exercice 5.10 (Difficile)**
Écrivez un programme qui trouve toutes les sous-séquences de longueur n.

- Données de test : [1, 2, 3, 4], n = 2

---

## 6. Les listes

**Exercice 6.1 (Facile)**
Créez un programme qui ajoute un élément à la fin d'une liste.

- Données de test : liste = [1, 2, 3], élément = 4

**Exercice 6.2 (Facile)**
Écrivez un programme qui supprime un élément spécifique d'une liste.

- Données de test : liste = [1, 2, 3, 2, 4], élément à supprimer = 2

**Exercice 6.3 (Facile)**
Créez un programme qui insère un élément à une position donnée.

- Données de test : liste = [1, 2, 4, 5], position = 2, élément = 3

**Exercice 6.4 (Moyen)**
Écrivez un programme qui fusionne deux listes triées en une seule liste triée.

- Données de test : [1, 3, 5, 7], [2, 4, 6, 8]

**Exercice 6.5 (Moyen)**
Créez un programme qui supprime tous les doublons d'une liste en préservant l'ordre.

- Données de test : [1, 2, 2, 3, 4, 3, 5, 1]

**Exercice 6.6 (Moyen)**
Écrivez un programme qui trouve l'intersection de deux listes.

- Données de test : [1, 2, 3, 4, 5], [3, 4, 5, 6, 7]

**Exercice 6.7 (Moyen)**
Créez un programme qui divise une liste en n sous-listes de taille égale.

- Données de test : [1, 2, 3, 4, 5, 6, 7, 8, 9], n = 3

**Exercice 6.8 (Difficile)**
Écrivez un programme qui applique une rotation circulaire sur une liste.

- Données de test : [1, 2, 3, 4, 5], rotations = 2

**Exercice 6.9 (Difficile)**
Créez un programme qui aplatit une liste de listes.

- Données de test : [[1, 2], [3, 4], [5, 6, 7]]

**Exercice 6.10 (Difficile)**
Écrivez un programme qui trouve toutes les permutations d'une liste.

- Données de test : [1, 2, 3]

---

## 7. Introduction aux tests if et à la syntaxe

**Exercice 7.1 (Facile)**
Créez un programme qui détermine si un nombre est positif, négatif ou nul.

- Données de test : 5, -3, 0

**Exercice 7.2 (Facile)**
Écrivez un programme qui trouve le maximum de trois nombres.

- Données de test : (10, 5, 8), (3, 9, 6), (7, 7, 4)

**Exercice 7.3 (Facile)**
Créez un programme qui vérifie si une année est bissextile.

- Données de test : 2020, 2021, 2000, 1900

**Exercice 7.4 (Moyen)**
Écrivez un programme qui attribue une note lettre selon un score numérique.

- Données de test : 95, 85, 75, 65, 55 (A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: <60)

**Exercice 7.5 (Moyen)**
Créez un programme qui détermine le type de triangle selon les longueurs de ses côtés.

- Données de test : (3, 3, 3), (3, 4, 5), (5, 5, 3), (1, 2, 10)

**Exercice 7.6 (Moyen)**
Écrivez un programme qui calcule le prix d'un billet selon l'âge.

- Données de test : âges = 5, 12, 18, 65, 70 (enfant <12: 5€, adulte: 10€, senior >60: 7€)

**Exercice 7.7 (Moyen)**
Créez un programme qui vérifie si un caractère est une voyelle, une consonne ou autre.

- Données de test : 'a', 'B', '5', ' '

**Exercice 7.8 (Difficile)**
Écrivez un programme qui détermine le quadrant d'un point dans un plan cartésien.

- Données de test : (3, 4), (-2, 5), (-3, -4), (5, -2), (0, 0), (0, 5)

**Exercice 7.9 (Difficile)**
Créez un programme qui valide un mot de passe selon plusieurs critères.

- Données de test : "Pass123", "password", "P@ssw0rd", "Ab1!"

**Exercice 7.10 (Difficile)**
Écrivez un programme qui calcule l'impôt sur le revenu selon des tranches.

- Données de test : revenus = 15000, 30000, 50000, 100000

---

## 8. Introductions aux boucles for et aux fonctions

**Exercice 8.1 (Facile)**
Créez une fonction qui affiche les nombres de 1 à n.

- Données de test : n = 10

**Exercice 8.2 (Facile)**
Écrivez une fonction qui calcule la somme des nombres de 1 à n.

- Données de test : n = 100

**Exercice 8.3 (Facile)**
Créez une fonction qui calcule la factorielle d'un nombre.

- Données de test : 5, 0, 10

**Exercice 8.4 (Moyen)**
Écrivez une fonction qui affiche les tables de multiplication de 1 à n.

- Données de test : n = 5

**Exercice 8.5 (Moyen)**
Créez une fonction qui compte les chiffres dans un nombre.

- Données de test : 12345, 0, 9876543210

**Exercice 8.6 (Moyen)**
Écrivez une fonction qui inverse les chiffres d'un nombre.

- Données de test : 12345, 1000, 987

**Exercice 8.7 (Moyen)**
Créez une fonction qui calcule la moyenne d'une liste de nombres.

- Données de test : [1, 2, 3, 4, 5], [10, 20, 30]

**Exercice 8.8 (Difficile)**
Écrivez une fonction qui trouve tous les nombres premiers jusqu'à n.

- Données de test : n = 50

**Exercice 8.9 (Difficile)**
Créez une fonction qui calcule le produit de tous les éléments d'une liste.

- Données de test : [1, 2, 3, 4], [5, 10, 2]

**Exercice 8.10 (Difficile)**
Écrivez une fonction qui génère le triangle de Pascal avec n lignes.

- Données de test : n = 5, n = 7

---

## 9. Introduction aux compréhensions de listes

**Exercice 9.1 (Facile)**
Créez une liste des carrés des nombres de 1 à 10.

- Données de test : nombres de 1 à 10

**Exercice 9.2 (Facile)**
Écrivez une compréhension qui extrait tous les nombres pairs d'une liste.

- Données de test : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

**Exercice 9.3 (Facile)**
Créez une liste de tous les caractères d'une chaîne en majuscules.

- Données de test : "python programming"

**Exercice 9.4 (Moyen)**
Écrivez une compréhension qui filtre les mots de plus de 5 caractères.

- Données de test : ["chat", "python", "code", "programmation", "test"]

**Exercice 9.5 (Moyen)**
Créez une liste des longueurs de chaque mot dans une phrase.

- Données de test : "Python est un langage de programmation"

**Exercice 9.6 (Moyen)**
Écrivez une compréhension qui crée une liste de tuples (nombre, carré).

- Données de test : nombres de 1 à 10

**Exercice 9.7 (Moyen)**
Créez une liste des diviseurs d'un nombre n.

- Données de test : n = 24, n = 36

**Exercice 9.8 (Difficile)**
Écrivez une compréhension qui génère toutes les paires possibles de deux listes.

- Données de test : [1, 2, 3], ['a', 'b']

**Exercice 9.9 (Difficile)**
Créez une matrice n×n remplie de zéros.

- Données de test : n = 3, n = 5

**Exercice 9.10 (Difficile)**
Écrivez une compréhension qui aplatit une matrice.

- Données de test : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

---

## 10. Introduction aux modules

**Exercice 10.1 (Facile)**
Créez un programme qui utilise le module math pour calculer la racine carrée et la valeur absolue.

- Données de test : 16, -25, 2.5

**Exercice 10.2 (Facile)**
Écrivez un programme qui génère 5 nombres aléatoires entre 1 et 100.

- Données de test : exécutez plusieurs fois

**Exercice 10.3 (Facile)**
Créez un programme qui affiche la date et l'heure actuelles.

- Données de test : exécutez à différents moments

**Exercice 10.4 (Moyen)**
Écrivez un programme qui calcule le sinus, cosinus et tangente d'un angle.

- Données de test : 0, 30, 45, 60, 90 degrés

**Exercice 10.5 (Moyen)**
Créez un programme qui mélange aléatoirement une liste.

- Données de test : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

**Exercice 10.6 (Moyen)**
Écrivez un programme qui calcule le nombre de jours entre deux dates.

- Données de test : (2024-01-01, 2024-12-31), (2024-02-15, 2024-03-20)

**Exercice 10.7 (Moyen)**
Créez un programme qui arrondit un nombre au plafond et au plancher.

- Données de test : 3.2, 7.8, -2.5

**Exercice 10.8 (Difficile)**
Écrivez un programme qui simule 1000 lancers de dés et affiche la distribution des résultats.

- Données de test : dé à 6 faces

**Exercice 10.9 (Difficile)**
Créez un programme qui calcule l'âge exact d'une personne en années, mois et jours.

- Données de test : date de naissance = 2000-05-15

**Exercice 10.10 (Difficile)**
Écrivez un programme qui génère un mot de passe aléatoire sécurisé.

- Données de test : longueur = 12, doit contenir majuscules, minuscules, chiffres et symboles

---

## 11. Les fichiers

**Exercice 11.1 (Facile)**
Créez un programme qui écrit du texte dans un fichier.

- Données de test : "Hello, World!"

**Exercice 11.2 (Facile)**
Écrivez un programme qui lit tout le contenu d'un fichier.

- Données de test : créez un fichier avec plusieurs lignes de texte

**Exercice 11.3 (Facile)**
Créez un programme qui compte le nombre de lignes dans un fichier.

- Données de test : fichier avec 10 lignes

**Exercice 11.4 (Moyen)**
Écrivez un programme qui copie le contenu d'un fichier vers un autre.

- Données de test : fichier source avec du texte

**Exercice 11.5 (Moyen)**
Créez un programme qui ajoute du texte à la fin d'un fichier existant.

- Données de test : fichier existant avec du contenu

**Exercice 11.6 (Moyen)**
Écrivez un programme qui compte le nombre de mots dans un fichier.

- Données de test : fichier avec plusieurs phrases

**Exercice 11.7 (Moyen)**
Créez un programme qui lit un fichier ligne par ligne et affiche les lignes numérotées.

- Données de test : fichier avec 5-10 lignes

**Exercice 11.8 (Difficile)**
Écrivez un programme qui remplace toutes les occurrences d'un mot dans un fichier.

- Données de test : fichier contenant le mot "Python" plusieurs fois, remplacer par "Java"

**Exercice 11.9 (Difficile)**
Créez un programme qui fusionne plusieurs fichiers en un seul.

- Données de test : 3 fichiers avec du texte différent

**Exercice 11.10 (Difficile)**
Écrivez un programme qui lit un fichier et crée un fichier inversé (dernière ligne en premier).

- Données de test : fichier avec 10 lignes numérotées

---

## 1. Boucle while

**Exercice 1.1 (Facile)**
Créez un programme qui demande à l'utilisateur d'entrer un nombre et continue à demander jusqu'à ce qu'il entre un nombre positif.
- Données de test : -5, -2, 0, -10, 7

**Exercice 1.2 (Facile)**
Écrivez un programme qui affiche les nombres de 1 à 10 en utilisant une boucle while.
- Données de test : aucune

**Exercice 1.3 (Facile)**
Créez un programme qui calcule la somme des nombres de 1 à n en utilisant while.
- Données de test : n = 100

**Exercice 1.4 (Moyen)**
Écrivez un jeu de devinette : le programme choisit un nombre aléatoire entre 1 et 100, l'utilisateur doit le deviner. Le programme indique "trop grand" ou "trop petit".
- Données de test : nombre secret = 42

**Exercice 1.5 (Moyen)**
Créez un programme qui demande un mot de passe et ne laisse passer que si le bon mot de passe est entré (maximum 3 tentatives).
- Données de test : mot de passe = "Python123"

**Exercice 1.6 (Moyen)**
Écrivez un programme qui affiche tous les diviseurs d'un nombre en utilisant while.
- Données de test : 24, 36, 100

**Exercice 1.7 (Moyen)**
Créez un programme qui inverse les chiffres d'un nombre en utilisant while.
- Données de test : 12345, 9876, 100

**Exercice 1.8 (Difficile)**
Écrivez un programme qui trouve le plus grand commun diviseur de deux nombres en utilisant l'algorithme d'Euclide avec while.
- Données de test : (48, 18), (100, 35)

**Exercice 1.9 (Difficile)**
Créez un programme qui simule un distributeur automatique : l'utilisateur peut acheter des produits jusqu'à ce qu'il n'ait plus d'argent ou choisisse de quitter.
- Données de test : solde initial = 10€, produits à 1.50€, 2€, 3€

**Exercice 1.10 (Difficile)**
Écrivez un programme qui génère la suite de Collatz pour un nombre donné en utilisant while.
- Données de test : 27, 10, 100

---

## 2. match - case

**Exercice 2.1 (Facile)**
Créez un programme qui prend un jour de la semaine (1-7) et affiche son nom en utilisant match-case.
- Données de test : 1, 4, 7, 8

**Exercice 2.2 (Facile)**
Écrivez un calculateur simple qui prend deux nombres et un opérateur (+, -, *, /) et utilise match-case pour effectuer l'opération.
- Données de test : (10, 5, "+"), (20, 4, "*"), (15, 3, "/")

**Exercice 2.3 (Facile)**
Créez un convertisseur de notes (A, B, C, D, F) en pourcentages en utilisant match-case.
- Données de test : "A", "B", "C", "D", "F", "Z"

**Exercice 2.4 (Moyen)**
Écrivez un programme qui classe un âge en catégorie (enfant, adolescent, adulte, senior) en utilisant match-case avec guards.
- Données de test : 5, 15, 30, 70

**Exercice 2.5 (Moyen)**
Créez un menu de restaurant interactif avec match-case qui affiche le prix selon le choix.
- Données de test : "pizza", "burger", "salade", "dessert"

**Exercice 2.6 (Moyen)**
Écrivez un programme qui identifie le type de triangle (équilatéral, isocèle, scalène) selon trois longueurs en utilisant match-case avec patterns.
- Données de test : (5, 5, 5), (5, 5, 3), (3, 4, 5)

**Exercice 2.7 (Moyen)**
Créez un interpréteur de commandes simple avec match-case (help, quit, list, clear).
- Données de test : "help", "quit", "list", "invalid"

**Exercice 2.8 (Difficile)**
Écrivez un programme qui analyse une structure de données (liste, tuple, dict) et effectue différentes actions selon le type et le contenu en utilisant match-case avec pattern matching.
- Données de test : [1, 2], (1, 2), {"a": 1}, [1, 2, 3, 4, 5]

**Exercice 2.9 (Difficile)**
Créez un système de gestion d'états avec match-case (nouveau, en cours, terminé, annulé) avec transitions valides.
- Données de test : transitions de "nouveau" vers "en cours", "en cours" vers "terminé"

**Exercice 2.10 (Difficile)**
Écrivez un parser simple d'expressions mathématiques qui utilise match-case pour évaluer des tuples représentant des opérations.
- Données de test : ("+", 5, 3), ("*", ("+", 2, 3), 4)

---

## 3. Les dictionnaires

**Exercice 3.1 (Facile)**
Créez un dictionnaire représentant un étudiant avec nom, âge et notes, puis affichez toutes les informations.
- Données de test : {"nom": "Alice", "age": 20, "notes": [15, 17, 14]}

**Exercice 3.2 (Facile)**
Écrivez un programme qui compte la fréquence de chaque caractère dans une chaîne en utilisant un dictionnaire.
- Données de test : "hello", "programming"

**Exercice 3.3 (Facile)**
Créez un programme qui fusionne deux dictionnaires.
- Données de test : {"a": 1, "b": 2}, {"c": 3, "d": 4}

**Exercice 3.4 (Moyen)**
Écrivez un programme qui inverse un dictionnaire (clés deviennent valeurs et vice-versa).
- Données de test : {"a": 1, "b": 2, "c": 3}

**Exercice 3.5 (Moyen)**
Créez un carnet d'adresses permettant d'ajouter, rechercher et supprimer des contacts.
- Données de test : ajouter 3 contacts, rechercher un contact, supprimer un contact

**Exercice 3.6 (Moyen)**
Écrivez un programme qui groupe des étudiants par note (dictionnaire de listes).
- Données de test : [("Alice", 15), ("Bob", 12), ("Charlie", 15), ("David", 18)]

**Exercice 3.7 (Moyen)**
Créez un programme qui trouve les clés communes entre deux dictionnaires.
- Données de test : {"a": 1, "b": 2, "c": 3}, {"b": 5, "c": 6, "d": 7}

**Exercice 3.8 (Difficile)**
Écrivez un programme qui aplatit un dictionnaire imbriqué (nested dict) en un dictionnaire à un seul niveau avec des clés composées.
- Données de test : {"a": {"b": 1, "c": 2}, "d": 3}

**Exercice 3.9 (Difficile)**
Créez un système de cache simple avec un dictionnaire qui stocke les résultats de calculs coûteux.
- Données de test : calculer des factorielles et les mettre en cache

**Exercice 3.10 (Difficile)**
Écrivez un programme qui trouve toutes les anagrammes dans une liste de mots en utilisant un dictionnaire.
- Données de test : ["listen", "silent", "enlist", "hello", "world"]

---

## 4. Les ensembles (sets)

**Exercice 4.1 (Facile)**
Créez un programme qui supprime les doublons d'une liste en utilisant un ensemble.
- Données de test : [1, 2, 2, 3, 4, 3, 5, 1]

**Exercice 4.2 (Facile)**
Écrivez un programme qui vérifie si un élément existe dans un ensemble.
- Données de test : ensemble = {1, 2, 3, 4, 5}, chercher 3 et 7

**Exercice 4.3 (Facile)**
Créez un programme qui trouve l'union de deux ensembles.
- Données de test : {1, 2, 3}, {3, 4, 5}

**Exercice 4.4 (Moyen)**
Écrivez un programme qui trouve l'intersection de deux ensembles.
- Données de test : {1, 2, 3, 4}, {3, 4, 5, 6}

**Exercice 4.5 (Moyen)**
Créez un programme qui trouve la différence entre deux ensembles (éléments dans A mais pas dans B).
- Données de test : {1, 2, 3, 4, 5}, {4, 5, 6, 7}

**Exercice 4.6 (Moyen)**
Écrivez un programme qui trouve la différence symétrique (éléments dans A ou B mais pas dans les deux).
- Données de test : {1, 2, 3}, {3, 4, 5}

**Exercice 4.7 (Moyen)**
Créez un programme qui vérifie si un ensemble est un sous-ensemble d'un autre.
- Données de test : {1, 2} et {1, 2, 3, 4}, {1, 5} et {1, 2, 3, 4}

**Exercice 4.8 (Difficile)**
Écrivez un programme qui trouve tous les caractères uniques communs à plusieurs chaînes.
- Données de test : ["hello", "world", "python"]

**Exercice 4.9 (Difficile)**
Créez un programme qui identifie les éléments présents dans exactement k ensembles parmi n ensembles donnés.
- Données de test : [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}], k = 2

**Exercice 4.10 (Difficile)**
Écrivez un programme qui vérifie si plusieurs ensembles sont mutuellement disjoints (aucun élément commun entre eux).
- Données de test : [{1, 2}, {3, 4}, {5, 6}], [{1, 2}, {2, 3}, {4, 5}]

---

## 5. Les tuples

**Exercice 5.1 (Facile)**
Créez un programme qui échange deux variables en utilisant un tuple.
- Données de test : a = 5, b = 10

**Exercice 5.2 (Facile)**
Écrivez un programme qui retourne plusieurs valeurs d'une fonction en utilisant un tuple.
- Données de test : calculer min, max et moyenne d'une liste

**Exercice 5.3 (Facile)**
Créez un programme qui compte les occurrences d'un élément dans un tuple.
- Données de test : (1, 2, 3, 2, 4, 2, 5), chercher 2

**Exercice 5.4 (Moyen)**
Écrivez un programme qui trouve l'indice d'un élément dans un tuple.
- Données de test : (10, 20, 30, 40, 50), chercher 30

**Exercice 5.5 (Moyen)**
Créez un programme qui concatène plusieurs tuples.
- Données de test : (1, 2), (3, 4), (5, 6)

**Exercice 5.6 (Moyen)**
Écrivez un programme qui convertit une liste de tuples en dictionnaire.
- Données de test : [("a", 1), ("b", 2), ("c", 3)]

**Exercice 5.7 (Moyen)**
Créez un programme qui trie une liste de tuples selon le deuxième élément.
- Données de test : [("Alice", 25), ("Bob", 20), ("Charlie", 30)]

**Exercice 5.8 (Difficile)**
Écrivez un programme qui dépaquette (unpacks) un tuple imbriqué.
- Données de test : (1, (2, 3), (4, (5, 6)))

**Exercice 5.9 (Difficile)**
Créez un programme qui utilise des tuples nommés (namedtuple) pour représenter des points en 2D et calculer la distance entre eux.
- Données de test : Point(0, 0) et Point(3, 4)

**Exercice 5.10 (Difficile)**
Écrivez un programme qui compresse deux listes en une liste de tuples en utilisant zip().
- Données de test : [1, 2, 3], ["a", "b", "c"]

---

## 6. Les exceptions

**Exercice 6.1 (Facile)**
Créez un programme qui gère une division par zéro avec try/except.
- Données de test : 10/0, 10/2

**Exercice 6.2 (Facile)**
Écrivez un programme qui gère la conversion d'une chaîne en entier avec gestion d'erreur.
- Données de test : "123", "abc", "45.5"

**Exercice 6.3 (Facile)**
Créez un programme qui gère l'accès à un indice invalide dans une liste.
- Données de test : liste = [1, 2, 3], indices 1 et 10

**Exercice 6.4 (Moyen)**
Écrivez un programme qui gère plusieurs types d'exceptions différemment (ValueError, TypeError, IndexError).
- Données de test : diverses opérations qui peuvent lever ces exceptions

**Exercice 6.5 (Moyen)**
Créez un programme qui utilise finally pour garantir la fermeture d'une ressource.
- Données de test : ouvrir un fichier, lire son contenu, garantir sa fermeture

**Exercice 6.6 (Moyen)**
Écrivez un programme qui lève une exception personnalisée quand une valeur est hors limites.
- Données de test : valeurs entre 1 et 100, tester avec 50, 150, -10

**Exercice 6.7 (Moyen)**
Créez un programme qui utilise else avec try/except pour exécuter du code seulement si aucune exception n'est levée.
- Données de test : diverses opérations

**Exercice 6.8 (Difficile)**
Écrivez un décorateur qui capture et log toutes les exceptions d'une fonction.
- Données de test : fonction qui peut réussir ou échouer

**Exercice 6.9 (Difficile)**
Créez une hiérarchie d'exceptions personnalisées pour un système de validation (ValidationError, avec sous-classes RangeError, FormatError).
- Données de test : valider différents types d'entrées

**Exercice 6.10 (Difficile)**
Écrivez un gestionnaire de contexte personnalisé (context manager) avec __enter__ et __exit__ pour gérer des ressources.
- Données de test : créer un gestionnaire pour mesurer le temps d'exécution

---

## 7. Type hints et isinstance

**Exercice 7.1 (Facile)**
Créez une fonction avec type hints qui prend deux entiers et retourne leur somme.
- Données de test : (5, 3), (10, 20)

**Exercice 7.2 (Facile)**
Écrivez une fonction avec type hints qui prend une liste de nombres et retourne leur moyenne.
- Données de test : [1, 2, 3, 4, 5], [10, 20, 30]

**Exercice 7.3 (Facile)**
Créez une fonction qui utilise isinstance() pour vérifier si un argument est une chaîne ou un nombre.
- Données de test : "hello", 42, 3.14, [1, 2, 3]

**Exercice 7.4 (Moyen)**
Écrivez une fonction avec type hints pour un dictionnaire et vérifiez les types des valeurs avec isinstance().
- Données de test : {"nom": "Alice", "age": 25, "notes": [15, 17]}

**Exercice 7.5 (Moyen)**
Créez une fonction générique avec type hints qui accepte une liste de n'importe quel type et retourne le premier élément.
- Données de test : [1, 2, 3], ["a", "b", "c"]

**Exercice 7.6 (Moyen)**
Écrivez une fonction avec type hints Optional pour gérer les valeurs None.
- Données de test : chercher un élément qui peut exister ou non

**Exercice 7.7 (Moyen)**
Créez une fonction qui utilise isinstance() pour traiter différemment les listes, tuples et ensembles.
- Données de test : [1, 2, 3], (1, 2, 3), {1, 2, 3}

**Exercice 7.8 (Difficile)**
Écrivez une fonction avec type hints Union qui accepte soit un int soit un str et retourne une str.
- Données de test : 42, "hello"

**Exercice 7.9 (Difficile)**
Créez une fonction avec type hints pour des fonctions callback (Callable).
- Données de test : passer différentes fonctions comme arguments

**Exercice 7.10 (Difficile)**
Écrivez une fonction générique avec TypeVar qui fonctionne avec n'importe quel type tout en préservant le type.
- Données de test : listes de différents types

---

## 8. Les classes (introduction)

**Exercice 8.1 (Facile)**
Créez une classe Point avec des attributs x et y, et une méthode pour afficher les coordonnées.
- Données de test : Point(3, 4)

**Exercice 8.2 (Facile)**
Écrivez une classe Rectangle avec largeur et hauteur, et une méthode pour calculer l'aire.
- Données de test : Rectangle(5, 3)

**Exercice 8.3 (Facile)**
Créez une classe Personne avec nom et âge, et une méthode pour se présenter.
- Données de test : Personne("Alice", 25)

**Exercice 8.4 (Moyen)**
Écrivez une classe CompteBancaire avec méthodes dépôt, retrait et consultation du solde.
- Données de test : solde initial 100, dépôt 50, retrait 30

**Exercice 8.5 (Moyen)**
Créez une classe Voiture avec marque, modèle, année et une méthode pour calculer l'âge.
- Données de test : Voiture("Toyota", "Corolla", 2015)

**Exercice 8.6 (Moyen)**
Écrivez une classe Étudiant qui hérite de Personne et ajoute un attribut notes.
- Données de test : Étudiant("Bob", 20, [15, 17, 14])

**Exercice 8.7 (Moyen)**
Créez une classe Cercle avec rayon et des méthodes pour calculer l'aire et le périmètre.
- Données de test : Cercle(5)

**Exercice 8.8 (Difficile)**
Écrivez une classe Stack (pile) avec méthodes push, pop, peek et is_empty.
- Données de test : push(1), push(2), pop(), peek()

**Exercice 8.9 (Difficile)**
Créez une classe File (queue) avec méthodes enqueue, dequeue et size.
- Données de test : enqueue(1), enqueue(2), dequeue()

**Exercice 8.10 (Difficile)**
Écrivez une classe avec des méthodes spéciales __str__, __repr__, __len__, __getitem__.
- Données de test : créer une classe personnalisée et utiliser ces méthodes

---

## 9. Portée des variables (LEGB)

**Exercice 9.1 (Facile)**
Créez un programme qui démontre la différence entre variable locale et globale.
- Données de test : modifier une variable dans une fonction

**Exercice 9.2 (Facile)**
Écrivez un programme qui utilise le mot-clé global pour modifier une variable globale.
- Données de test : compteur global incrémenté par une fonction

**Exercice 9.3 (Facile)**
Créez une fonction imbriquée et démontrez la portée enclosing.
- Données de test : variable dans fonction externe accessible par fonction interne

**Exercice 9.4 (Moyen)**
Écrivez un programme qui utilise nonlocal pour modifier une variable de la fonction englobante.
- Données de test : compteur dans fonction externe modifié par fonction interne

**Exercice 9.5 (Moyen)**
Créez un programme qui démontre l'ordre de recherche LEGB.
- Données de test : même nom de variable à différents niveaux

**Exercice 9.6 (Moyen)**
Écrivez une closure qui capture et modifie une variable de la fonction englobante.
- Données de test : créer un compteur avec closure

**Exercice 9.7 (Moyen)**
Créez un programme qui utilise des variables built-in et évite de les masquer.
- Données de test : utiliser len, sum sans les écraser

**Exercice 9.8 (Difficile)**
Écrivez un décorateur qui utilise des variables nonlocal pour compter le nombre d'appels.
- Données de test : fonction décorée appelée plusieurs fois

**Exercice 9.9 (Difficile)**
Créez un générateur de fonctions qui utilisent des closures pour capturer différentes valeurs.
- Données de test : créer plusieurs fonctions avec différents comportements

**Exercice 9.10 (Difficile)**
Écrivez un programme qui démontre les pièges de la portée avec les lambdas dans une boucle.
- Données de test : créer des lambdas dans une boucle et les appeler

---

## 10. Affectation simultanée et références partagées

**Exercice 10.1 (Facile)**
Créez un programme qui échange trois variables en une seule ligne.
- Données de test : a=1, b=2, c=3

**Exercice 10.2 (Facile)**
Écrivez un programme qui démontre l'affectation multiple.
- Données de test : x = y = z = 0

**Exercice 10.3 (Facile)**
Créez un programme qui dépaquette une liste en plusieurs variables.
- Données de test : [1, 2, 3, 4, 5]

**Exercice 10.4 (Moyen)**
Écrivez un programme qui démontre la différence entre = et copy() pour les listes.
- Données de test : liste1 = [1, 2, 3]

**Exercice 10.5 (Moyen)**
Créez un programme qui démontre le problème des références partagées avec des listes imbriquées.
- Données de test : matrice = [[0] * 3] * 3

**Exercice 10.6 (Moyen)**
Écrivez un programme qui utilise deepcopy pour copier des structures imbriquées.
- Données de test : liste de listes ou dictionnaire de listes

**Exercice 10.7 (Moyen)**
Créez un programme qui utilise l'opérateur walrus := dans une boucle while.
- Données de test : lire des entrées jusqu'à condition

**Exercice 10.8 (Difficile)**
Écrivez un programme qui démontre les références partagées avec des objets mutables comme valeurs par défaut de fonction.
- Données de test : fonction avec liste comme valeur par défaut

**Exercice 10.9 (Difficile)**
Créez un programme qui utilise l'affectation étendue avec * pour capturer plusieurs valeurs.
- Données de test : first, *middle, last = [1, 2, 3, 4, 5]

**Exercice 10.10 (Difficile)**
Écrivez un programme qui démontre et résout le problème des références circulaires.
- Données de test : deux objets qui se référencent mutuellement

---

## 11. Expressions et instructions if / Opérateurs booléens

**Exercice 11.1 (Facile)**
Créez un programme qui utilise l'opérateur ternaire (if-else en une ligne).
- Données de test : déterminer si un nombre est pair

**Exercice 11.2 (Facile)**
Écrivez un programme qui utilise les opérateurs and, or, not.
- Données de test : vérifier plusieurs conditions

**Exercice 11.3 (Facile)**
Créez un programme qui utilise l'évaluation court-circuit (short-circuit).
- Données de test : conditions qui s'arrêtent à la première False

**Exercice 11.4 (Moyen)**
Écrivez un programme qui utilise all() et any() avec des itérables.
- Données de test : listes de booléens

**Exercice 11.5 (Moyen)**
Créez un programme qui vérifie si une valeur est dans un intervalle en utilisant des opérateurs chaînés.
- Données de test : 1 <= x <= 10

**Exercice 11.6 (Moyen)**
Écrivez un programme qui utilise l'opérateur in avec différentes structures de données.
- Données de test : listes, tuples, sets, dicts, strings

**Exercice 11.7 (Moyen)**
Créez un programme qui utilise l'opérateur is vs ==.
- Données de test : comparer des objets et des valeurs

**Exercice 11.8 (Difficile)**
Écrivez un programme qui implémente une logique complexe avec des opérateurs booléens imbriqués.
- Données de test : système de validation avec plusieurs règles

**Exercice 11.9 (Difficile)**
Créez un programme qui utilise des expressions booléennes pour le filtrage de données.
- Données de test : filtrer une liste selon plusieurs critères

**Exercice 11.10 (Difficile)**
Écrivez un programme qui démontre la différence entre bool(x) et x is True.
- Données de test : différentes valeurs truthy et falsy

---

## 12. Module builtins

**Exercice 12.1 (Facile)**
Créez un programme qui liste toutes les fonctions built-in disponibles.
- Données de test : dir(__builtins__)

**Exercice 12.2 (Facile)**
Écrivez un programme qui utilise map() pour transformer une liste.
- Données de test : [1, 2, 3, 4, 5]

**Exercice 12.3 (Facile)**
Créez un programme qui utilise filter() pour filtrer une liste.
- Données de test : filtrer les nombres pairs de [1, 2, 3, 4, 5, 6]

**Exercice 12.4 (Moyen)**
Écrivez un programme qui utilise zip() pour combiner plusieurs listes.
- Données de test : [1, 2, 3], ["a", "b", "c"], [True, False, True]

**Exercice 12.5 (Moyen)**
Créez un programme qui utilise enumerate() avec un index de départ personnalisé.
- Données de test : ["a", "b", "c"], start=1

**Exercice 12.6 (Moyen)**
Écrivez un programme qui utilise sorted() avec une clé personnalisée.
- Données de test : trier une liste de tuples selon le deuxième élément

**Exercice 12.7 (Moyen)**
Créez un programme qui utilise reversed() sur différentes séquences.
- Données de test : listes, tuples, strings

**Exercice 12.8 (Difficile)**
Écrivez un programme qui combine map(), filter() et reduce().
- Données de test : calculer la somme des carrés des nombres pairs

**Exercice 12.9 (Difficile)**
Créez un programme qui utilise exec() et eval() de manière sécurisée.
- Données de test : expressions mathématiques simples

**Exercice 12.10 (Difficile)**
Écrivez un programme qui utilise vars() et dir() pour l'introspection d'objets.
- Données de test : examiner les attributs d'une classe personnalisée