def div(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Attension division par zero")
    except TypeError:
        print("Il faut des int")
    print("continuons")

div(10, 2)
div(10, 0)
div(10, "a")

def div2(a, b):
    try:
        print(a / b)
    except:
        print("Attention division par zero")
    print("continuons")

div2(10, 2)
div2(10, 0)
div2(10, "a")

def div3(a, b):
    print(a / b)

def f(x):
    div3(1, x)

print(f(2))
print(f(0))

# une fonction qui fait des choses après un return
def return_with_finally(number):
    try:
        return 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
        return("zero-divide")
    finally:
        print("on passe ici même si on a vu un return")

print(return_with_finally(1))
print(return_with_finally(0))

# pour montrer la clause else dans un usage banal
def function_with_else(number):
    try:
        x = 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
    else:
        print("on passe ici seulement avec un nombre non nul")
    return 'something else'

print(function_with_else(1))
print(function_with_else(0))

# la clause else ne traverse pas les return
def return_with_else(number):
    try:
        return 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
        return("zero-divide")
    else:
        print("on ne passe jamais ici à cause des return")

print(return_with_else(1))
print(return_with_else(0))

def check_age(age):
    if age < 0:
        raise ValueError('Age ne peut pas être négatif')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age ne peut pas être négatif


def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: données invalides reçues')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')


def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Fichier de configuration manquant') from None
    except ValueError as e:
        raise ValueError('Format de configuration invalide') from e

config = parse_config('config.txt')
