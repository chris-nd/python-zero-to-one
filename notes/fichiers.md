## Les fichiers en Python

### Bonnes pratiques de base

**Toujours utiliser un context manager (`with`)**

```python
# ✅ RECOMMANDÉ - fermeture automatique garantie
with open("foo.txt", "w", encoding='utf-8') as sortie:
    for i in range(2):
        sortie.write(f"{i}\n")
```

**Avantages :**

- Fermeture automatique du fichier (même en cas d'erreur)
- Pas de fuite de ressources
- Code plus propre et sûr

### Modes d'ouverture principaux

| Mode | Description | Effet si fichier existe |
| --- | --- | --- |
| **`'r'`** | Lecture seule (défaut) | Erreur si n'existe pas |
| **`'w'`** | Écriture seule | **Écrase** le contenu |
| **`'a'`** | Ajout (append) | Ajoute à la fin |
| **`'r+'`** | Lecture + écriture | Conserve le contenu |
| **`'b'`** | Mode binaire | Combine avec r/w/a |

**Exemples :**

```python
# Lire un fichier (mode par défaut)
with open("foo.txt", encoding='utf-8') as entree:
    for line in entree:
        print(line, end='')

# Ajouter du contenu
with open("foo.txt", "a", encoding='utf-8') as sortie:
    sortie.write("nouvelle ligne\n")
```

### Un fichier est un itérateur

**Point clé :** Un fichier est son propre itérateur, donc on ne peut le parcourir qu'**une seule fois**.

```python
with open("foo.txt", encoding='utf-8') as entree:
    print(entree.__iter__() is entree)  # → True
```

**Conséquence - boucles imbriquées :**

```python
# ❌ NE FONCTIONNE PAS comme attendu
with open("foo.txt", encoding='utf-8') as entree:
    for l1 in entree:
        for l2 in entree:  # entree est déjà "épuisé"
            print(l1, "x", l2)
```

**Solution :** Fermer et rouvrir le fichier, ou charger le contenu en mémoire.

### Méthodes de lecture

**`read(size)` - Lire un nombre d'octets/caractères**

```python
# Lire TOUT le contenu
with open("foo.txt", encoding='utf-8') as entree:
    contenu = entree.read()
    print(contenu)

# Lire par blocs de 4 caractères
with open("foo.txt", encoding='utf-8') as entree:
    bloc1 = entree.read(4)  # 4 premiers caractères
    bloc2 = entree.read(4)  # 4 suivants
```

**Autres méthodes :**

- `readline()` : lit une ligne
- `readlines()` : lit toutes les lignes dans une liste
- Itération directe : `for line in fichier:`

### La méthode `flush()`

Les écritures sont **bufferisées** (stockées en mémoire temporairement) pour des raisons de performance.

```python
with open("log.txt", "w", encoding='utf-8') as f:
    f.write("Message important")
    f.flush()  # Force l'écriture immédiate sur disque
```

**Utilité :** Garantir que les données sont écrites immédiatement (logs critiques, etc.)

### Fichiers textuels vs binaires

**Mode textuel (défaut)**

- Manipule des objets `str`
- Nécessite de spécifier l'encodage (UTF-8 recommandé)

```python
with open('fichier.txt', 'w', encoding='utf-8') as f:
    f.write("déjà l'été\n")  # str

with open('fichier.txt', encoding='utf-8') as f:
    line = f.read()  # retourne un str
    print(type(line))  # <class 'str'>
```

**Mode binaire (avec `'b'`)**

- Manipule des objets `bytes`
- Pas besoin de spécifier l'encodage

```python
with open('fichier.txt', 'rb') as f:
    octets = f.read()  # retourne des bytes
    print(type(octets))  # <class 'bytes'>
```

### Exemple : encodage UTF-8

**Écriture en mode texte :**

```python
with open('test', 'w', encoding='utf-8') as output:
    output.write("déjà l'été\n")
```

**Lecture en mode binaire pour voir l'encodage :**

```python
with open('test', 'rb') as binfile:
    octets = binfile.read()
    for i, octet in enumerate(octets):
        print(f"{i} → {repr(chr(octet))} [{hex(octet)}]")
```

**Résultat :** Le caractère `é` (Unicode) est encodé en UTF-8 sur **2 octets** : `0xc3` et `0xa9`

**Comparaison :**

```python
# Mode texte : compte les caractères
with open('test', encoding='utf-8') as f:
    print(len(f.read()))  # 12 caractères

# Mode binaire : compte les octets
with open('test', 'rb') as f:
    print(len(f.read()))  # 16 octets (4 caractères UTF-8 = 8 octets)
```

### Fonction utile : `repr()`

Permet de voir le contenu exact d'une chaîne (y compris les caractères invisibles) :

```python
lines = "abc\ndef\n"
print(lines)      # Affiche avec retours à la ligne
print(repr(lines)) # → 'abc\ndef\n' (montre les \n)
```

### Tableau récapitulatif

| Opération | Code | Description |
| --- | --- | --- |
| **Ouvrir en lecture** | `open('f.txt', encoding='utf-8')` | Mode par défaut |
| **Ouvrir en écriture** | `open('f.txt', 'w', encoding='utf-8')` | Écrase le fichier |
| **Ouvrir en ajout** | `open('f.txt', 'a', encoding='utf-8')` | Ajoute à la fin |
| **Mode binaire** | `open('f.bin', 'rb')` | Lecture binaire |
| **Lire tout** | `f.read()` | Retourne tout le contenu |
| **Lire n octets** | `f.read(n)` | Lit n caractères/octets |
| **Itérer** | `for line in f:` | Parcourt ligne par ligne |
| **Écrire** | `f.write(texte)` | Écrit du texte |
| **Forcer écriture** | `f.flush()` | Vide le buffer |

## Fichiers et utilitaires (pathlib)

### Évolution des outils

**Ancienne approche (Python < 3.4) - OBSOLÈTE**
Trois modules distincts :

- `os.path` : calculs sur les chemins
- `os` : opérations sur fichiers (renommer, supprimer)
- `glob` : recherche de fichiers

**Nouvelle approche (Python ≥ 3.4) - RECOMMANDÉE**
Module unique : **`pathlib`** - Interface orientée objet moderne

### Ancien système (pour référence)

**Fonctions principales (à connaître pour lire du vieux code) :**

```python
import os
import glob

# Manipulation de chemins
os.path.join('dir', 'file.txt')    # Construit un chemin
os.path.basename('/path/to/file')   # → 'file'
os.path.dirname('/path/to/file')    # → '/path/to'
os.path.abspath('file.txt')         # Chemin absolu

# Tests
os.path.exists('file.txt')          # Existe ?
os.path.isfile('file.txt')          # Est un fichier ?
os.path.isdir('dir')                # Est un répertoire ?

# Métadonnées
os.path.getsize('file.txt')         # Taille en octets
os.path.getmtime('file.txt')        # Date de modification

# Opérations
os.remove('file.txt')               # Supprimer fichier
os.rmdir('dir')                     # Supprimer répertoire vide
os.removedirs('dir/subdir')         # Supprimer récursivement
os.rename('old.txt', 'new.txt')     # Renommer

# Recherche
glob.glob("*.txt")                  # Tous les fichiers .txt
```

### Module `pathlib` (moderne)

**Philosophie : Orienté Objet**

Au lieu de fonctions dispersées, on manipule des **objets** de type `Path`.

**Import :**

```python
from pathlib import Path
```

### Utilisation de base

**Créer un objet Path :**

```python
# Créer une instance associée à un fichier/répertoire
path = Path('fichier-temoin')
dirpath = Path('./data/')
```

C'est comme créer un `int` ou un `str` :

```python
i = int(3.5)      # int est une "usine" à entiers
path = Path(nom)  # Path est une "usine" à chemins
```

### Méthodes principales

**Vérifier l'existence :**

```python
path = Path('fichier.txt')
path.exists()  # → True ou False
```

**Créer un fichier et vérifier :**

```python
# Au départ, n'existe pas
path.exists()  # → False

# Créer le fichier
with open('fichier.txt', 'w', encoding='utf-8') as f:
    f.write('0123456789\n')

# Maintenant existe
path.exists()  # → True
```

### Métadonnées

**Obtenir toutes les métadonnées :**

```python
# Retourne un namedtuple avec toutes les infos
path.stat()
```

**Taille du fichier :**

```python
path.stat().st_size  # Taille en octets
```

**Date de modification :**

```python
# Nombre de secondes depuis le 1er janvier 1970
mtime = path.stat().st_mtime

# Convertir en format lisible
from datetime import datetime
mtime_datetime = datetime.fromtimestamp(mtime)
print(mtime_datetime)  # → 2024-02-06 14:30:45

# Formater
f"{mtime_datetime:%H:%M}"  # → "14:30"
```

### Supprimer un fichier

**Méthode simple :**

```python
path.unlink()  # Supprime le fichier
```

**Méthode sûre (si le fichier pourrait ne pas exister) :**

```python
try:
    path.unlink()
except FileNotFoundError:
    print("Fichier déjà supprimé")
```

**Vérifier après suppression :**

```python
path.exists()  # → False
```

### Attributs utiles

**Nom du fichier :**

```python
path.name  # Attention : ATTRIBUT, pas méthode (pas de parenthèses)
```

### Recherche de fichiers

**Trouver tous les fichiers correspondant à un motif :**

```python
# Créer un Path pour le répertoire
dirpath = Path('./data/')

# Utiliser glob() pour chercher
for json_file in dirpath.glob("*.json"):
    print(json_file)
```

**Exemples de motifs :**

```python
dirpath.glob("*.txt")        # Tous les .txt
dirpath.glob("*.py")         # Tous les .py
dirpath.glob("test_*.py")    # Tous les test_*.py
dirpath.glob("**/*.json")    # Récursif (tous sous-répertoires)
```

### Pour les avancés : sous-classes

**Type réel de l'objet :**

```python
path = Path('file.txt')
type(path)  # → <class 'pathlib.PosixPath'> (sous Linux/Mac)
            # → <class 'pathlib.WindowsPath'> (sous Windows)
```

**Hiérarchie :**

```python
from pathlib import PosixPath
issubclass(PosixPath, Path)  # → True
isinstance(path, Path)        # → True
```

Python choisit automatiquement la sous-classe appropriée selon l'OS.

## Formats de fichiers (JSON et autres)

### Le problème de la persistance des données

**Deux formes de représentation des données :**

1. **En mémoire (RAM) :** Format binaire optimisé pour calculs
    - Exemple : entier stocké sur 64 bits en binaire
    - Prêt pour le processeur
2. **Sur disque/réseau :** Format plus pérenne et portable
    - Besoin de lisibilité
    - Compatibilité entre machines différentes

**Solution :** Faire de la **traduction** (marshalling) entre ces deux formats.

### Le format JSON (recommandé)

**JSON = JavaScript Object Notation**

**Caractéristiques :**

- ✅ Format le plus populaire actuellement
- ✅ Léger et lisible
- ✅ Supporté par de nombreux langages
- ✅ Idéal pour communication avec applications web JavaScript
- ✅ Types de base des langages modernes (Python, Ruby, JavaScript)

**Utilisation en Python :**

```python
import json

# Données Python (types de base)
data = [
    [1, 2, 'a', [3.23, 4.32], {'eric': 32, 'jean': 43}],
    (1, 2, 3),  # tuple
]

# 📝 SAUVEGARDER dans un fichier JSON
with open("s1.json", "w", encoding='utf-8') as json_output:
    json.dump(data, json_output)

# 📖 RELIRE depuis un fichier JSON
with open("s1.json", encoding='utf-8') as json_input:
    data2 = json.load(json_input)
```

### Limitations de JSON

**Types NON supportés nativement :**

| Type Python | Dans JSON | Remarque |
| --- | --- | --- |
| `tuple` | → `list` | ⚠️ Converti en liste |
| `complex` | ❌ | Pas d'encodage possible |
| `set` | ❌ | Pas d'encodage possible |
| `frozenset` | ❌ | Pas d'encodage possible |

**Exemple de conversion :**

```python
data = [(1, 2, 3)]  # tuple
# Après sauvegarde/relecture JSON
data2 = [[1, 2, 3]]  # devient une liste !

print(type(data[0]))   # → <class 'tuple'>
print(type(data2[0]))  # → <class 'list'>
```

**Comportement :**

- Les données "simples" restent intactes (comme une deep copy)
- Les tuples deviennent des listes
- Complex, set, frozenset : impossibles sans extension

## Autres formats disponibles

### **1. Format CSV (Comma Separated Values)**

**Module :** `csv`

**Caractéristiques :**

- Format tableur (colonnes séparées par virgules)
- Utile pour données tabulaires
- Compatible avec Excel, LibreOffice, etc.

**Usage typique :**

```python
import csv

# Écrire
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['nom', 'age'])
    writer.writerow(['Alice', 30])

# Lire
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### **2. Format Pickle (spécifique Python)**

**Module :** `pickle`

**Caractéristiques :**

- ⚠️ Spécifique à Python (pas pour échange inter-langages)
- ✅ Moins de limitations que JSON
- ✅ Très utile pour sauvegardes locales
- ✅ Points de reprise de programmes

**Quand utiliser :**

- ❌ PAS pour échanger avec d'autres langages
- ✅ Pour sauvegarder l'état d'un programme Python
- ✅ Pour créer des checkpoints/reprises

**Usage :**

```python
import pickle

# Sauvegarder
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Charger
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)
```

### **3. Format XML**

**Caractéristiques :**

- Format populaire mais plus complexe
- ⚠️ Beaucoup plus lourd que JSON
- ✅ Très flexible et puissant
- Plusieurs bibliothèques disponibles en Python

**Comparaison XML vs JSON :**

| Critère | JSON | XML |
| --- | --- | --- |
| **Simplicité** | ✅ Simple | ❌ Complexe |
| **Légèreté** | ✅ Léger | ❌ Verbeux |
| **Flexibilité** | Limitée | ✅ Très flexible |
| **Performance** | ✅ Rapide | Plus lent |
| **Usage** | APIs web modernes | Systèmes legacy, configs |

### Tableau comparatif des formats

| Format | Usage principal | Avantages | Inconvénients |
| --- | --- | --- | --- |
| **JSON** | Échange de données, APIs web | Léger, universel, lisible | Limitations sur types Python |
| **CSV** | Données tabulaires | Simple, compatible tableurs | Pas de structure complexe |
| **Pickle** | Sauvegarde Python locale | Supporte tous types Python | Spécifique Python |
| **XML** | Configs, échange entreprise | Très flexible, validable | Lourd, complexe |

### 💡 Recommandations d'usage

**Choisir JSON si :**

- ✅ Échange de données entre programmes/langages
- ✅ Communication avec APIs web
- ✅ Données lisibles par humains
- ✅ Format universel nécessaire

**Choisir CSV si :**

- ✅ Données tabulaires simples
- ✅ Compatibilité avec Excel/tableurs
- ✅ Import/export de bases de données

**Choisir Pickle si :**

- ✅ Sauvegarde interne Python uniquement
- ✅ Tous les types Python doivent être préservés
- ✅ Performance importante
- ⚠️ Pas d'échange avec d'autres langages

**Choisir XML si :**

- ✅ Standards industriels imposés
- ✅ Validation de structure nécessaire
- ✅ Systèmes legacy

### Résumé en une phrase

**JSON** est le format standard moderne pour l'échange de données (léger, universel, lisible), **CSV** pour les tableaux, **Pickle** pour la sauvegarde Python locale, et **XML** pour les besoins très spécifiques nécessitant flexibilité maximale.

## Le module sys : Fichiers systèmes (stdin, stdout, stderr)

### Contexte : Interaction avec le système d'exploitation

**Architecture système :**

- **Noyau (kernel)** : a l'exclusivité pour interagir avec le matériel
- **Programmes utilisateur (userspace)** : utilisent des abstractions fournies par le noyau

**Opérations élémentaires sur fichiers :**

- `open` : ouvrir
- `close` : fermer
- `read` : lire
- `write` : écrire

### Les trois flux standards

Le système d'exploitation fournit trois flux (streams) pour l'interaction avec les programmes :

| Flux | Nom complet | Abréviation | Rôle |
| --- | --- | --- | --- |
| **Entrée standard** | Standard Input | `stdin` | Entrée du programme |
| **Sortie standard** | Standard Output | `stdout` | Sortie normale |
| **Erreur standard** | Standard Error | `stderr` | Messages d'erreur |

### Redirection dans le shell

**Concept :** Rediriger les entrées/sorties sans modifier le programme

**Exemples en ligne de commande :**

```bash
# Rediriger l'entrée et la sortie
$ monprogramme < fichier_entree > fichier_sortie

