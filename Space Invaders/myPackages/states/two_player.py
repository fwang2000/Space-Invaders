import pygame
from pygame import mixer
from .includes.player import *
from .includes.enemy import *
from myPackages.states import game
from .. import prepare, tools
import sys

class Two_Player(game.Game):

	WIDTH = 800
	HEIGHT = 600
	FADE_IN = True

	def __init__(self):

		super().__init__()
		
		self.player = Player(300, self.HEIGHT * 0.8125)
		self.player2 = Player(500, self.HEIGHT * 0.8125)
		self.player2.img = pygame.image.load('images/spaceship2.png').convert_alpha()
		self.player2.bullet.img = pygame.image.load('images/bullet2.png').convert_alpha()

	def get_event(self):

		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_LEFT]:

			self.player.xChange = -0.3

		elif pressed[pygame.K_RIGHT]:

			self.player.xChange = 0.3

		else:

			self.player.xChange = 0

		if pressed[pygame.K_a]:

			self.player2.xChange = -0.3

		elif pressed[pygame.K_d]:

			self.player2.xChange = 0.3

		else:

			self.player2.xChange = 0
		
		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				pygame.quit()
				sys.exit(0)

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE and self.player.bullet_free:

					self.shoot(1)

				if event.key == pygame.K_q and self.player2.bullet_free:

					self.shoot(2)

	def update(self):

		super().update()
		self.update_player_and_bullet()

	def update_player_and_bullet(self):

		if self.player.bullet.y < 0:

			self.player.bullet_reset()

		if self.player2.bullet.y < 0:

			self.player2.bullet_reset()

		# Bullet Movement
		if not self.player.bullet_free:

			self.player.move_bullet(self.screen)

		if not self.player2.bullet_free:

			self.player2.move_bullet(self.screen)

		# Draw Player
		if self.player.x + self.player.xChange <= 800 - 64 and self.player.x + self.player.xChange >= 0:

			self.player.x += self.player.xChange

		if self.player2.x + self.player2.xChange <= 800 - 64 and self.player2.x + self.player2.xChange >= 0:

			self.player2.x += self.player2.xChange

		self.player.draw(self.screen)
		self.player2.draw(self.screen)

	def checkCollision(self, e):

		p1_hit = self.player.hasHit(self.currRound[e])
		p2_hit = self.player2.hasHit(self.currRound[e])

		collision = p1_hit or p2_hit

		if collision:

			self.currRound[e].lives -= 1

			if p1_hit:

				self.player.bullet_reset()

			else:

				self.player2.bullet_reset()

			self.explosion_sound()

			self.currRound[e].checkDamage()

			if self.currRound[e].lives == 0:
				
				self.currRound[e] = None
				self.num_of_enemies -= 1

	def shoot(self, player):

		fire = mixer.Sound('sounds/shoot.wav')
		fire.set_volume(0.3) 		
		fire.play()

		if player == 1:

			self.player.fire_bullet(self.screen)

		elif player == 2:

			self.player2.fire_bullet(self.screen)

	def reset(self):

		self.player = Player(300, self.HEIGHT * 0.8125)
		self.player2 = Player(500, self.HEIGHT * 0.8125)
		super().reset()