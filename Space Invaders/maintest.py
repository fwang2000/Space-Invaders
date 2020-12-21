import pygame
import random
import math
import threading
import time
from datetime import datetime, timedelta
from pygame import mixer
from myPackages.states.includes.player import *
from myPackages.states.includes.enemy import *
from myPackages.states.includes.rounds import *

# Initialize Game
pygame.init()
width = 800
height = 600

# Screen Created
screen = pygame.display.set_mode((width, height))

# Background
background = pygame.image.load('images/background.jpg')

# Background sound
music = mixer.music.load('sounds/8bitmusic.wav')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/si.png')
pygame.display.set_icon(icon)

# Directions:
directions = [1, -1] #[right, left]

# Score

font = pygame.font.Font('8bit.ttf', 14)
textX = 10
textY = 10

# Game Over

gameOver = False
g_font = pygame.font.Font('8bit.ttf', 32)

# Rounds

rounds = Rounds()

# Restart

r_font = pygame.font.Font('8bit.ttf', 24)

# Player
player = Player(width, height)

e_img = pygame.image.load('images/explosion.png')	

# Game's Infinite Loop
running = True

num_of_enemies = 0
roundCount = 6
timer = 0
printRound = True
getRoundTime = True
gameWon = False	

def draw_enemy(enemy):

	screen.blit(enemy.img, (enemy.x, enemy.y))

def remove_enemy(wave, enemy):

	wave[enemy] = None

def explode(x, y):

	t_end = datetime.now() + timedelta(seconds=2)

	while datetime.now() < t_end:

		screen.blit(e_img, (x, y))

def show_score(x, y):

	score_text = font.render("Enemies Left " + str(num_of_enemies), True, (255, 255, 255))
	screen.blit(score_text, (x, y))

def show_round(round):
	round_text = g_font.render("Round " + str(round), True, (255, 255, 255))
	text_rect = round_text.get_rect(center=(int(width//2), int(height//2)))
	screen.blit(round_text, text_rect)

def move_enemy(enemy):

	enemy.x += enemy.xChange
	enemy.y += enemy.yChange
	enemy.changeDirection()

def game_over_text(gameWon):

	if gameWon:

		g_text = g_font.render("You Won", True, (255, 255, 255))

	else: 

		g_text = g_font.render("Game Over", True, (255, 255, 255))

	text_rect = g_text.get_rect(center=(int(width//2), 250))
	screen.blit(g_text, text_rect)

def restart_text():

	r_text = r_font.render("Play Again", True, (255, 255, 255))
	text_rect = r_text.get_rect(center=(int(width//2), 350))
	screen.blit(r_text, text_rect)

def quit_text():

	q_text = r_font.render("Quit", True, (255, 255, 255))
	text_rect = q_text.get_rect(center=(int(width//2), 400))
	screen.blit(q_text, text_rect)

def play_again():

	pass

def explosion_sound():

	explosion = mixer.Sound('sounds/invaderkilled.wav')
	explosion.set_volume(0.3)
	explosion.play()

def checkCollision(wave, e, num_of_enemies):

	collision = player.hasHit(wave[e])

	if collision:

		wave[e].lives -= 1

		player.bullet_reset()
		explosion_sound()

		wave[e].checkDamage()

		if wave[e].lives == 0:
			
			wave[e] = None
			num_of_enemies -= 1

while running:

	# RGB
	screen.fill((0, 0, 0))

	# Background
	screen.blit(background, (0, 0))

	# Update Round
	if num_of_enemies == 0:

		roundCount += 1
		currRound = rounds.selection(roundCount, width)
		num_of_enemies = rounds.getEnemyCount()
		printRound = True

	if roundCount > 10:

		gameWon = True
		gameOver = True
		printRound = False
		end_time = datetime.now() + timedelta(seconds=3)

	if printRound:

		show_round(roundCount)

		if getRoundTime:

			r_time = datetime.now() + timedelta(seconds=5)
			getRoundTime = False

		if datetime.now() > r_time:

			printRound = False
			getRoundTime = True		

	if gameOver:

		restart = False
		game_over_text(gameWon)

		restart_text()
		quit_text()
		play_again()

		if datetime.now() > end_time:

			break
	
	else: 

		# Score
		show_score(textX, textY)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				running = False

			# Check Right or Left Keystroke
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_LEFT:

					player.xChange = -1.2

				if event.key == pygame.K_RIGHT:

					player.xChange = 1.2

				if event.key == pygame.K_SPACE and player.bullet_free == True:

					fire = mixer.Sound('sounds/shoot.wav')
					fire.set_volume(0.3) 		
					fire.play()
					player.fire_bullet(screen)

			if event.type == pygame.KEYUP:

				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

					player.xChange = 0

		# Draw Enemy

		for wave in currRound:

			for e in range(len(wave)):

				if wave[e] is not None:

					wave[e].draw(screen)

					if wave[e].y > player.y:

						gameOver = True
						end_time = datetime.now() + timedelta(seconds=3)
						break 

					# Update Enemy
					move_enemy(wave[e])

					# Collision
					checkCollision(wave, e, num_of_enemies)

			else: 

				continue

			break


		if player.bullet.y < 0:

			player.bullet_reset()

		# Bullet Movement
		if not player.bullet_free:

			player.move_bullet(screen)

		# Draw Player
		if player.x + player.xChange <= 800 - 64 and player.x + player.xChange >= 0:

			player.x += player.xChange

		player.draw(screen)

	# Update Display
	pygame.display.update()