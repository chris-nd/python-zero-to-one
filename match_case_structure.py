def choix1(boisson):
    match boisson:
        case 1:
            #faire_cafe()
            print("Votre café est prêt !")
        case 2:
            #faire_cappuccino()
            print("Votre cappuccino est prêt !")
        case 3:
            #faire_the()
            print("Votre thé est prêt !")
        case 4:
            #faire_chocolat()
            print("Votre chocolat est prêt !")
        case _:
            print("Boisson inconnue !")

choix1(13)

# le pipe ‘|’ (or)
def c_pas_faux(mot):
    """Voir Kaamelott, épisode La botte secrète"""
    match mot:
        case "paradoxale"|"dichotomie":
            print("Ouais, c'est pas faux !")
        case "insipide"|"péremptoire":
            print("Non, j'connais pas c'mot la !")
        case _:
            print("Chante sloubi !")

c_pas_faux("paradoxale")
c_pas_faux("dichotomie")
c_pas_faux("insipide")
c_pas_faux("python")

# les nombres
def match_number(my_var):
    match my_var:
        case 8|-8:
            print("cas 1", type(my_var))
        case 3.14|-3.14:
            print("cas 2", type(my_var))
        case 2j|2+3j|2-3j:
            print("cas 3", type(my_var))
        case _:
            print("Pas un nombre")

lit_list = [8, -8, 3.14, -3.14, 2j, 2+3j, 2-3j]
for item in lit_list:
    match_number(item)

# les booléens
def match_bool(my_var):
    match my_var:
        case True:
            print("cas 1", True)
        case False:
            print("cas 2", False)
        case None:
            print("cas 3", None)
        case _:
            print("Pas un booléen.")

# 0 ne renvoie pas False et diffèrent de 0 ne renvoie pas True
bool_list = [True, False, None, 0, 1, bool(-10), bool(0), bool(1)]

for item in bool_list:
    match_bool(item)

# les chaînes
def match_string(my_var):
    match my_var:
        case (
             'simple quotes'
            |"double quotes"
            |"""triple quotes"""
        ):
            print("cas 1", type(my_var))
        case b"binary":
            print("cas 2", type(my_var))
        case r"raw string":
            print("cas 3", type(my_var))
        case _:
            print("autre")

string_list = ['simple quotes', 
               "double quotes",
               """triple quotes""",
               b"binary",
               r"raw string",
              "other"]
for item in string_list:
    match_string(item)

# les tuples
def odd_even(a, b):
    match(bool(a%2), bool(b%2)):
        case (False, False):
            print("a pair, b pair")
        case (False, True):
            print("a pair, b impair")
        case (True, True):
            print("a impair, b impair")   
        case (True, False):
            print("a impair, b pair")
        case _:
            print("Pas évaluable")

odd_even(1, 2)

# les listes
def action(player_input):
    match(player_input.split()):
        case ["go", "north"]: # ou ("go", "north")
            print("ok")
        case _:
            print("commande inconnue")

action("go north")

# unpacking
def choix(boisson):
    match boisson:
        case(1, sucre):
            print(f"Un café {sucre}.")
        
choix((1, "peu sucré"))

def choix(boisson):
    match boisson:
        # Valide uniquement si dans la séquence.
        case (1, ("non sucré"|"peu sucré"|"sucré"|"très sucré") as sucre):
            print(f"Un café {sucre}.")
        # Peu importe les deux premiers éléments, il y en a plus de deux.
        case (_, _, *args):
            print("argument inconnu ou trop d'arguments.")
        case _:
            print("Autre cas")
            
choix((1, "peu sucré"))
choix((1, "sucré", 8))
choix((1))