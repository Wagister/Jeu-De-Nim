#! /usr/bin/env python3
from PIL import Image
from random import randint
from tkinter import Image as tkImage
import turtle
import os


def afficher_jeu(nombre_allumettes, texture=str(os.getcwd()) + "\skins\Allumette.gif"):
    """Affiche le plateau du jeu.

    :param nombre_allumettes: doit être positif ou nul.
    :type nombre_allumettes: int.
    :param texture: chemin de latexture de l'allumette.
    :type texture: str.
    """
    texture = Image.open(texture)

    espacement = 10
    largeur_texture, hauteur_texture = texture.size
    largeur_jeu = (largeur_texture + espacement) * nombre_allumettes - espacement
    
    jeu = Image.new("RGBA", (largeur_jeu, hauteur_texture), (255, 255,  255, 0))
    for i in range(nombre_allumettes):
        jeu.paste(texture, (i * (largeur_texture + espacement), 0))
    jeu = jeu.save("Jeu.gif", "GIF", transparency=0)

    wn.addshape("Jeu.gif")
    affichage_jeu.shape("Jeu.gif")


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
    
    if nombre_allumettes <= 3:
        #La première parenthèse est prise en compte que si gagnant_dernier est True (Donc égale à 1, sinon la parenthèse est multipliée par 0)
        #Si elle est prise en compte, elle prend toute les allumettes (Donc nombre_allumettes * 1)
        #La seconde est prise en compte si gagnant_dernier est False (Donc égale à 0 mais inversé grâce au "not")
        #Si elle est prise en compte elle essayera de laisser 1 allumette (Donc nombre_allumettes - 1)
        nombre_prendre = (nombre_allumettes * gagnant_dernier) + ((nombre_allumettes - 1) * (not gagnant_dernier))
        
        #Empêche de retourner 0 ou 4 (Si nombre_prendre == 0 est True alors sa revient à écrire 1, donc 0 + 1. Idem avec nombre_prendre == 4 sauf qu'on soustrait)
        return nombre_prendre + (nombre_prendre <= 0) - (nombre_prendre > 3)
    else:
        #En gros si l'IA laisse un multiple de 4 (ou un multiple de 4 + 1 selon gagnant_dernier)
        nombre_prendre = nombre_allumettes % 4 + (not gagnant_dernier)
        
        #Et la sa vérifie que le resultat est pas en dessous de 0 ou au dessus de 3, sinon sa prend un nombre aléatoire (Car elle panique)
        return (nombre_prendre * (nombre_prendre > 0 and nombre_prendre <= 3)) + (randint(1, 3) * (nombre_prendre <= 0 or nombre_prendre > 3))


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
    if ia_joueur_2:
        premier = reponse_oui_non("Voulez vous jouer en premier ?")
    else:
        j1 = str(input("Renseignez le nom du Joueur 1 :"))
        j2 = str(input("Renseignez le nom du Joueur 2 :"))
        premier = reponse_oui_non(str(j1+" joue-t-il en premier ?")) #j'ai quand même pris 2 minutes à me rendre compte qu'il fallait un +

    while nombre_allumettes > 1:
        if ia_joueur_2 and premier:        
            nbj = reponse_entier("Combien d'allumettes voulez-vous retirer ? 1, 2 ou 3 ?",1,3)
            nbia = prise_ia(nombre_allumettes, gagnant_dernier)
        elif premier:
            nbj1 = reponse_entier("Combien d'allumettes "+j1+" veut retirer ? 1, 2 ou 3 ?",1,3)
            nbj2 = reponse_entier("Combien d'allumettes "+j2+" veut retirer ? 1, 2 ou 3 ?",1,3)
        elif ia_joueur_2:
            nbia = prise_ia(nombre_allumettes, gagnant_dernier)
            nbj = reponse_entier("Combien d'allumettes voulez-vous retirer ? 1, 2 ou 3 ?",1,3)
        else:
            nbj2 = reponse_entier("Combien d'allumettes "+j2+" veut retirer ? 1, 2 ou 3 ?",1,3)


