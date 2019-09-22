from pygame.locals import *
import pygame

class Cheese(pygame.sprite.Sprite):


    def __init__(self, a, b):

        self.image = pygame.Surface([100, 99])

        self.image = pygame.image.load("images\cheese.jpg").convert_alpha()

        self.rect = self.image.get_rect(center = (100, 99))

        self.rect.x = a

        self.rect.y = b