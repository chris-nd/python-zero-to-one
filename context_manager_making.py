"Implémentation de la conception d'un context manager"

from contextlib import contextmanager
import time

# Un context manager est un objet qui définit les méthodes __enter__ et __exit__.
# Il permet de gérer les ressources de manière propre, même en cas d'erreur,
# de finaliser certaines opérations en sortant du contexte, ce qui permet
# de libérer des ressources

# Implémentation du protocole de context manager
class Timer:
    "Classe objet de type Timer pour mesurer le temps d'exécution"

    # Cette méthode s'exécute àprès l'évaluation de l'expression with
    # sur l'objet instancié et retourne un objet accessible via un alias
    # pour ensuite enter dans la contexte
    def __enter__(self):
        self.start = time.time()
        return self

    # Cette methode s'exécute lorsque l'on sort
    # du contexte ou qu'une exception est lancée.
    # La méthode doit retourner un booléen

    # False: En cas d'exception, l'exception va être remontée le long de la
    # traceback et va arrêté le programme. Donc ne supprime pa l'exception

    # True: En cas d'exception, l'exception va être capturé par l'instruction
    # with et ne vas pas remontée le long de la trackback

    # Il est important, lorsqu’on conçoit un context manager, de bien propager
    # les exceptions qui ne sont pas liées au fonctionnement attendu du context manager.
    # Par exemple un objet de type fichier va par exemple devoir attraper les exceptions
    # liées à la fin du fichier, mais doit par contre laisser passer une exception
    # comme ZeroDivisionError.

    def __exit__(self, *args):
        duree = time.time() - self.start
        print(f"Temps d'exécution: {duree}s")
        print(args)
        print("Le type d'exception est:", args[0])
        print("La valeur d'exception est:", args[1])
        print("La trace d'exception est:", args[2])
        return False

    def __str__(self):
        duree =  time.time() - self.start
        return f"Temps intermédiaire: {duree}s"

with Timer() as t:
    sum(x for x in range(10_000_000))
    print(t)
    # En cas d'exception
    # print(1/0)
    sum(x**2 for x in range(10_000_000))


class Timer2:
    "Classe objet de type Timer pour mesurer le temps d'exécution"

    def __enter__(self):
        print("\nEntering Timer1")
        self.start = time.time()
        # rappel : le retour de __enter__ est ce qui est passé
        # à la clause `as` du `with`
        return self

    # Si l'on sort du bloc `with` sans qu'une exception soit levée,
    # ces trois arguments valent `None`;

    # Si une exception est levée, ils permettent d'accéder
    # respectivement au type, à la valeur de l'exception,
    # et à l'état de la pile lorsque l'exception est levée.
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            # pas d'exception levée dans le corps du 'with'
            print(f"Total duration {time.time()-self.start:2f}")
            # dans ce cas la valeur de retour n'est pas utilisée
        else:
            # il y a eu une exception de type 'exc_type'
            if exc_type in (ZeroDivisionError,) :
                print("on étouffe")
                # on peut l'étouffer en retournant True
                return True
            else:
                print(f"OOPS : on propage l'exception "
                      f"{exc_type} - {exc_value}")
                # et pour ça il suffit... de ne rien faire du tout
                # ce qui renverra None

# avec une exception filtrée
try:
    with Timer2():
        time.sleep(0.5)
        1/0
except Exception as e:
    # on va bien recevoir cette exception
    print(f"OOPS -> {type(e)}")

# avec une autre exception 
try:
    with Timer2():
        time.sleep(0.5)
        raise OSError()
except Exception as e:
    # on va bien recevoir cette exception
    print(f"OOPS -> {type(e)}")

# Création d'un context mananger avec la librairie 'contextlib'

# La bibliothèque contextlib offre des utilitaires pour définir
# un contextmanager sous une forme compacte à l'aide d'une fonction
# génératrice et du décorateur @contextmanager
@contextmanager
def compact_timer(message: str):
    """
    Un context manager pour mesurer le temps d'exécution.

    Args:
        message (str): Le message à afficher avec la durée.
    """
    start = time.time()
    yield
    print(f"{message}: durée = {time.time() - start}s")

with compact_timer("Temps d'exécution"):
    print(sum(x**2 for x in range(10**5)))
