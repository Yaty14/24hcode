import pygame
from pygame.locals import *

from personnage import *
from fenetre import *
from structure import *
from bloc import * 

jeu = game()
hanSolo = personnage(100,100)
bloc1 = bloc(100,100, 0)

pattern = structure(0, 3)

matPattern = [(100,100), (140,100), (180,100)]

for i in range(3):
	bloc1 = bloc(matPattern[i][0], matPattern[i][1], 0)
	pattern.addBloc(bloc)


boucle = 1
i = 0
while(boucle):
	pattern.afficher(jeu)
	hanSolo.afficher(jeu)
	i = i + 1