# Utiliser des pipes (chaîner des programmes)
$ programme1 | programme2 | programme3
```

**Avantage :** Pas besoin de sauvegarder les résultats intermédiaires sur disque.

### Le module `sys` en Python

Python expose ces trois flux via le module `sys` :

```python
import sys

# Les trois flux standards
sys.stdin   # Entrée standard
sys.stdout  # Sortie standard
sys.stderr  # Erreur standard
```

**Afficher les flux :**

```python
import sys
for channel in (sys.stdin, sys.stdout, sys.stderr):
    print(channel)
```

**Sortie typique (hors notebook) :**

```
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>
```

**Dans un notebook IPython/Jupyter :**
Les flux sont implémentés par des classes spécifiques à IPython.

### Redirection de `stdout` depuis Python

**Principe :** `print()` écrit dans `sys.stdout`, qui est une **variable** (attribut du module `sys`). On peut donc la modifier pour rediriger les sorties.

**Exemple complet :**

```python
import sys

# Ouvrir un fichier destination
autre_stdout = open('ma_sortie.txt', 'w', encoding='utf-8')

# Sauvegarder la référence originale
tmp = sys.stdout

# Sortie normale (terminal)
print('sur le terminal')

# REDIRECTION : remplacer stdout
sys.stdout = autre_stdout
print('dans le fichier')  # Écrit dans ma_sortie.txt

