import pygame
import random
import math

class Enemy():

	def __init__(self, img, x, y, xChange, yChange, width, height):

		self.img = img
		self.x = x
		self.y = y	
		self.xChange = xChange
		self.yChange = yChange
		self.width = width
		self.height = height

	def changeDirection(self):

		raise NotImplementedError("Subclass must implement this abstract method")

	def draw(self, screen):

		screen.blit(self.img, (self.x, self.y))

class SimpleEnemy(Enemy):

	def __init__(self, x, y):

		self.lives = 1
		self.img = pygame.image.load('images/si.png').convert_alpha()
		self.x = x - 16
		self.originalX = self.x
		self.y = y
		self.xChange = 0.03
		self.yChange = 0.0145
		self.width = self.img.get_size()[0]
		self.height = self.img.get_size()[1]

		super().__init__(self.img, self.x, self.y, self.xChange, self.yChange, self.width, self.height)

	def changeDirection(self):

		if self.x > self.originalX + 20:

			self.x = self.originalX + 20
			self.xChange *= -1

		elif self.x < self.originalX - 20:

			self.x = self.originalX - 20
			self.xChange *= -1

	def checkDamage(self):

		pass

class RacingEnemy(Enemy):

	def __init__(self, x, y):

		self.lives = 2
		self.img = pygame.image.load('images/ufo.png').convert_alpha()
		self.x = x
		self.y = y
		self.xChange = 0.36 * random.randrange(-1, 2, 2)
		self.yChange = 0.02
		self.width = self.img.get_size()[0]
		self.height = self.img.get_size()[1]

		super().__init__(self.img, self.x, self.y, self.xChange, self.yChange, self.width, self.height)

	def changeDirection(self):

		if self.x <= 0 or self.x >= 736:

			self.xChange *= -1

	def checkDamage(self):

		if self.lives == 1:

			self.img = pygame.image.load('images/ufo_damaged.png').convert_alpha()

class MediumEnemy(Enemy):

	def __init__(self, x, y):

		self.lives = 5
		self.img = pygame.image.load('images/medium.png').convert_alpha()
		self.x = x - 32
		self.y = y
		self.xChange = 0
		self.yChange = 0.0145
		self.width = self.img.get_size()[0]
		self.height = self.img.get_size()[1]

		super().__init__(self.img, self.x, self.y, self.xChange, self.yChange, self.width, self.height)

	def changeDirection(self):

		if self.x <= 0:

			self.xChange *= -1

	def checkDamage(self):

		if self.lives == 1:

			self.img = pygame.image.load('images/medium_damaged2.png').convert_alpha()
			self.yChange = 0.1

		elif self.lives == 3:

			self.img = pygame.image.load('images/medium_damaged1.png').convert_alpha()
			self.yChange = 0.05

class HeavyEnemy(Enemy):

	def __init__(self, x, y):

		self.lives = 10
		self.img = pygame.image.load('images/heavy.png').convert_alpha()
		self.x = x - 64
		self.y = y
		self.xChange = 0
		self.yChange = 0.015
		self.width = self.img.get_size()[0]
		self.height = self.img.get_size()[1]

		super().__init__(self.img, self.x, self.y, self.xChange, self.yChange, self.width, self.height)

	def changeDirection(self):

		if self.x <= 0 or self.x >= 800 - 128:

			self.xChange *= -1

	def checkDamage(self):

		if self.lives == 2: 

			self.img = pygame.image.load('images/heavy_damaged2.png').convert_alpha()

		elif self.lives == 4:

			self.img = pygame.image.load('images/heavy_damaged1.png').convert_alpha()

		elif self.lives == 7:

			self.img = pygame.image.load('images/heavy_damaged.png').convert_alpha()