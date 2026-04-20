## 1. Problème de départ : encapsulation

- En Python, on accède souvent directement aux attributs :
    
    ```python
    t.kelvin
    ```
    
- Mais ça pose un problème :
    
    👉 aucune vérification (ex : température négative ❌)
    

---

## 2. Solution classique (Java / C++) : getter & setter

- On utilise :
    
    ```python
    get_kelvin()
    set_kelvin()
    ```
    
- Avantage :
    
    ✅ contrôle des données (ex : empêcher valeurs invalides)
    
- Inconvénients :
    
    ❌ syntaxe lourde
    
    ❌ code moins lisible
    
    ❌ casse les anciens usages (`t.kelvin`)
    

---

## 3. Solution Python : les *properties*

Permet de garder une **syntaxe simple** tout en ajoutant du contrôle

### Principe :

- On écrit des méthodes internes :
    
    ```python
    _get_kelvin()
    _set_kelvin()
    ```
    
- Puis on crée une *property* :
    
    ```python
    kelvin = property(_get_kelvin, _set_kelvin)
    ```
    

### Résultat :

- On utilise toujours :
    
    ```python
    t.kelvin = -30
    ```
    
- MAIS en réalité :
    
    du code s’exécute en arrière-plan (validation, transformation…)
    

---

## 4. Avantages des properties

✅Encapsulation forte

✅ Code propre et lisible

✅ Compatible avec l’accès direct (`t.kelvin`)

✅ Standard en Python (pas de `get_` / `set_` dans les API)

---

## 5. Exemple avancé : plusieurs unités

- Une classe peut exposer plusieurs attributs :
    - `kelvin`
    - `celsius`
    - `fahrenheit`
- MAIS en réalité :
    
    👉 une seule vraie donnée : `_kelvin`
    
- Les properties :
    - font les conversions automatiquement
    - vérifient les valeurs (ex : pas de Kelvin négatif)

👉 Exemple :

```python
t.celsius = 100
```

➡️ converti automatiquement en Kelvin

---

## 6. Bonus

- On peut aussi définir un **deleter** :
    
    ```python
    del t.kelvin
    ```
    
- Mais seulement si on le programme

---

## Conclusion

Les *properties* permettent de :

- garder une **syntaxe simple (comme un attribut)**
- tout en ajoutant une **logique interne (comme des méthodes)**

👉 C’est la solution Python parfaite pour :

**simplicité + encapsulation + puissance**