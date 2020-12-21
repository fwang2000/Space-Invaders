import pygame
from pygame import mixer
from .includes.player import *
from .includes.enemy import *
from myPackages.states import game
from .. import prepare, tools
import sys

class One_Player(game.Game):

	WIDTH = 800
	HEIGHT = 600
	FADE_IN = True

	def __init__(self):

		super().__init__()

		self.player = Player(self.WIDTH//2 - 32, self.HEIGHT * 0.8125)

	# ENEMIES

	def get_event(self):

		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_LEFT]:

			self.player.xChange = -0.3

		elif pressed[pygame.K_RIGHT]:

			self.player.xChange = 0.3

		else:

			self.player.xChange = 0
		
		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				pygame.quit()
				sys.exit(0)

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE and self.player.bullet_free:

					self.shoot()
				
	# UPDATE

	def update(self):

		super().update()
		self.update_player_and_bullet()
	
	def update_player_and_bullet(self):

		if self.player.bullet.y < 0:

			self.player.bullet_reset()

		# Bullet Movement
		if not self.player.bullet_free:

			self.player.move_bullet(self.screen)

		# Draw Player
		if self.player.x + self.player.xChange <= 800 - 64 and self.player.x + self.player.xChange >= 0:

			self.player.x += self.player.xChange

		self.player.draw(self.screen)

	def checkCollision(self, e):

		collision = self.player.hasHit(self.currRound[e])

		if collision:

			self.currRound[e].lives -= 1

			self.player.bullet_reset()
			self.explosion_sound()

			self.currRound[e].checkDamage()

			if self.currRound[e].lives == 0:
				
				self.currRound[e] = None
				self.num_of_enemies -= 1

	def shoot(self):

		fire = mixer.Sound('sounds/shoot.wav')
		fire.set_volume(0.3) 		
		fire.play()
		self.player.fire_bullet(self.screen)

	def reset(self):

		self.player = Player(self.WIDTH//2, self.HEIGHT * 0.8125)
		super().reset()