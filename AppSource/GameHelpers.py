import pygame
from Classes import *
from random import randint

#determine circle radius based on difficulty of the game
def genCircleRadius(gameSession):
	if(gameSession.getDifficulty() == "EASY"):
		return 40
	elif(gameSession.getDifficulty() == "MEDIUM"):
		return 30
	elif(gameSession.getDifficulty() == "HARD"):
		return 20
	else: return 40 #default to easy mode if not set

def randomizeCirclePosition(circle):
	width, height = pygame.display.get_surface().get_size()
	circle.setXPos((int)(width * 0.01 * randint(15, 85))) #randomize XPosition to a value between 15% and 5% of the screen's width
	circle.setYPos((int)(height * 0.01 * randint(15, 85))) #randomize YPosition to a value between 15% and 85% of the screen's height