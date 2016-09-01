import pygame, sys
from pygame.locals import *

FPS = 30 # Frame per second, The general speed of the program
WINDOWWIDTH = 640 # Size of window's width in pixels
WINDOWHEIGHT = 480 # Size of window's height in pixels
REVEALSPEED = 8 # Speed boxes sliding reveals and covers
BOXSIZE = 40 # Size of box width and height in pixels
GAPSIZE = 10 # Size of gap between boxes in pixels
BOARDWIDTH = 10 # Number of columns of icons
BOARDHEIGHT = 7 # Number of rows of icons

assert (BOARDWIDTH*BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE)))/2) # 70
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE)))/2) # 65

# RGB

GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BGCOLOE = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUAER = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUAER, DIAMOND, LINES, OVAL)

assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, 'Board is too big for the number of shapes/colors defind.'

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event

    pygame.display.set_caption('Memory Puzzle')

    # mainBoard = getRandomizedBoard()

    DISPLAYSURF.fill((255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()