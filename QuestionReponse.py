import pygame
from pygame.locals import*

from constante import*
from fonction import*


class QuestionReponse:


    def __init__(self, num):
        self.num = num
        self.laQuestion = modifStr(question[num])
        self.laReponse = modifStr(reponse[num])
        self.lExplication = modifStr(explication[num])
        self.resultat = -1;


    def afficherQ(self):
        x = 100
        y = 100
        s = ""
        for a in self.laQuestion:
            if a != "#":
                s += a
            elif a == "#":
                fenetre.blit(text_font.render(" " + s + " ", 2, (0, 0, 0), (255, 255, 255)), (x, y))
                y += 41
                s = ""
        fenetre.blit(text_font.render(" " + s + " ", 2, (0, 0, 0), (255, 255, 255)), (x, y))


    def afficherE(self):
        x = 100
        y = 200
        s = ""
        for a in self.lExplication:
            if a != "#":
                s += a
            elif a == "#":
                fenetre.blit(text_font.render(" " + s + " ", 2, (0, 0, 0), (255, 255, 255)), (x, y))
                y += 41
                s = ""
        fenetre.blit(text_font.render(" " + s + " ", 2, (0, 0, 0), (255, 255, 255)), (x, y))


    def ValiderReponse(self, resp):
        if(resp == int(modifStr(self.laReponse))):
            self.resultat = 1
            return True
        self.resultat = 0
        return False
