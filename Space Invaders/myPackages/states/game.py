import pygame
from datetime import datetime, timedelta
from pygame import mixer
from .includes.player import *
from .includes.enemy import *
from .includes.rounds import *
from .. import prepare, tools

class Game(tools._State):

	WIDTH = 800
	HEIGHT = 600
	FADE_IN = True

	def __init__(self):

		super().__init__()
		self.next = "END_LOSE"

		self.screen = tools._State._getscreen(self)
		self.background = pygame.image.load('images/background.jpg').convert()

		self.rounds = Rounds()

		# GAME TRACKERS
		self.roundCount = 0
		self.currRound = []
		self.num_of_enemies = 0
		self.printRound = True
		self.alpha = 255

		# FONTS
		self.score_font = pygame.font.Font('8bit.ttf', 14)
		self.small_font = pygame.font.Font('8bit.ttf', 24)
		self.title_font = pygame.font.Font('8bit.ttf', 32)

		self.endTime = 0
		self.countdownTime = True

	# ENEMIES

	def get_event(self):

		raise NotImplementedError("Must be overloaded in subclass")

	def draw(self):

		self.screen.fill((0, 0, 0))

		self.screen.blit(self.background, (0, 0));

		self.show_score(10, 10)

		if self.printRound:

			self.show_round(self.roundCount)

			if self.countdownTime: 

				self.endTime = datetime.now() + timedelta(seconds=5)
				self.countdownTime = False

			elif self.endTime < datetime.now():

				self.fade_text()
				

	# UPDATE

	def update(self):

		if self.FADE_IN:

			self.fade_in(self.WIDTH, self.HEIGHT)
			self.FADE_IN = False

		if self.num_of_enemies == 0:

			self.update_round()

		if self.roundCount > 10: 

			self.reset()
			self.next = "END_WIN"
			self.done = True

		self.draw()

		self.update_enemies()

	def fade_text(self):

		if self.alpha > 0:

			self.alpha -= 1

		else:

			self.printRound = False

	def fade_in(self, width, height):

		fade = pygame.Surface((width, height))
		fade.fill((0, 0, 0))
		for alpha in range(0, 300):

			fade.set_alpha(299 - alpha)
			self.draw()
			self.screen.blit(fade, (0, 0))
			pygame.display.update()

	def update_round(self):

		self.roundCount += 1
		self.currRound = self.rounds.selection(self.roundCount, self.WIDTH)
		self.num_of_enemies = self.rounds.getEnemyCount()
		self.printRound = True
		self.countdownTime = True
		self.alpha = 255

	def update_enemies(self):

		for e in range(len(self.currRound)):

			if self.currRound[e] is not None:

				self.draw_enemy(self.currRound[e])
				self.move_enemy(self.currRound[e])
				self.checkGameOver(e)
				self.checkCollision(e)

	def checkCollision(wave, enemy):

		raise NotImplementedError("Must be overloaded in subclass")

	def checkGameOver(self, e):

		if self.currRound[e].y > self.HEIGHT - 32:

			self.reset()
			self.done = True

	def draw_enemy(self, enemy):

		self.screen.blit(enemy.img, (enemy.x, enemy.y))

	def move_enemy(self,enemy):

		enemy.x += enemy.xChange
		enemy.y += enemy.yChange
		enemy.changeDirection()

	def explode(self, x, y):

		t_end = datetime.now() + timedelta(seconds=2)

		while datetime.now() < t_end:

			self.screen.blit(e_img, (x, y))

	def explosion_sound(self):

		explosion = mixer.Sound('sounds/invaderkilled.wav')
		explosion.set_volume(0.3)
		explosion.play()

	# TEXT

	def show_score(self, x, y):

		score_text = self.score_font.render("Enemies Left " + str(self.num_of_enemies), True, (255, 255, 255))
		self.screen.blit(score_text, (x, y))

	def show_round(self, round):

		round_text = self.title_font.render("Round " + str(round), True, (255, 255, 255))
		alpha_img = pygame.Surface(round_text.get_size(), pygame.SRCALPHA)
		# Fill it with white and the desired alpha value.
		alpha_img.fill((255, 255, 255, self.alpha))
		# Blit the alpha surface onto the text surface and pass BLEND_RGBA_MULT.
		round_text.blit(alpha_img, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
		text_rect = round_text.get_rect(center=(int(self.WIDTH//2), int(self.HEIGHT//2)))
		self.screen.blit(round_text, text_rect)

	def reset(self):

		self.rounds = Rounds()

		self.roundCount = 0
		self.currRound = []
		self.num_of_enemies = 0
		self.printRound = True
		self.alpha = 255

		self.endTime = 0
		self.countdownTime = True