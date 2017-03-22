# -*- coding: UTF8 -*-
import pygame
from pygame.locals import*

from fonction import*

pygame.init()
pygame.font.init()

fenetre = pygame.display.set_mode((700,700))

fond = pygame.image.load("res/img/fond.png").convert_alpha()
fond_reviue = pygame.image.load("res/img/fond_Reviue.png").convert_alpha()
text_font = pygame.font.Font("res/lucon.ttf", 25)

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

#les nombres
c_un = pygame.image.load("res/img/Nombres/1.png").convert_alpha()

c_deux = pygame.image.load("res/img/Nombres/2.png").convert_alpha()

c_trois = pygame.image.load("res/img/Nombres/3.png").convert_alpha()

c_quatre = pygame.image.load("res/img/Nombres/4.png").convert_alpha()

c_cinq = pygame.image.load("res/img/Nombres/5.png").convert_alpha()

c_six = pygame.image.load("res/img/Nombres/6.png").convert_alpha()

c_sept = pygame.image.load("res/img/Nombres/7.png").convert_alpha()

c_huit = pygame.image.load("res/img/Nombres/8.png").convert_alpha()

c_neuf = pygame.image.load("res/img/Nombres/9.png").convert_alpha()

#les meme en inverser
c_unb = pygame.image.load("res/img/Nombres/1_blanc.png").convert_alpha()

c_deuxb = pygame.image.load("res/img/Nombres/2_blanc.png").convert_alpha()

c_troisb = pygame.image.load("res/img/Nombres/3_blanc.png").convert_alpha()

c_quatreb = pygame.image.load("res/img/Nombres/4_blanc.png").convert_alpha()

c_cinqb = pygame.image.load("res/img/Nombres/5_blanc.png").convert_alpha()

c_sixb = pygame.image.load("res/img/Nombres/6_blanc.png").convert_alpha()

c_septb = pygame.image.load("res/img/Nombres/7_blanc.png").convert_alpha()

c_huitb = pygame.image.load("res/img/Nombres/8_blanc.png").convert_alpha()

c_neufb = pygame.image.load("res/img/Nombres/9_blanc.png").convert_alpha()

c = [c_un, c_deux, c_trois, c_quatre, c_cinq, c_six, c_sept, c_huit, c_neuf]

c_blanc = [c_unb, c_deuxb, c_troisb, c_quatreb, c_cinqb, c_sixb, c_septb, c_huitb, c_neufb]

c_blanc_ch = [c_un, c_deuxb, c_troisb, c_quatreb, c_cinqb, c_sixb, c_septb, c_huitb, c_neufb]


#definition des rectangles
R_oui = bouton_oui.get_rect()
R_non = bouton_non.get_rect()
R_suivant = bouton_suivant.get_rect()

R_c = []
for a in c:
    R_c.append(a.get_rect())
R_c_blanc = R_c

#on remplace les retour chariot par rien, sinon il s'affiche dans pygame
def modifStr(string):
    s = ""
    for a in string:
        if a != "\n":
            s += a
    return s
