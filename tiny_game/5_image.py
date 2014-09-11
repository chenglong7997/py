import pygame
import sys
from pygame.locals import *

pygame.init()

yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)

setDisplay = pygame.display.set_mode((400, 600))
pygame.display.set_caption('epic game')
setDisplay.fill(cyan)

img = pygame.image.load('code.jpg')

FPS = 30
imgx = 10
imgy = 10
pixMove = 5
movement = 'down'

fpsTime = pygame.time.Clock()

while True:
    #hide the moving lines
    setDisplay.fill(cyan)

    if movement == 'down':
        imgy += pixMove
        if imgy > 300:
            img = pygame.transform.rotate(img, 90)
            movement = 'right'
    elif movement == 'right':
        imgx += pixMove
        if imgx > 150:
            img = pygame.transform.rotate(img, 90)
            movement = 'up'
    elif movement == 'up':
        imgy -= pixMove
        if imgy < 30:
            img = pygame.transform.rotate(img, 90)
            movement = 'left'
    elif movement == 'left':
        imgx -= pixMove
        if imgx < 30:
            img = pygame.transform.rotate(img, 90)
            movement = 'down'
        
    setDisplay.blit(img, (imgx, imgy))
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(FPS)
