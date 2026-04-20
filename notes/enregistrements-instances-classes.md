## 1. Classe vs Dictionnaire

Un dictionnaire est pratique pour stocker des données brutes, mais une **classe** permet d'associer ces données à des **comportements** (méthodes).

### Comparaison

- **Dictionnaire :** Accès via clés (`p['nom']`), aucune validation, pas de méthodes métier.
- **Instance de classe :** Accès via attributs (`p.nom`), méthodes personnalisées (`p.sendmail()`), type métier explicite.

```python
class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
    
    def __repr__(self):
        return f"<<{self.nom}, {self.age} ans, email:{self.email}>>"
```

## 2. Flexibilité de Python : Ajouter des méthodes "à la volée"

En Python, les classes sont des objets comme les autres. Vous pouvez modifier leur comportement **après** leur définition initiale. C'est un trait puissant de la nature dynamique du langage.

### La technique d'extension dynamique

Il suffit d'affecter une fonction à un attribut de la classe. Notez que la fonction doit impérativement accepter `self` comme premier argument.

```python
def sendmail(self, subject, body):
    print(f"To: {self.email} - Subject: {subject}")

# Ajout dynamique à la classe
Personne.sendmail = sendmail

# Désormais, toutes les instances de Personne possèdent cette méthode
pierre = Personne('pierre', 25, 'pierre@foo.com')
pierre.sendmail("Bienvenue", "Bonjour Pierre !")
```

## 3. L'Encapsulation et le piège des attributs

Vous pourriez vous inquiéter : "Si je fais `pierre.age += 1` directement, ne casse-je pas l'encapsulation ?"

Dans de nombreux langages (Java/C++), on force l'utilisation de `getAge()` et `setAge()`. En Python, on préfère la simplicité. Si un jour vous avez besoin de calculer l'âge au lieu de le stocker, vous utiliserez une **`@property`** (décorateur) qui permet de transformer un accès attribut en un appel de fonction, **sans changer la syntaxe du code utilisateur**.

## Synthèse : Ce qu'il faut retenir

- **Instances comme enregistrements :** Elles rendent le code plus lisible et permettent d'ajouter de la logique (méthodes).
- **Méthodes dynamiques :** Vous pouvez injecter des fonctionnalités dans une classe en cours d'exécution. C'est utile pour le *patching* ou l'extension de bibliothèques tierces, bien que cela doive rester une pratique exceptionnelle.
- **Simplicité avant tout :** Contrairement au C++/Java, Python ne vous impose pas de rendre les attributs "privés". Utilisez la convention de l'underscore (`self._age`) pour indiquer ce qui est interne, mais gardez votre interface publique la plus simple possible.
    
    **Le concept de `@property` dont j'ai parlé est fondamental pour l'encapsulation élégante en Python.**