import pygame
import sys
from variable import *
from importation_images import *
from fonctions_de_jeu import *

pygame.init()

pygame.display.set_caption("echec")

running = True

screen.blit(echiquier, (0, 0))
initialisation(coordonnées_cases)
piece_en_cours=None

while running:

  pygame.display.update()

  # loop through all events
  for event in pygame.event.get():
      # check the quit condition
    if event.type == pygame.QUIT:
      # quit the game
      pygame.quit()

    if event.type == pygame.MOUSEBUTTONUP :
      if piece_en_cours==None:
        piece_en_cours=selection_piece(pygame.mouse.get_pos(),tour)
        if piece_en_cours!= None:
          coups_jouables=coups_possible(piece_en_cours,tour)
          affiche_coups_possibles(coups_jouables)

      else:
        joue,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours=joue_piece(pygame.mouse.get_pos(),coups_jouables,piece_en_cours,tour)
        reaffichage()
        p=pion_derniere_ligne(pieces_blanches,pieces_noires)
        if p[0]==True:
          attente=True
          if tour==True:
            screen.blit(promotion_b,(50,50))
          else:
            screen.blit(promotion_n,(50,450))
          pygame.display.update()

          while attente:
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                pygame.quit()
              if event.type == pygame.MOUSEBUTTONUP:
                if promotion(pygame.mouse.get_pos(),p[1],tour):
                  attente=False

        if joue!=-1:
          piece_en_cours=None
          tour=not tour
          liste_coup_joué.append((pieces_blanches,pieces_noires,tour))

      if mat(tour)==True:
        print("et c'est un mat")
        fin=True
        while fin:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()



