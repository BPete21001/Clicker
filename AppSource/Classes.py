import pygame 
from random import randint
from GameHelpers import *

#Class to store the information about any given circle on the screen
class Circle(object):
	#constructor for all fields
	def __init__(self, radius, color): 
		self.radius = radius
		self.color = color
		self.xPos = 0
		self.yPos = 0
	#default constructor 
	def __init__(self):
		self.radius = 20
		self.color = (255, 255, 255)
		self.xPos = 0
		self.yPos = 0
	#Radius mutator
	def setRadius(self, radius):
		self.radius = radius
	#Color mutator
	def setColor(self, color):
		self.color = color
	#xPos mutator
	def setXPos(self, xPos):
		self.xPos = xPos
	#yPos mutator
	def setYPos(self, yPos):
		self.yPos = yPos
	#Radius accessor
	def getRadius(self):
		return self.radius
	#Color accessor
	def getColor(self):
		return self.color
	#xPos accessor
	def getXPos(self):
		return self.xPos
	#yPos accessor
	def getYPos(self):
		return self.yPos

#Class to store information about the running game
class Game(object):
	#Class declaration method with number of circles and difficuly included
	def __init__ (self, totalCircles, difficulty):
		self.totalCircles = totalCircles
		self.hits = 0
		self.misses = 0
		self.endTime = 999
		self.difficulty = difficulty
	#Class declaration method for no parameters. Defaults to Easy mode with 10 circles
	def __init__(self):
		self.totalCircles = 10
		self.hits = 0
		self.misses = 0
		self.endTime = 999
		self.difficulty = "EASY"
	#Mutator for total circles field
	def setTotalCircles(self, circles):
		self.totalCircles = circles
	#Mutator for Hits field
	def setHits(self, hits):
		self.hits = hits
	#Mutator for misses field
	def setMisses(self, misses):
		self.misses = misses
	#Mutator for EndTime field
	def setEndTime(self, endTime):
		self.endTime = endTime
	#Mutator for Difficulty field
	def setDifficulty(self, difficulty):
		self.difficulty = difficulty
	#Mutator for total circles field
	def getTotalCircles(self):
		return self.totalCircles
	#Mutator for Hits field
	def getHits(self):
		return self.hits
	#Mutator for misses field
	def getMisses(self):
		return self.misses
	#Mutator for EndTime field
	def getEndTime(self):
		return self.endTime
	#Mutator for Difficulty field
	def getDifficulty(self):
		return self.difficulty
	#Method to execute the playing of the game
	def play(self, DISPLAYSURF):
		
		running = True
		activeCircle = Circle()
		activeCircle.setRadius(genCircleRadius(self))
		activeCircle.setColor((255,255,255));
		activeCircle.setXPos(250);
		activeCircle.setYPos(150);

		clock = pygame.time.Clock()

		while running: 
				
			DISPLAYSURF.fill((0, 0, 0))
			#Check for inputs 
			for event in pygame.event.get():
				#Kill the game if escape is pressed	
				if (event.type == pygame.KEYDOWN):
					if(event.key == pygame.K_ESCAPE):
						running = False

				if(event.type == pygame.MOUSEBUTTONUP):
					randomizeCirclePosition(activeCircle)
					print("X: " + str(activeCircle.getXPos()))
					print("Y: " + str(activeCircle.getYPos()))

			pygame.draw.circle(DISPLAYSURF, activeCircle.getColor(), (activeCircle.getXPos(), activeCircle.getYPos()), activeCircle.getRadius())
			pygame.display.flip()
			clock.tick(40)	

#Class to store information about text to me used as a button
class TextButton(object):
	def __init__(self, text, font, color, hoverColor, xPos, yPos):
		self.text = text
		self.font = font 
		self.color = color 
		self.hoverColor = hoverColor 
		self.xPos = xPos
		self.yPos = yPos
	def draw(self, DISPLAYSURF):
		#if the mouse is over the button, change to its hover color and draw to screen
		if(self.mouseIsOver):
			buttonImage = self.font.render(self.text, True, self.hoverColor)
		else:
			buttonImage = self.font.render(self.text, True, self.color)
		DISPLAYSURF.blit(buttonImage, (self.xPos, self.yPos))
	def mouseIsOver(self):
		#Create button image using same information to get dimensions
		buttonImage = self.font.render(self.text, True, self.color)
		width, height = buttomImage.get_size()

		#get mouse position
		mouseX, mouseY = pygame.mouse.get_pos()

		#return true if the mouse is currently over the object
		if(mouseX > self.xPos and (mouseX < self.xPos + width)):
			if(mouseY > self.yPos and (mouseY < self.yPos + height)):
				return True

		#return false if it is not
		return False
