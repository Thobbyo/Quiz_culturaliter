# -*- coding: UTF8 -*-
import random

from constante import*
from QuestionReponse import*

#on selectionne les question
def choixQuestion():
    lesQuestion = []
    hold = []

    #tant que l'on n'a pas 10 question
    while len(lesQuestion) < 9:
        val = random.randint(0, len(question)-1)
        if hold.count(val) == 0:
            qr = QuestionReponse(val)
            lesQuestion.append(qr)
            hold.append(val)

    return lesQuestion


def afficherB(bouton, R, x, y):
    fenetre.blit(bouton,(x, y))
    R[0 : 2] = [x, y]
    pygame.display.flip()
