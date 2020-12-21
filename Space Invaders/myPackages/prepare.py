'''
This module initializes the display, music and game elements
'''

import pygame
from pygame import mixer
from .states.includes.player import *
from .states.includes.rounds import *

SCREEN_SIZE = (800, 600)
CAPTION = "Space Invaders"

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption(CAPTION)
icon = pygame.image.load('images/si.png')
pygame.display.set_icon(icon)

# Background sound
music = mixer.music.load('sounds/8bitmusic.wav')
mixer.music.set_volume(0.2)
mixer.music.play(-1)