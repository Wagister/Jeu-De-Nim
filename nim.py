#! /usr/bin/env python3

def afficher_jeu(nombre_allumettes):
    """Affiche le plateau du jeu.

    :param nombre_allumettes: doit être positif ou nul.
    :type nombre_allumettes: int.
    """
    
    return "|" * nombre_allumettes


def prise_ia(nombre_allumettes, gagnant_dernier):
    """Implémentation de la statégie gagnante : donne le nombre
    d'allumettes à prendre en fonction de nombre restant et de la
    variante du jeu.

    :param nombre_allumettes: doit être positif ou nul.
    :type nombre_allumettes: int.
    :param gagnant_dernier: indique si celui qui prend la dernière
                            allumette est le gagnant.
    :type gagnant_dernier: bool.
    :returns: nombre d'allumettes à prendre.
    :rtype: int.
    """
    
    if nombre_allumettes <= 3: #C'est extrement chaotique mais en vrai j'en suis trop fier
        nombre_prendre = (nombre_allumettes * gagnant_dernier) + (nombre_allumettes - 1) * (not gagnant_dernier)
        return nombre_prendre + (nombre_prendre == 0)


def partie(nombre_allumettes, gagnant_dernier, ia_joueur_2):
    """Une seule partie du jeu de Nim.

    :param nombre_allumettes: nombre d'allumettes au début de la partie,
                              doit être positif ou nul.
    :type nombre_allumettes: int.
    :param gagnant_dernier: indique si celui qui prend la dernière
                            allumette est le gagnant.
    :type gagnant_dernier: bool.
    :param ia_joueur_2: indique si le joueur 2 est la machine (True)
                  ou l'utilisateur (False).
    :type ia_joueur_2: bool.
    """
    # À implémenter.
    pass


def afficher_message_bienvenue():
    """Affiche le message de bienvenue."""

    print("Bienvenue sur le jeu de Nim !")


def afficher_message_fin():
    """Affiche le message de fin."""
    
    print("Votre partie est terminée")


def reponse_oui_non(question):
    """Pose une question binaire (oui/non) à l'utilisateur qui répond
    soit 'o', soit 'n' (éventuellement 'O' ou 'N').
    La question est reposée tant que la réponse n'est pas comprise.

    :param question: la question à poser.
    :type question: str.
    :returns: la réponse sous forme de booléen.
    :rtype: bool.
    """
    
    reponse = input(question)
    if str.lower(reponse) == "o":
        return True
    elif str.lower(reponse) == "n":
        return False
    else:
        return reponse_oui_non(question)


def reponse_entier(question, vmin, vmax):
    """Pose une question à l'utilisateur dont la réponse est un entier
    compris dans l'intervalle [vmin ; vmax]. vmin >= 0.
    La question est reposée tant que la réponse n'est pas correcte.

    :param question: la question à poser.
    :type question: str.
    :param vmin: la valeur minimale possible (>=0).
    :type vmin: int.
    :param vmax: la valeur maximale possible (>= vmin).
    :type vmax: int.
    :returns: l'entier choisi.
    :rtype: int.
    """
    
    entier = input(question)
    try:
        entier = int(entier)

        if entier >= vmin and entier <= vmax:
            return entier
        else:
            return reponse_entier(question, vmin, vmax)
    except:
        return reponse_entier(question, vmin, vmax)


def jouer():
    """Lance le jeu de Nim.
    On peut lancer autant d'instances du jeu que l'on souhaite.
    L'utilisateur a le choix de rejouer à chaque fin de partie.
    """
    afficher_message_bienvenue()

    while True:
        # paramètres de la partie
        ia = reponse_oui_non("Jouer contre la machine ?")
        gagnant_dernier = reponse_oui_non(
            "Le gagnant est celui qui prend la dernière allumette ?")
        nombre_allumettes = reponse_entier("Combien d'allumettes ?", 1, 100)
        # lancement de la partie
        partie(nombre_allumettes, gagnant_dernier, ia)
        # on rejoue ?
        if not reponse_oui_non("Rejouer ?"):
            break

    afficher_message_fin()


if __name__ == "__main__":
    # si le programme est exécuté directement, on lance une partie
    jouer()