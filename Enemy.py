import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/asteroid.png").convert_alpha()
        self.rect = self.image.get_rect(center = (10, 350))

    def update(self):
        self.rect.x += 5

pygame.image.load("image_file_path.filetype").comvert_alpha()
asteroid = pygame.image.load("images/asteroid.png")

surface_name.blit(image, (x, y))
screen.blit(asteroid, (50, 50))