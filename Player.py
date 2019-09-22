from pygame.locals import *
import pygame
import math
from time import sleep

class Player(pygame.sprite.Sprite):
    #starting position and speed
    x = 10
    y = 10
    speed = 10

    def __init__(self):
        super().__init__()

        #create the surface
        self.image = pygame.Surface([250, 250])

        #load the image
        self.image = pygame.image.load("images/paddle.png").convert_alpha()

        #create a rectangle to handle location, collision
        self.rect = self.image.get_rect(center = (10, 350))

        #set the horizontal starting position. this never needs to chanfe
        self.rect.y= 380

