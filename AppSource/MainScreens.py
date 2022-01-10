import pygame 
from Classes import *

def startScreen(DISPLAYSURF):
	#initialize variables
	pygame.font.init() 
	clock = pygame.time.Clock()
	running = True

	#create fonts
	subFont = pygame.font.SysFont('Courier New', 30)
	headFont = pygame.font.SysFont('Courier New', 100)

	#get size of screen 
	screenWidth, screenHeight = pygame.display.get_surface().get_size()

	#place the title button in the middle of the screen 35% down
	titleText = TextButton("clicker", headFont, (0, 255, 0), (0, 255, 0))
	titleX = (int)(0.5 * screenWidth) - (titleText.getWidth() * 0.5)
	titleY = (int)(0.35 * screenHeight) - (titleText.getHeight() * 0.5)
	titleText.setXPos(titleX)
	titleText.setYPos(titleY)

	#palce the start button in the middle of the screen and 65% down
	startButton = TextButton("start", subFont, (0, 255, 0), (255, 0, 0))
	startX = (int)(0.5 * screenWidth) - (startButton.getWidth() * 0.5)
	startY = (int)(0.65 * screenHeight) - (startButton.getHeight() * 0.5)
	startButton.setXPos(startX)
	startButton.setYPos(startY)

	#place the settings button in the middle of the screen and 75% down
	settingsButton = TextButton("settings", subFont, (0, 255, 0), (255, 0, 0))
	settingsX = (int)(0.5 * screenWidth) - (settingsButton.getWidth() * 0.5)
	settingsY = (int)(0.75 * screenHeight) - (settingsButton.getHeight() * 0.5)
	settingsButton.setXPos(settingsX)
	settingsButton.setYPos(settingsY)

	#main screen loop
	while running: 
			
		DISPLAYSURF.fill((0, 0, 0))
		#Check for inputs 
		for event in pygame.event.get():
			#Kill the game if escape is pressed	
			if (event.type == pygame.KEYDOWN):
				if(event.key == pygame.K_ESCAPE):
					return "EXIT"
			if (event.type == pygame.MOUSEBUTTONUP):
				if(startButton.mouseIsOver()):
					print("start")
					return "START"
				elif(settingsButton.mouseIsOver()):
					print("settings")
					return "SETTINGS"

		
		#draw text buttons
		titleText.draw(DISPLAYSURF)
		startButton.draw(DISPLAYSURF)
		settingsButton.draw(DISPLAYSURF)

		pygame.display.flip()
		clock.tick(80)	

