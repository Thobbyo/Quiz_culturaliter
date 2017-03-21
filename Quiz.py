import pygame
from pygame.locals import*

from fonction import*
from constante import*
from QuestionReponse import*

result = choixQuestion()

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

            afficherB(bouton_non, R_non, 300, 500)
            
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
                fenetre.blit(text_font.render(" Correct, en effet :", 2, (0, 0, 0), (255, 255, 255)), (50, 50))
            else:
                fenetre.blit(text_font.render(" Faux, en effet :", 2, (0, 0, 0), (255, 255, 255)), (50, 50))

            a.afficherE()

            afficherB(bouton_suivant, R_suivant, 300, 500)
            
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

    """#affichage d'une reviue
    for a in result:

        #pour une question/reponse
        while res != -1:

            a.afficherE()

            afficherB(bouton_suivant, R_suivant, 300, 500)
            
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
"""
   
pygame.font.quit()
pygame.quit()