def afficher_message_bienvenue():
    # À ne pas faire.
    pass


def afficher_message_fin():
    # À ne pas faire.
    pass


def reponse_oui_non(question):
    """Pose une question binaire (oui/non) à l'utilisateur qui répond
    soit 'o', soit 'n' (éventuellement 'O' ou 'N').
    La question est reposée tant que la réponse n'est pas comprise.

    :param question: la question à poser.
    :type question: str.
    :returns: la réponse sous forme de booléen.
    :rtype: bool.
    """
    
    reponse = turtle.textinput("Question", question)
    if reponse is None:
        return reponse_oui_non(question)
    elif str.lower(reponse) == "o":
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
    
    nombre = wn.numinput("Question", question, vmin, minval=vmin, maxval=vmax)
    if nombre is None:
        return reponse_entier(question, vmin, vmax)
    else:
        return int(nombre)


def jouer():
    """Lance le jeu de Nim.
    On peut lancer autant d'instances du jeu que l'on souhaite.
    L'utilisateur a le choix de rejouer à chaque fin de partie.
    """

    # affichage de la partie
    global wn
    wn = turtle.Screen()
    wn.title("Jeu de Nim")
    wn._root.iconphoto(True, tkImage("photo", file=str(os.getcwd()) + r"\textures\Icon.png"))
    wn.setup(0.5, 0.5)

    global affichage_jeu
    affichage_jeu = turtle.Turtle()
    
    afficher_message_bienvenue()

    while True:
        # paramètres de la partie
        ia_joueur_2 = reponse_oui_non("Voulez-vous jouer contre la machine ?")
        gagnant_dernier = reponse_oui_non(
            "Le gagnant est-il celui qui prend la dernière allumette ?")
        nombre_allumettes = reponse_entier("Avec combien d'allumettes voulez-vous jouer ?", 1, 100)

        # lancement de la partie
        partie(nombre_allumettes, gagnant_dernier, ia_joueur_2)

        # on rejoue ?
        afficher_jeu(nombre_allumettes)
        if not reponse_oui_non("Voulez-vous rejouer ?"):
            break

    afficher_message_fin()

def creer_bouton(x, y, texture, fonction):
    """ Créer un bouton tout gentil tout mignon.
    
    :param x: position x du bouton.
    :type x: int.
    :param y: position Y du bouton.
    :type y: int.
    :param y: texture du bouton.
    :type y: str.
    :param fonction: fonction à executer lors de l'appui.
    :type fonction: func.
    """
    
    wn.addshape(texture)

    bouton = turtle.Turtle()
    bouton.shape(texture)
    bouton.penup()
    bouton.goto(x, y)

    def click(x, y):
        fonction()

    bouton.onclick(click, btn=1, add=True)
    
def print_skins():
    skins_dir = str(os.getcwd()) + "\skins"
    
    for file in os.listdir(skins_dir):
        if file.endswith(".gif"):
            skin = Image.open(os.path.join(skins_dir, file))
            afficher_jeu(16, skin)
    
def print_bonjour():
    print("Bonjour")


if __name__ == "__main__":
    # si le programme est exécuté directement, on lance une partie
    global wn
    wn = turtle.Screen()
    wn.title("Jeu de Nim")
    wn._root.iconphoto(True, tkImage("photo", file=str(os.getcwd()) + r"\textures\Icon.png"))
    wn.setup(0.5, 0.5)

    creer_bouton(0, 110, str(os.getcwd()) + r"\textures\Solo.gif", print_bonjour)
    creer_bouton(0, 4, str(os.getcwd()) + r"\textures\Duo.gif", print_bonjour)
    creer_bouton(0, -102, str(os.getcwd()) + r"\textures\Casier.gif", print_bonjour)
    creer_bouton(0, -208, str(os.getcwd()) + r"\textures\Boutique.gif", print_bonjour)

    turtle.mainloop()
