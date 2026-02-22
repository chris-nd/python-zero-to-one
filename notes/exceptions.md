## `try`...`else`...`finally`

### Structure complète d'un `try`

Au-delà des clauses `except`, on peut ajouter :

- **`else`** : exécutée si **aucune exception** n'est levée
- **`finally`** : exécutée **quoi qu'il arrive** (exception ou pas)

**Ordre obligatoire :**

```python
try:
    # code à surveiller
except ExceptionType:
    # gestion de l'exception
else:
    # exécuté si pas d'exception
finally:
    # exécuté dans tous les cas
```

### La clause `finally` (très utile)

**Objectif :** Faire du nettoyage dans **tous les cas de figure**.

**Caractéristique unique :** S'exécute **même après un `return`** !

**Exemple :**

```python
def return_with_finally(number):
    try:
        return 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
        return "zero-divide"
    finally:
        print("on passe ici même si on a vu un return")
```

**Test sans exception :**

```python
return_with_finally(1)
# Affiche :
# on passe ici même si on a vu un return
# Retourne : 1.0
```

**Test avec exception :**

```python
return_with_finally(0)
# Affiche :
# OOPS, <class 'ZeroDivisionError'>, division by zero
# on passe ici même si on a vu un return
# Retourne : "zero-divide"
```

**Point clé :** `finally` s'exécute **toujours**, même quand il y a un `return` dans `try` ou `except`.

### La clause `else` (moins courante)

**Objectif :** Code exécuté **seulement si aucune exception** n'est levée.

**Différence subtile avec mettre le code à la fin du `try` :**

> *"The use of the `else` clause is better than adding additional code to the `try` clause because it avoids accidentally catching an exception that wasn't raised by the code being protected by the `try` … `except` statement."*
> 

**Traduction :** Si le code dans `else` lève une exception, elle **ne sera pas** attrapée par les `except` du `try` courant → sera propagée.

**Exemple :**

```python
def function_with_else(number):
    try:
        x = 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
    else:
        print("on passe ici seulement avec un nombre non nul")
    return 'something else'
```

**Test sans exception :**

```python
function_with_else(1)
# Affiche :
# on passe ici seulement avec un nombre non nul
# Retourne : 'something else'
```

**Test avec exception :**

```python
function_with_else(0)
# Affiche :
# OOPS, <class 'ZeroDivisionError'>, division by zero
# Retourne : 'something else'
```

### `else` ne traverse PAS les `return`

**Contrairement à `finally`, `else` ne s'exécute pas après un `return` :**

```python
def return_with_else(number):
    try:
        return 1/number  # return direct
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
        return "zero-divide"  # return dans except
    else:
        print("on ne passe jamais ici à cause des return")
```

**Test :**

```python
return_with_else(1)  # Retourne 1.0
# else n'est PAS exécuté car return dans try

return_with_else(0)  # Retourne "zero-divide"
# else n'est PAS exécuté car return dans except
```

### Flux d'exécution complet

**Cas 1 : Aucune exception**

```python
try:
    code_normal()      # ✅ Exécuté
except:
    gestion_erreur()   # ❌ Pas exécuté
else:
    code_succes()      # ✅ Exécuté
finally:
    nettoyage()        # ✅ Exécuté
```

**Cas 2 : Exception levée et attrapée**

```python
try:
    code_erreur()      # ✅ Exécuté (lève exception)
except:
    gestion_erreur()   # ✅ Exécuté
else:
    code_succes()      # ❌ Pas exécuté
finally:
    nettoyage()        # ✅ Exécuté
```

**Cas 3 : Exception non attrapée**

```python
try:
    code_erreur()      # ✅ Exécuté (lève exception non gérée)
except AutreException:
    gestion()          # ❌ Pas exécuté
else:
    code_succes()      # ❌ Pas exécuté
finally:
    nettoyage()        # ✅ Exécuté (puis exception propagée)
```

### Points clés à retenir

1. **`finally`** : exécuté **toujours**, même après `return`
2. **`else`** : exécuté **seulement si pas d'exception**
3. **`finally`** rappelle les context managers (nettoyage garanti)
4. **`else`** évite d'attraper accidentellement des exceptions
5. **Ordre obligatoire** : `try` → `except` → `else` → `finally`
6. En pratique : **`finally` fréquent**, `else` rare