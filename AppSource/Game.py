#Import necessary modules
import pygame 
from Classes import *
from MainScreens import *

#Start pygame
pygame.init()

#Create the display for the game
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#Variables to be used by the game itself
activeCircle = Circle()
gameSession = Game()
gameSession.setDifficulty("EASY")
running = True
statusCode = "TITLE"

while running:
	#display the starting screen
	if(statusCode == "TITLE"):
		statusCode = startScreen(DISPLAYSURF)
		continue
	elif(statusCode == "START"):
		#Play the game 
		statusCode = gameSession.play(DISPLAYSURF)
		continue
	else: 
		running = False

#End Pygame
pygame.quit()