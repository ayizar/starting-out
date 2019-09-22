from pygame.locals import *
import pygame
import math
from time import sleep

class Mouse(pygame.sprite.Sprite):
    x = 150
    y = 240
    speed = 10

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([150, 240])

        self.image = pygame.image.load("images\mouse.png").convert_alpha()


        self.rect = self.image.get_rect(center = (150, 240))

        self.rect.x = 150

        self.rect.y = 240