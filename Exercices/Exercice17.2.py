def str_to_integer(data):
    try:
        print(int(data))
    except ValueError as e:
        print(f"Erreur : {e}")

str_to_integer("123")
str_to_integer("abc")
str_to_integer("45.5")
