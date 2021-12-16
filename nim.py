#! /usr/bin/env python3

from turtle import *

def afficher_jeu(nombre_allumettes): #C'est assez long et désordonné, ça aurait pu être plus réduit je pense, mais j'ai un peu la flemme de réfléchir.
    """Affiche le plateau du jeu.
    :param nombre_allumettes: doit être positif ou nul.
    :type nombre_allumettes: int.
    """
    bgcolor("green")
    speed("fastest")
    for i in range(nombre_allumettes):
        penup()
        goto(-300+i*12,0)
        pendown()
        color("beige")
        begin_fill()
        left(180)
        forward(5)
        left(90)
        forward(25)
        left(90)
        forward(5)
        left(90)
        forward(25)
        end_fill()
        color("red")
        begin_fill()
        forward(5)
        left(90)
        forward(5)
        left(90)
        forward(5)
        left(90)
        forward(5)
        end_fill()
        penup()
    done()

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
    
    if nombre_allumettes <= 4:
        #La première parenthèse est prise en compte que si gagnant_dernier est True (Donc égale à 1, sinon la parenthèse est multipliée par 0)
        #Si elle est prise en compte, elle prend toute les allumettes (Donc nombre_allumettes * 1)
        #La seconde est prise en compte si gagnant_dernier est False (Donc égale à 0 mais inversé grâce au "not")
        #Si elle est prise en compte elle essayera de laisser 1 allumette (Donc nombre_allumettes - 1)
        nombre_prendre = (nombre_allumettes * gagnant_dernier) + ((nombre_allumettes - 1) * (not gagnant_dernier)) 
        
        #Empêche de retourner 0 ou 4 (Si nombre_prendre == 0 est True alors sa revient à écrire 1, donc 0 + 1. Idem avec nombre_prendre == 4 sauf qu'on soustrait)
        return nombre_prendre + (nombre_prendre == 0) - (nombre_prendre == 4)


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

    print("Bienvenue sur le jeu de Nim !") #30 secondes à faire


def afficher_message_fin():
    """Affiche le message de fin."""
    
    print("Votre partie est terminée") #30 secondes à faire


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
