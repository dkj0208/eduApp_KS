import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # Frames per second setting
fpsClock = pygame.time.Clock()

# Set up the window
DISPLAYSUR = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
BLACK = (0,0,0)

catImg = pygame.image.load('cat.png')
# catImg = pygame.draw.rect(DISPLAYSUR, BLACK, (0,0,0,0),20)
catX = 10
catY = 10

direction = 'right'

while True: # The main game loop
    DISPLAYSUR.fill(WHITE)

    if direction == 'right':
        catX += 5
        if catX == 280:
            direction = 'down'
    elif direction == 'down':
        catY += 5
        if catY == 220:
            direction = 'left'
    elif direction == 'left':
        catX -= 5
        if catX == 10:
            direction = 'up'
    elif direction == 'up':
        catY -= 5
        if catY == 10:
            direction = 'right'
    DISPLAYSUR.blit(catImg, (catX,catY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    fpsClock.tick(FPS)
