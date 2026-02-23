print("""
      
      Concersion de temperature

      1 - Celsius à Fahrenheit
      2 - Celsius à Kelvin

      3 - Fahrenheit à Kelvin
      4 - Fahrenheit à Celsius

      5 - Kelvin à Celsius
      6 - Kelvin à Fahrenheit

      """)

option = int(input("Choisir une option de conversion selon le numéro :"))
temp = int(input("Entrer la valeur à convertir :"))

if option == 1:
    F = (temp * 1.8) + 32
    print(F)
elif option == 2:
    K = temp + 273.15
    print(K)
elif option == 3:
    K = (temp + 459.67) / 1.8
    print(K)
elif option == 4:
    C = (temp - 32) / 1.8
    print(C)
elif option == 5:
    C = temp - 273.15
    print(C)
elif option == 6:
    F = (temp * 1.8) - 459.67
    print(F)

