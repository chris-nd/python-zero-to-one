def display(string):
    print(f"Chaîne originale : {string}")
    print(f"UTF8 : {string.encode("utf-8")}")
    print(f"Latin 1 : {string.encode("latin-1")}")
    
    try:
        print(f"ASCII : {string.encode("ascii")}")
    except UnicodeEncodeError:
        print("ASCII : Impossible (caractères non-ASCII présents)")

display("Héllo Wörld")