# RESTAURATION : remettre stdout original
sys.stdout = tmp

# Fermer le fichier
autre_stdout.close()

# Sortie de nouveau normale
print('de nouveau sur le terminal')
```

**Vérification :**

```python
with open("ma_sortie.txt", encoding='utf-8') as check:
    print(check.read())
# Affiche : "dans le fichier\n"
```

### Cas d'usage pratiques

**1. Capturer les sorties d'un programme :**

```python
import sys
from io import StringIO

# Créer un buffer en mémoire
buffer = StringIO()
old_stdout = sys.stdout

# Rediriger vers le buffer
sys.stdout = buffer
print("Message capturé")
print("Autre message")

# Restaurer
sys.stdout = old_stdout

# Récupérer le contenu
contenu = buffer.getvalue()
print(f"Capturé : {contenu}")
```

**2. Écrire dans stderr (messages d'erreur) :**

```python
import sys

# Écrire dans stderr au lieu de stdout
print("Message d'erreur", file=sys.stderr)

# Équivalent à :
sys.stderr.write("Message d'erreur\n")
```

**3. Lire depuis stdin :**

```python
import sys

# Lire une ligne depuis l'entrée standard
ligne = sys.stdin.readline()

# Lire tout le contenu
contenu = sys.stdin.read()
```

### Points importants

**1. `sys.stdout` est une variable**

- C'est un **attribut** du module `sys`
- On peut le modifier pour rediriger les sorties
- Toujours sauvegarder l'original pour le restaurer

**2. Portée des redirections**

```python
# Redirection dans des fonctions différentes
def rediriger():
    global ancien_stdout
    ancien_stdout = sys.stdout
    sys.stdout = open('sortie.txt', 'w', encoding='utf-8')

