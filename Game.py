import pygame
import sys
import random
from Mouse import Mouse
from Cat import Cat
from pygame.locals import *



pygame.init()

screen = pygame.display.set_mode((960, 690))
screen.fill((255, 255, 255))
pygame.display.set_caption('Mouse')
background = pygame.image.load("images\_floorboards.jpg").convert_alpha()
font = pygame.font.SysFont(None, 36)

main_clock = pygame.time.Clock()
score = 0
health = 3
alive = True

mouse = Mouse()
mouse.rect.x = 150
mouse.rect.y = 240
mouse_speed = mouse.speed

draw_mouse = pygame.sprite.Group()
draw_mouse.add(mouse)


move_left = False
move_right = False
move_up = False
move_down = False

def draw_screen():
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (255, 255, 255))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)

cat = Cat()
cat.rect.x = -300
cat.rect.y = 240
cat_speed = cat.speed
draw_cat = pygame.sprite.Group()
draw_cat.add(cat)

cat_can_move = False

all_traps = []
trap_width = 50
trap_height = 30
rand_x = []
rand_y = []

all_cheese = []

def create_rand():
    for ten in range(0, 10):
        rand_x.append(random.randrange(200, 810))
        rand_y.append(random.randrange(0, 600))

create_rand()

def create_traps():
    for amount in range(0, 5):
        trap = pygame.Rect(rand_x[amount], rand_y[amount], trap_width, trap_height)
        pygame.draw.rect(screen, (216, 186, 142), trap)
        all_traps.append(trap)

create_traps()


cheese_group = pygame.sprite.Group()
def create_cheese():
    for amount in range(0, len(rand_x)):
        cheese = pygame.draw.circle(screen, (242, 221, 120), (rand_x[amount] + 85, rand_y[amount] + 28), 25, 0)
        all_cheese.append(cheese)

create_cheese()


def draw_traps():
    for trap in all_traps:
        trap = pygame.Rect(trap.x, trap.y, trap_width, trap_height)
        trap = pygame.draw.rect(screen, (216, 186, 142), trap)

def draw_cheese():
    for cheese in all_cheese:
        cheese = pygame.draw.circle(screen, (242, 221, 120), (cheese.x, cheese.y), 25, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                move_left = True
            if event.key == K_d:
                move_right = True
            if event.key == K_w:
                move_up = True
            if event.key == K_s:
                move_down = True
        if event.type == KEYUP:
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False
            if event.key == K_w:
                move_up = False
            if event.key == K_s:
                move_down = False
            if alive:
                if event.key == K_SPACE:
                    cat_can_move = True
            if (cat_can_move == False):
                if event.key == K_RETURN:
                    alive = True
                    health = 3
                    score = 0
                    cat_can_move = False
                    mouse.rect.x = 150
                    mouse.rect.y = 240
                    cat.rect.x = -300
                    cat.rect.y = 240
                    for x in range(0, len(rand_x)):
                        rand_x.pop()
                        rand_y.pop()
                    for x in range (0, len(all_cheese)):
                        all_cheese.pop()
                    for x in range(0, len(all_traps)):
                        all_traps.pop()
                    create_rand()
                    create_cheese()
                    create_traps()

    main_clock.tick(50)

    if cat_can_move:

        if move_left and mouse.rect.left > 0:
            mouse.rect.x -= mouse_speed
        if move_right and mouse.rect.right < 960:
            mouse.rect.x += mouse_speed
        if move_up and mouse.rect.top > 0:
            mouse.rect.y -= mouse_speed
        if move_down and mouse.rect.bottom < 690:
            mouse.rect.y += mouse_speed

        for trap in all_traps:
            if (mouse.rect).colliderect(trap):
                all_traps.remove(trap)
                health -= 1
                break

        for cheese in all_cheese:
            if (mouse.rect).colliderect(cheese):
                all_cheese.remove(cheese)
                score += 10
                break

        if (cat.rect.right >= mouse.rect.left) and ((cat.rect.right - mouse.rect.left) <= 10) :
            if ((cat.rect.top - mouse.rect.bottom) <= 0) and ((cat.rect.bottom - mouse.rect.top) >= 0):
                cat_can_move = False
                alive = False

        else:
            if(mouse.rect.right <= cat.rect.right) or (mouse.rect.left < cat.rect.right):
                cat.rect.x -= cat_speed
            else:
                cat.rect.x += cat_speed
            if(mouse.rect.y > cat.rect.y):
                cat.rect.y += cat_speed
            else:
                cat.rect.y -= cat_speed


    if health < 0:
        alive = False

    draw_screen()
    destination = pygame.draw.circle(screen, (0, 0, 0), (960, 345), 35, 0)
    draw_traps()
    draw_cheese()
    draw_mouse.draw(screen)
    draw_cat.draw(screen)
    draw_text('Score: %s' % (score), font, screen, 5, 5)
    draw_text('Health: %s' % (health), font, screen, 800, 5)
    if alive:
        if all_cheese == []:
            if mouse.rect.right >= 960 and (mouse.rect.y <= 330 and mouse.rect.y >= 320):
                cat_can_move = False
                draw_text('You Won!', font, screen, 440, 345)
                draw_text('Press Enter to Play Again', font, screen, 350, 390)

    else:
        cat_can_move = False
        if health < 0:
            draw_text('You ran into too many traps', font, screen, 350, 300)
        else:
            draw_text('The cat caught you', font, screen, 400, 300)
        draw_text('Game Over', font, screen, 440, 345)
        draw_text('Press Enter to Play Again', font, screen, 350, 390)

    pygame.display.update()