import pygame
from pygame.locals import*

from fonction import*

pygame.init()
pygame.font.init()

fenetre = pygame.display.set_mode((720,720))

fond = pygame.image.load("res/img/fond.png").convert_alpha()
text_font = pygame.font.Font("res/lucon.ttf", 40)

#test de boucle infini
exit = False

question = []
reponse = []
explication = []
result = []

with open("res/eqr/q.txt", "r") as fichier:
    for a in fichier:
        question.append(a)

with open("res/eqr/r.txt", "r") as fichier:
    for a in fichier:
        reponse.append(a)

with open("res/eqr/e.txt", "r") as fichier:
    for a in fichier:
        explication.append(a)

#les boutons
bouton_oui = pygame.image.load("res/img/B_oui.png").convert_alpha()

bouton_non = pygame.image.load("res/img/B_non.png").convert_alpha()

bouton_suivant = pygame.image.load("res/img/B_suivant.png").convert_alpha()

#definition des rectangles
R_oui = bouton_oui.get_rect()
R_non = bouton_non.get_rect()
R_suivant = bouton_suivant.get_rect()

#on remplace les retour chariot par rien, sinon il s'affiche dans pygame
def modifStr(string):
    s = ""
    for a in string:
        if a != "\n":
            s += a
    return s