def restaurer():
    sys.stdout.close()
    sys.stdout = ancien_stdout
```

**3. Alternative avec context manager (recommandé)**

```python
from contextlib import redirect_stdout
import io

buffer = io.StringIO()
with redirect_stdout(buffer):
    print("Ceci va dans le buffer")

contenu = buffer.getvalue()
```

### Différences stdout vs stderr

**Pourquoi deux flux de sortie ?**

```python
import sys

# Sortie normale
print("Résultat : 42", file=sys.stdout)

# Message d'erreur
print("ATTENTION : valeur incorrecte", file=sys.stderr)
```

**En ligne de commande :**

```bash
# Rediriger seulement stdout
$ python script.py > resultats.txt
# Les erreurs s'affichent toujours à l'écran

# Rediriger seulement stderr
$ python script.py 2> erreurs.txt
# Les résultats s'affichent à l'écran

# Rediriger les deux séparément
$ python script.py > resultats.txt 2> erreurs.txt
```

### Utilisation dans des scripts

**Script qui lit stdin et écrit dans stdout :**

```python
#!/usr/bin/env python3
import sys

# Lire toutes les lignes de stdin
for ligne in sys.stdin:
    # Traiter et écrire dans stdout
    resultat = ligne.strip().upper()
    print(resultat)
```

**Utilisation en ligne de commande :**

```bash
$ echo "hello world" | python script.py
HELLO WORLD

$ cat fichier.txt | python script.py > sortie.txt
```

### Bonnes pratiques

1. **Toujours sauvegarder** l'original avant de rediriger
2. **Toujours restaurer** après utilisation
3. **Fermer** les fichiers ouverts pour redirection
4. **Préférer les context managers** quand possible
5. Utiliser `stderr` pour les **messages d'erreur et diagnostics**
6. Utiliser `stdout` pour les **résultats du programme**