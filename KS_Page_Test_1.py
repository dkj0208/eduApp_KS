#-*- coding: euc-kr -*-
import pygame, time
from pygame.locals import *

pygame.init()
displayWidth = 1024
displayHeight = 768

white = (255,255,255)
black = (0,0,0)
red = (175,0,0)
green = (34,177,76)
yellow = (175,175,0)
blue = (30,144,255)
lightGreen = (0,255,0)
lightRed = (255,0,0)
lightYellow = (255,255,0)
lightBlue = (0,191,255)

smallFont = pygame.font.SysFont("NanumGothic", 20)
medFont = pygame.font.SysFont("NanumGothic", 45)
largeFont = pygame.font.SysFont("NanumGothic", 55)
# sound1 = pygame.mixer.Sound("beep1.ogg")
# sound2 = pygame.mixer.Sound("beep2.ogg")
# sound3 = pygame.mixer.music.load("beep3.ogg")

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("KS Test")

def textObjects(text, color, size):
    if size == "small":
        textSurf = smallFont.render(text, True, color)
    elif size == "medium":
        textSurf = medFont.render(text, True, color)
    elif size == "large":
        textSurf = largeFont.render(text, True, color)

    return textSurf, textSurf.get_rect()

def messageToScreen(msg, color, yDistance=0, size="small"):
    textSurface, textRect = textObjects(msg, color, size)
    textRect.center = (displayWidth/2), (displayHeight/2) + yDistance # 높이 위치 조절
    gameDisplay.blit(textSurface, textRect)

def textToButton(msg, color, buttonX, buttonY, buttonWidth, buttonHeight, size = "small"):
    textSurfce, textRect = textObjects(msg, color, size)
    textRect.center = ((buttonX + (buttonWidth/2), buttonY + (buttonHeight/2)))
    gameDisplay.blit(textSurfce, textRect)

def button(text, x, y, width, height, inactiveColor, activeColor, textColor = black, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, activeColor, (x+2,y+2,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "sound1":
                # sound1.play()
                print("test1")
            if action == "sound2":
                # sound2.play()
                print("test2")
            if action == "sound3":
                # sound2.play()
                print("test3")

            if action == "page_1":
                gameDisplay.fill(white)
                pygame.display.update()
                page_1()
            if action == "page_2":

    else:
        pygame.draw.rect(gameDisplay, inactiveColor, (x,y,width,height))

    textToButton(text, textColor, x, y, width, height)

def page_1():
    level = 1
    while level:
        gameDisplay.fill(white)
        messageToScreen(u"소리를 듣고 무엇인지 맞춰주세요.", green, -200, size="large")
        button(u"1번 소리", 150, 500, 150, 50, lightYellow, yellow, action="sound_1")
        button(u"2번 소리", 350, 500, 150, 50, lightRed, red, action="sound_2")
        button(u"나가기", 550, 500, 150, 50, lightGreen, green, action="quit")
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                level = 0
                pygame.quit()
                quit()

def startScreen():
    game = True
    while game:
        gameDisplay.fill(white)
        messageToScreen(u"경신 프로그램 테스트", green, -100, size="large")
        button(u"A 그룹",150,400,150,50,lightGreen, green, action="page_1")
        button(u"2번 사운드",350,400,150,50,lightYellow, yellow, action="sound2")
        button(u"3번 사운드",550,400,150,50,lightRed, red, action="sound3")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
                pygame.quit()
                quit()

startScreen()