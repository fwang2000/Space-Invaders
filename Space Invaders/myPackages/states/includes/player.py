import pygame
import math

class Player:

	def __init__(self, x, y):

		self.x = x
		self.y = y
		self.xChange = 0
		self.img = pygame.image.load('images/spaceship.png').convert_alpha()
		self.bullet_free = True
		self.bullet = Bullet(self.x)

	def __str__(self):

		return "x: " + str(self.x) + ", y: " + str(self.y)

	def draw(self, screen):

		screen.blit(self.img, (self.x, self.y))

	def fire_bullet(self, screen):

		self.bullet_free = False
		self.bullet.x = self.x
		screen.blit(self.bullet.img, (self.bullet.x + 16, self.bullet.y + 10))

	def move_bullet(self, screen):

		self.bullet.y += self.bullet.yChange
		screen.blit(self.bullet.img, (self.bullet.x + 16, self.bullet.y + 10))

	def bullet_reset(self):

		self.bullet.y = 480
		self.bullet_free = True

	def hasHit(self, enemy):

		xCollision = self.bullet.x + self.bullet.width >= enemy.x + 5 and self.bullet.x + self.bullet.width//2 <= enemy.x + enemy.width - 5
		yCollision = self.bullet.y >= enemy.y and self.bullet.y <= enemy.y + enemy.height/2

		return xCollision and yCollision and not self.bullet_free


class Bullet:

	def __init__(self, x):

		self.img = pygame.image.load('images/bullet.png').convert_alpha()
		self.x = x
		self.y = 480
		self.yChange = -1.25
		self.width = self.img.get_size()[0]




