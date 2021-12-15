#! /usr/bin/env python3

import nim


def test_prise_ia():
     # À faire !
     assert False


def capturer_appel(func, *args):
    """Retourne l'affichage produit par la fonction func
    sous forme de chaîne de caractère.
    Le saut de ligne de fin est supprimé.
    """
    from io import StringIO
    import sys

    tmp = sys.stdout
    sys.stdout = StringIO()
    func(*args)
    res = sys.stdout.getvalue()
    sys.stdout = tmp
    if res.endswith('\n'):
        res = res[:-1]
    return res


def faux_input_multi(func, inputs_str, *args):
    """Retourne la valeur d'une fonction (du module nim)
    faisant appel à plusieurs input comme si les éléments de inputs_str
    étaient passés à stdin.
    """
    from io import StringIO
    import sys

    inputs = iter(inputs_str)

    def fake_input(*margs):
        return next(inputs)
    nim.input = fake_input

    tmp = sys.stdout
    sys.stdout = StringIO()

    res = func(*args)

    nim.input = input
    sys.stdout = tmp
    return res


def faux_input(func, input_str, *args):
    """Retourne la valeur d'une fonction (du module nim)
    faisant appel à input comme si input_str était passé à stdin.
    """
    return faux_input_multi(func, (input_str,), *args)


def test_afficher_jeu():
    # on teste si le nombre d'allumettes affichées est le bon
    for nombre_allumettes in range(1, 101):
        assert len(capturer_appel(nim.afficher_jeu, nombre_allumettes)) == nombre_allumettes


def test_reponse_oui_non():
    # on teste si le booléen renvoyé est le bon
    assert faux_input(nim.reponse_oui_non, "o", "ma question")
    assert not faux_input(nim.reponse_oui_non, "n", "ma question")
    assert faux_input(nim.reponse_oui_non, "O", "ma question")
    assert not faux_input(nim.reponse_oui_non, "N", "ma question")

    assert faux_input_multi(nim.reponse_oui_non,
                            ("x", "1", "12", "o"), "ma question")

    assert not faux_input_multi(nim.reponse_oui_non,
                                ("z", "0", "-3", "n"), "ma question")


def test_reponse_entier():
    # on test si l'entier retourné est le bon
    for x in [1, 50, 100]:
        assert faux_input(nim.reponse_entier,
                          str(x), "ma question", 1, 100) == x
    assert faux_input(nim.reponse_entier, "1", "ma question", 1, 1) == 1
    assert faux_input(nim.reponse_entier, "2", "ma question", 1, 2) == 2

    assert faux_input_multi(nim.reponse_entier, ("q", "1", "0"),
                            "ma question", 0, 0) == 0

    assert faux_input_multi(nim.reponse_entier, ("z", "0", "-3", "5"),
                            "ma question", 1, 10) == 5


def tester():
    import inspect
    import sys

    fonctions_test = [(obj, nom) for nom, obj in inspect.getmembers(sys.modules[__name__])
                      if inspect.isfunction(obj) and nom.startswith('test_')]
    ntests = len(fonctions_test)
    passes = 0
    for i, (test, nom) in enumerate(fonctions_test):
        print("{}/{}\t".format(i + 1, ntests),
              (nom[5:] + " " * 20)[:20], "\t", end="")
        try:
            test()
            print("OK")
            passes += 1
        except Exception as e:
            print("échec /!\\ (", type(e).__name__, ")", sep="")
    print("Synthèse : {}/{} tests passés ({:.01f}%)".format(
        passes, ntests, passes/ntests*100))


if __name__ == "__main__":
    # si le programme est exécuté directement, on lance la fonction de test
    tester()
