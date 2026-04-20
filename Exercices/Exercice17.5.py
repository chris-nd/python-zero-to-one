def open_file(file):
    fl = open(file, encoding="utf8")
    try:
        print(fl.read())
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        fl.close()

open_file("Exercices/Prompt.txt")
    