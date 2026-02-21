import os
import glob
import pathlib as Path
import datetime as datetime
from pathlib import PosixPath
import sys

my_file = open(
    r"/Users/Chris/Software Development/Langage de programmation/Python/Zero to One/my_file1.txt",
    "w",
    encoding="utf-8",
)

for i in range(100):
    my_file.write(f"Ligne {i + 1}\n")

my_file.close()


my_file1 = open(
    r"/Users/Chris/Software Development/Langage de programmation/Python/Zero to One/my_file1.txt",
    "r",
    encoding="utf-8",
)
my_file2 = open(
    r"/Users/Chris/Software Development/Langage de programmation/Python/Zero to One/my_file2.txt",
    "w",
    encoding="utf-8",
)

for line in my_file1:
    line = line.split()
    line[0] = line[0].upper()
    my_file2.write(" ".join(line) + "\n")

my_file1.close()
my_file2.close()

# RECOMMANDÉ - fermeture automatique garantie
with open("foo.txt", "w", encoding="utf-8") as sortie:
    for i in range(2):
        sortie.write(f"{i}\n")

# Lire un fichier (mode par défaut)
with open("foo.txt", encoding="utf-8") as entree:
    for line in entree:
        print(line, end="")

# Ajouter du contenu
with open("foo.txt", "a", encoding="utf-8") as sortie:
    sortie.write("nouvelle ligne\n")

with open("fichier.txt", "w", encoding="utf-8") as f:
    f.write("déjà l'été\n")  # str

with open("fichier.txt", encoding="utf-8") as f:
    line = f.read()  # retourne un str
    print(type(line))  # <class 'str'>

# Lire TOUT le contenu
with open("foo.txt", encoding="utf-8") as entree:
    contenu = entree.read()
    print(contenu)

# Lire par blocs de 4 caractères
with open("foo.txt", encoding="utf-8") as entree:
    bloc1 = entree.read(4)  # 4 premiers caractères
    bloc2 = entree.read(4)  # 4 suivants

with open("log.txt", "w", encoding="utf-8") as f:
    f.write("Message important")
    f.flush()  # Force l'écriture immédiate sur disque

with open("fichier.txt", "w", encoding="utf-8") as f:
    f.write("déjà l'été\n")  # str

with open("fichier.txt", encoding="utf-8") as f:
    line = f.read()  # retourne un str
    print(type(line))  # <class 'str'>

with open("fichier.txt", "rb") as f:
    octets = f.read()  # retourne des bytes
    print(type(octets))  # <class 'bytes'>

with open("fichier.txt", "rb") as binfile:
    octets = binfile.read()
    for i, octet in enumerate(octets):
        print(f"{i} → {repr(chr(octet))} [{hex(octet)}]")

# Ancienne approche (Python < 3.4) - OBSOLÈTE

# Manipulation de chemins
os.path.join("dir", "file.txt")  # Construit un chemin
os.path.basename("/path/to/file")  # → 'file'
os.path.dirname("/path/to/file")  # → '/path/to'
os.path.abspath("file.txt")  # Chemin absolu

# Tests
os.path.exists("file.txt")  # Existe ?
os.path.isfile("file.txt")  # Est un fichier ?
os.path.isdir("dir")  # Est un répertoire ?

# Métadonnées
os.path.getsize("file.txt")  # Taille en octets
os.path.getmtime("file.txt")  # Date de modification

# Opérations
os.remove("file.txt")  # Supprimer fichier
os.rmdir("dir")  # Supprimer répertoire vide
os.removedirs("dir/subdir")  # Supprimer récursivement
os.rename("old.txt", "new.txt")  # Renommer

# Recherche
glob.glob("*.txt")  # Tous les fichiers .txt

# Nouvelle approche (Python ≥ 3.4) - RECOMMANDÉE

# Créer une instance associée à un fichier/répertoire
# path = Path('fichier-temoin')
# dirpath = Path('./data/')

path = Path("fichier.txt")
path.exists()

with open("fichier.txt", "w", encoding="utf-8") as f:
    f.write("0123456789\n")

# Obtenir toutes les métadonnées
# Retourne un namedtuple avec toutes les infos
path.stat()
path.stat().st_size  # Taille en octets

# Nombre de secondes depuis le 1er janvier 1970
mtime = path.stat().st_mtime

mtime_datetime = datetime.fromtimestamp(mtime)
print(mtime_datetime)  # → 2024-02-06 14:30:45

# Formater
print(f"{mtime_datetime:%H:%M}")  # → "14:30"

path.unlink()  # Supprime le fichier

# Méthode sûre (si le fichier pourrait ne pas exister)

try:
    path.unlink()
except FileNotFoundError:
    print("Fichier déjà supprimé")

path.name  # Attention : ATTRIBUT, pas méthode (pas de parenthèses)
# Créer un Path pour le répertoire
dirpath = Path("./data/")

# Utiliser glob() pour chercher
for json_file in dirpath.glob("*.json"):
    print(json_file)

dirpath.glob("*.txt")  # Tous les .txt
dirpath.glob("*.py")  # Tous les .py
dirpath.glob("test_*.py")  # Tous les test_*.py
dirpath.glob("**/*.json")  # Récursif (tous sous-répertoires)

type(path)

print(issubclass(PosixPath, Path))  # → True
print(isinstance(path, Path))  # → True

for channel in (sys.stdin, sys.stdout, sys.stderr):
    print(channel)

# Ouvrir un fichier destination
autre_stdout = open("ma_sortie.txt", "w", encoding="utf-8")

# Sauvegarder la référence originale
tmp = sys.stdout

# Sortie normale (terminal)
print("sur le terminal")

# REDIRECTION : remplacer stdout
sys.stdout = autre_stdout
print("dans le fichier")  # Écrit dans ma_sortie.txt

# RESTAURATION : remettre stdout original
sys.stdout = tmp

# Fermer le fichier
autre_stdout.close()

# Sortie de nouveau normale
print("de nouveau sur le terminal")

with open("ma_sortie.txt", encoding="utf-8") as check:
    print(check.read())  # Affiche : "dans le fichier\n"
