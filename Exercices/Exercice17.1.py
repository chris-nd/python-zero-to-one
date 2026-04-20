def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print(f"Erreur : {e}")

divide(10, 0)
divide(12, 2)
