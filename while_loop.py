a = list(range(1, 10))

while a:
    a.pop()
    print(a)

while a:
    a.pop() # Retire le dernier élément de la liste
    print(a)
    if len(a) == 5:
        continue # Passe à l'itération suivante

while True:
    s = input('Quelle est votre question ?\n')
    if 'aucune' in s:
        break # Quitte la boucle while

while True:
    if s.startswith('bonjour'):
        print("bonjour, comment allez-vous?")
    elif "bien" in s:
        print("c'est super !")
    elif "bye" in s:
        print("Au revoir !")
        break
    else:
        print("mais encore...")
    s = input()

# Un exemple de while avec une clause else

# si break_mode est vrai on va faire un break
# après le premier élément de la liste
def scan(liste, break_mode):

    # un message qui soit un peu parlant
    message = "avec break" if break_mode else "sans break"
    print(message)
    while liste:
        print(liste.pop())
        if break_mode:
            break
    else:
        print('else...')

# sortie de la boucle sans break
# on passe par else
scan(['a'], False)

# on sort de la boucle par le break
scan(['a'], True)