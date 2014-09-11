import pygame
import sys
import random
import math
from pygame.locals import *

pygame.init()

yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)
red = (175,0,0)
white = (255,255,255)

FPS = 30
dispWidth = 800
dispHeight = 600
cellSize = 40

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

deadZones = []

def runGame():
    global fpsTime
    global setDisplay
    global deadZones

    isAlive = 'yes'
    startx = 3
    starty = 3
    coords = [{'x':startx, 'y':starty}]
    evilCoords = [{'x':dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    evilCoords1 = [{'x':dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    evilCoords2 = [{'x':dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    
    direction = RIGHT

    while True:
        while isAlive == 'yes':
            deadZones = []
            for event in pygame.event.get():
                #print event
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        direction = LEFT
                    elif event.key == K_RIGHT:
                        direction = RIGHT
                    elif event.key == K_DOWN:
                        direction = DOWN
                    elif event.key == K_UP:
                        direction = UP

            if direction == UP:
                if coords[0]['y'] - 1 > 0:
                    coords[0]['y'] -= 1
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y']}
            elif direction == DOWN:
                if coords[0]['y'] + 1 < dispHeight / cellSize -1:
                    coords[0]['y'] += 1
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y']}
            elif direction == RIGHT:
                if coords[0]['x'] + 1 < (dispWidth / cellSize - 1):
                    coords[0]['x'] += 1
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y']}
            elif direction == LEFT:
                if coords[0]['x'] - 1 > 0:
                    coords[0]['x'] -= 1
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y']}

            #delete the old cell
            del coords[-1]
            
            coords.insert(0, newCell)
            setDisplay.fill(cyan)

            evilMove(evilCoords)
            evilMove(evilCoords1)
            evilMove(evilCoords2)
            drawCell(evilCoords, red)
            drawCell(evilCoords1, red)
            drawCell(evilCoords2, red)
            
            drawCell(coords, white)

            #check collision
            currentPos = [newCell['x'], newCell['y']]
            for eachDeath in deadZones:
                if eachDeath == currentPos:
                    isAlive = 'no'
            
            pygame.display.update()
            fpsTime.tick(FPS)
                
        msgSurface('You Died!', red)

def evilMove(evilGuy):
    evilCoords = []
    
    #return -1,0,1
    randx = random.randrange(-1,2)
    randy = random.randrange(-1,2)
    
    newCell = {'x':evilGuy[0]['x'] + randx, 'y':evilGuy[0]['y'] + randy}

    if (newCell['x']<0 or newCell['y']<0 or newCell['x']>dispWidth/cellSize or newCell['y']>dispHeight/cellSize):
        newCell = {'x':dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}

    del evilGuy[-1]
    evilCoords.append(newCell['x'])
    evilCoords.append(newCell['y'])
    deadZones.append(evilCoords)
    
    evilGuy.insert(0,newCell)

def drawCell(coords, ccolor):
    for coord in coords:
        x = coord['x']*cellSize
        y = coord['y']*cellSize
        makeCell = pygame.Rect(x,y,cellSize,cellSize)
        pygame.draw.rect(setDisplay, ccolor, makeCell)


#whatNext and makeTextObjs ared used by msgSurface
def whatNext():
    for event in pygame.event.get([KEYDOWN, KEYUP, QUIT]):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            continue
        #return when got keyup event
        return event.key
    return None

def makeTextObjs(text, font, tcolor):
    textSurface = font.render(text, True, tcolor)
    return textSurface, textSurface.get_rect()

#show the messages when died
def msgSurface(text, textColor):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText, textColor)
    titleTextRect.center = (int(dispWidth/2), int(dispHeight/2))
    setDisplay.blit(titleTextSurf, titleTextRect)

    typeTextSurf, typeTextRect = makeTextObjs('Press key to continue', smallText, purple)
    typeTextRect.center = (int(dispWidth/2), int(dispHeight/2) + 75)
    setDisplay.blit(typeTextSurf, typeTextRect)

    pygame.display.update()
    fpsTime.tick()

    #finish? check event types
    while whatNext() == None:
        for event in pygame.event.get([QUIT]):
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        fpsTime.tick()

    runGame()
    
while True:
    global fpsTime
    global setDisplay

    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((dispWidth, dispHeight))
    pygame.display.set_caption('controlling')
    runGame()






    
