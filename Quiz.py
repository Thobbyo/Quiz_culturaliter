# -*- coding: UTF8 -*-
import pygame
from pygame.locals import*

from fonction import*
from constante import*
from QuestionReponse import*

result = choixQuestion()

#on limite le nombre de fps
pygame.time.Clock().tick(60)

while not exit:

    fenetre.blit(fond, (0,0))

    #pour chaque question
    for a in result:
        
        res = -1

        fenetre.blit(fond, (0,0))

        #pour une question
        while res == -1:
            
            a.afficherQ()

            afficherB(bouton_oui, R_oui, 100, 500)

            afficherB(bouton_non, R_non, 500, 500)
            
            #on regarde si on clique dessus
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        
                        if R_oui.collidepoint(event.pos) == True:
                            res = 1

                        if R_non.collidepoint(event.pos) == True:
                            res = 0

                #requete de fermeture de la fenetre
                if event.type == pygame.QUIT:
                    exit = True
                    res = -10
                    break
    
            pygame.display.flip()

        if res == -10:
           break

        fenetre.blit(fond, (0,0))
        
        #pour une reponse
        while res != -1:

            if a.ValiderReponse(res):
                fenetre.blit(text_font.render(" Correct, en effet :", 2, (0, 0, 0), (255, 255, 255)), (50, 100))
            else:
                fenetre.blit(text_font.render(" Faux, en effet :", 2, (0, 0, 0), (255, 255, 255)), (50, 100))

            a.afficherE()

            afficherB(bouton_suivant, R_suivant, 300, 550)
            
            #on regarde si on passe au suivant
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:

                        if R_suivant.collidepoint(event.pos) == True:
                            res = -1

                #requete de fermeture de la fenetre
                if event.type == pygame.QUIT:
                    exit = True
                    res = -10
                    break
    
            pygame.display.flip()

        if res == -10:
           break

    pygame.display.flip()

    #affichage d'une reviue
    end = 0
    ss = 0
    while end == 0:

        fenetre.blit(fond_reviue, (0, 0))
        
        x = 80
        y = 200
        for a in range(len(c)):
            fenetre.blit(c_blanc_ch[a], (x, y))
            R_c[a][0:2] = [x, y]
            x += 63

        result[ss].afficherE()
        
        result[ss].afficherQ()
        
        afficherB(bouton_suivant, R_suivant, 300, 550)

        pygame.display.flip()
        
        #on regarde si on clique dessus
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:

                    x = 85
                    for a in range(len(R_c)):
                        x += 63
                        if R_c[a].collidepoint(event.pos) == True:
                            ss = a
                            for b in range(len(c_blanc_ch)):
                                c_blanc_ch[b] = c_blanc[b]
                                c_blanc_ch[a] = c[a]

                    if R_suivant.collidepoint(event.pos) == True:
                            exit = True
                            res = -10
                            end = 1
                            break

                #requete de fermeture de la fenetre
                if event.type == pygame.QUIT:
                    exit = True
                    res = -10
                    break
    
            pygame.display.flip()

        if res == -10:
           break
   
pygame.font.quit()
pygame.quit()
