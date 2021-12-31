#Import necessary modules
import pygame 
from Classes import *

#Start pygame
pygame.init()

#Create the display for the game
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#Variables to be used by the game itself
activeCircle = Circle()
gameSession = Game()
gameSession.setDifficulty("EASY")

#Play the game 
gameSession.play(DISPLAYSURF)

#End Pygame
pygame.quit()