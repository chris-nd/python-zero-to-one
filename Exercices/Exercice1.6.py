def gestion_de_conversion(value):
    try:
        print(int(value))
    except:
        print("conversion impossible en entier")

gestion_de_conversion("123")
gestion_de_conversion("12.5")
gestion_de_conversion("hello")
gestion_de_conversion(45)
gestion_de_conversion(3.14)
gestion_de_conversion("3.74 + 0j")