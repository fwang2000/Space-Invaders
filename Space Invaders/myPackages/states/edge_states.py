import pygame
import random
from datetime import datetime, timedelta
from queue import *
from .includes.myThread import *
from .includes.enemy import *
import time
from .. import prepare, tools
import sys

class EdgeState(tools._State):

	WHITE = (255, 255, 255)
	LIGHT_BLUE = (0, 255, 255)
	WIDTH = 800
	HEIGHT = 600

	# TEXT

	SMALL_FONT = pygame.font.Font('8bit.ttf', 20)
	TITLE_FONT = pygame.font.Font('8bit.ttf', 32)

	def __init__(self, next_state, title_caption, button1_caption, button2_caption):

		super().__init__()
		self.next = next_state

		self.screen = tools._State._getscreen(self)
		self.background = pygame.image.load('images/background.jpg').convert()

		# TEXT

		self.title_caption = title_caption
		self.button1_caption = button1_caption
		self.button2_caption = button2_caption

		self.title = self.TITLE_FONT.render(title_caption, True, (255, 255, 255))
		self.title_rect = self.title.get_rect(center=(int(self.WIDTH//2), int(200)))

		self.button_1_text = self.SMALL_FONT.render(button1_caption, True, self.WHITE)
		self.button_2_text = self.SMALL_FONT.render(button2_caption, True, self.WHITE)

		self.button_1_rect = self.button_1_text.get_rect(center=(275, 325))
		self.button_2_rect = self.button_2_text.get_rect(center=(515, 325))

		self.keyboard = False
		self.click = False
		self.done = False

		self.lefthighlight = False
		self.righthighlight = False

		self.enemies = []
		self.endTime = 0
		self.countdownTime = True
		self.append_new = True

	def get_event(self):
		
		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				pygame.quit()
				sys.exit(0)

			if event.type == pygame.MOUSEBUTTONDOWN:

				if event.button == 1:

					if self.button_1_rect.collidepoint((self.mx, self.my)) or self.button_2_rect.collidepoint((self.mx, self.my)):

						self.click = True

			elif event.type == pygame.KEYDOWN:

				if event.key == pygame.K_RETURN:

					if self.lefthighlight:

						self.click = True
						self.left_button_highlight()

					elif self.righthighlight:

						self.click = True
						self.right_button_highlight()

				elif event.key == pygame.K_LEFT:

					self.keyboard = True
					self.left_button_highlight()

				elif event.key == pygame.K_RIGHT:

					self.keyboard = True
					self.right_button_highlight()

	def update(self):

		self.draw()
		self.check_button_click()

	def draw(self):

		self.screen.blit(self.background, (0, 0))	
		self.draw_random_enemy()	
		self.screen.blit(self.title, self.title_rect)
		self.screen.blit(self.button_1_text, self.button_1_rect)
		self.screen.blit(self.button_2_text, self.button_2_rect)

	def draw_random_enemy(self):

		if self.append_new:

			self.append_enemy()

			if self.countdownTime:

				self.endTime = datetime.now() + timedelta(seconds=5)
				self.append_new = False

		if self.enemies[0].y >= self.HEIGHT:

			self.enemies.pop(0)
			print(len(self.enemies))

		if self.endTime < datetime.now():

			self.append_new = True

		for enemy in self.enemies:

			self.screen.blit(enemy.img, (enemy.x, enemy.y))
			enemy.x += enemy.xChange
			enemy.y += enemy.yChange
			enemy.changeDirection()

	def append_enemy(self):

		num = random.randint(0, 19)

		if num <= 10:

			self.enemies.append(SimpleEnemy(random.randint(16, self.WIDTH - 32), -32))

		elif num >= 11 and num <= 13:

			self.enemies.append(RacingEnemy(random.randint(32, self.WIDTH - 64), -64))

		elif num >= 14 and num <= 16:

			self.enemies.append(MediumEnemy(random.randint(32, self.WIDTH - 64), -64))

		else:

			self.enemies.append(HeavyEnemy(random.randint(64, self.WIDTH - 128), -128))

	def fade_out(self, width, height):

		fade = pygame.Surface((width, height))
		fade.fill((0, 0, 0))
		for alpha in range(0, 300):

			fade.set_alpha(alpha)
			self.draw()
			self.screen.blit(fade, (0, 0))
			pygame.display.update()

	def check_button_click(self):

		self.mx, self.my = pygame.mouse.get_pos()

		if self.button_1_rect.collidepoint((self.mx, self.my)):

			self.left_button_highlight()
			self.keyboard = False

		elif self.button_2_rect.collidepoint((self.mx, self.my)):

			self.right_button_highlight()
			self.keyboard = False

		elif not self.keyboard:

			self.reset_right()
			self.reset_left()

	def left_button_highlight(self):

		self.button_1_rect = self.button_1_text.get_rect(center=(275, 315))
		self.button_1_text = self.SMALL_FONT.render(self.button1_caption, True, self.LIGHT_BLUE)
		self.reset_right()
		self.lefthighlight = True

		if self.click:

			self.fade_out(self.WIDTH, self.HEIGHT)
			self.state_reset()
			self.done = True

	def reset_right(self):

		self.button_2_rect = self.button_2_text.get_rect(center=(515, 325))
		self.button_2_text = self.SMALL_FONT.render(self.button2_caption, True, self.WHITE)
		self.righthighlight = False

	def right_button_highlight(self):

		raise NotImplementedError("Must be overloaded in subclass")

	def reset_left(self):

		self.button_1_rect = self.button_1_text.get_rect(center=(275, 325))	
		self.button_1_text = self.SMALL_FONT.render(self.button1_caption, True, self.WHITE)
		self.lefthighlight = False

	def state_reset(self):

		self.click = False
		self.lefthighlight = False
		self.righthighlight = False

		self.enemies = []
		self.endTime = 0
		self.countdownTime = True
		self.append_new = True
