import pygame
import sys
from pygame.locals import *

pygame.init()

yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)

setDisplay = pygame.display.set_mode((400, 300))
pygame.display.set_caption('epic game')

singlePix = pygame.PixelArray(setDisplay)
setDisplay.fill(cyan)

#set color to one pix
singlePix[4][4] = yellow

#draw line
pygame.draw.line(setDisplay, yellow, (300, 200), (200,300), 4)

#draw circle
pygame.draw.circle(setDisplay, purple, (50,50), 20)
pygame.draw.circle(setDisplay, purple, (50,50), 20, 5)

#draw rect
pygame.draw.rect(setDisplay, purple, (100,100,200,100))

#polygon
pygame.draw.polygon(setDisplay, purple, ((50,20),(30,40),(60,100),(200,100),(400,99)))

while True:
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
