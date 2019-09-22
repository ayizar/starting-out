from pygame.locals import *
import pygame
import math
from time import sleep

class MouseTrap(pygame.sprite.Sprite):

    def __init__(self, a, b):
        super().__init__()

        self.image = pygame.Surface([50, 240])

        self.image = pygame.image.load("images\mousetrap.png").convert_alpha()


        self.rect = self.image.get_rect(center = (-300, 240))

        self.rect.x = -300

        self.rect.y = 240