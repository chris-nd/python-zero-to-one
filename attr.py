"getattr, setattr, hasattr, delattr"

# La résolution des attributes s'éffectue dynamiquement au moment de l'exécution(runtime)
# alors que la liaison des variables s'effectue lexicalement et statiquement au moment de
# la compilation(compile time).

# getattr()
# permet de récupérer la valeur d'un attribut
class Person1:
    "Classe objet de type Person1"
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person1('John Doe', 30)

attr_name = input('Enter the attribute you want to see: ')
print(getattr(person, attr_name, 'Attribute not found'))


class Person2:
    "Classe objet de type Person2"
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person2('John Doe', 30)

# Boucle à travers tous les attributs de l'objet person avec la fonction dir()
for attr in dir(person):
    # Ignore les méthodes doubles comme __init__ ou __str__ et les méthodes régulières
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f'{attr}: {value}')


# setattr()
# permet de définir la valeur d'un attribut
def func():
    "documentation de la fonction foo"
    pass

setattr(func, "width", 100)

print("width:", func.width)


class Configuration:
    "Classe objet de type Configuration"
    pass

# Données chargées à l'exécution
# (comme avec un fichier de configuration ou d'une variable d'environnement)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Saisie dynamique des attributs en utilisant setattr()s
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec) # 30
print(config_obj.max_retries) # 5


# hasattr()
# permet de vérifier si un attribut existe dans l'espase de nommage de l'objet
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)

required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Produit manquant car l'attribut requis: '{attr}'")
    else:
        # Accès aux attributs dynamiquement une fois leur existence confirmée
        print(f'{attr}: {getattr(product_a, attr)}')

# Il est impossible de rajouter des attributs sur les
# types de base, car ce sont des classes immuables.
# C'est par contre possible sur virtuellement tout le reste:
# modules, packages, fonctions, classes, instances

for builtin_type in (int, str, float, complex, tuple, dict, set, frozenset):
    obj = builtin_type()
    try:
        obj.foo = 'bar'
    except AttributeError as e: 
        print(f"{builtin_type.__name__:>10} → exception {type(e)} - {e}")


# delattr()
# permet de supprimer un attribut de l'espace de nommage d'un objet
class UserSession2:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token # sensitive
        self.temp_counter = 0 # temporary

session = UserSession2(101, 'a1b2c3d4e5')

# Liste d'attributs à nettoyer dynamiquement avant "sauvegarder" la session
attributes_to_clean = ['auth_token', 'temp_counter']

# Supprimé dynamiquement les attributs spécifiés
for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')

# Bouclé à travers les attributs restants avec dir()
for attr in dir(session):
    # Ignorer les méthodes dunders comme __init__ ou __str__ et les méthodes régulières
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f' - {attr}: {getattr(session, attr)}')
