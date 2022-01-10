import pygame 
from Classes import *

def startScreen(DISPLAYSURF):
	pygame.font.init() 
	Font = pygame.font.SysFont('Times New Roman', 30)
	clock = pygame.time.Clock()
	running = True
	text = TextButton("Start", Font, (0, 255, 0), (255, 0, 0), 800, 800)
	while running: 
			
		DISPLAYSURF.fill((0, 0, 0))
		#Check for inputs 
		for event in pygame.event.get():
			#Kill the game if escape is pressed	
			if (event.type == pygame.KEYDOWN):
				if(event.key == pygame.K_ESCAPE):
					running = False
		
		text.draw(DISPLAYSURF)

		pygame.display.flip()
		clock.tick(80)	

