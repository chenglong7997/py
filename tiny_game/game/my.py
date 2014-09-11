import pygame
import sys
import random
import math
from pygame.locals import *
import time

pygame.init()

yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)
red = (175,0,0)
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)

FPS = 30
dispWidth = 1500
dispHeight = 580
cellSize = 40

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'
bgImg = pygame.image.load('bk.jpg')
myImg = pygame.image.load('my.png')
rockImg = pygame.image.load('rock.png')
winImg = pygame.image.load('win.png')

deadZones = []
win = 0
lose = 0

def runGame():
    global deadZones
    global bgImg
    global win
    global lose
    win = 0
    
    isAlive = 'yes'
    startx = 3
    starty = 3
    coords = [{'x':startx, 'y':starty}]
    evilCoords = [{'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}]
    evilCoords1 = [{'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}]
    evilCoords2 = [{'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}]
    evilCoords3 = [{'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}]
    evilCoords4 = [{'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}]
    evilCoords5 = [{'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}]
    evilCoords6 = [{'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}]
    evilCoords7 = [{'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}]
    evilCoords8 = [{'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}]
    evilCoords9 = [{'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}]
    
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
                else:
                    isAlive = 'no'
                    win = 1
                    
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y']}
            elif direction == LEFT:
                if coords[0]['x'] - 1 > 0:
                    coords[0]['x'] -= 1
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y']}

            #delete the old cell
            del coords[-1]
            
            coords.insert(0, newCell)
            setDisplay.fill(cyan)
            
            setDisplay.blit(bgImg,(0,0))

            evilMove(evilCoords)
            evilMove(evilCoords1)
            evilMove(evilCoords2)
            evilMove(evilCoords3)
            evilMove(evilCoords4)
            evilMove(evilCoords5)
            evilMove(evilCoords6)
            evilMove(evilCoords7)
            evilMove(evilCoords8)
            evilMove(evilCoords9)
            
 
            drawCell(evilCoords, red)
            drawCell(evilCoords1, red)
            drawCell(evilCoords2, red)
            drawCell(evilCoords3, red)
            drawCell(evilCoords4, red)
            drawCell(evilCoords5, red)
            drawCell(evilCoords6, red)
            drawCell(evilCoords7, red)
            drawCell(evilCoords8, red)
            drawCell(evilCoords9, red)
            
            drawMy(coords)

            #check collision
            currentPos = [newCell['x'], newCell['y']]
            for eachDeath in deadZones:
                if eachDeath[0] <= newCell['x'] and eachDeath[0] + 1 >= newCell['x'] and eachDeath[1] <= newCell['y'] and eachDeath[1] + 1 >= newCell['y']:
                    isAlive = 'no'
                    lose += 1

            pygame.display.update()
            fpsTime.tick(FPS)

        if lose == 3:
            lose = 0
            msgSurface('Lose 3 times!', cyan, True)
            
        if win == 0:
            msgSurface('You Died!', red, False)
        elif win == 1:
            setDisplay.fill(black)
            setDisplay.blit(winImg,(470,60))
            msgSurface('You win!', red, False)

def evilMove(evilGuy):
    evilCoords = []
    
    #return -1,0,1
    randx = random.randrange(-1,2)
    randy = random.randrange(-1,2)
    
    newCell = {'x':evilGuy[0]['x'] + randx, 'y':evilGuy[0]['y'] + randy}

    if (newCell['x']<0 or newCell['y']<0 or newCell['x']>dispWidth/cellSize or newCell['y']>dispHeight/cellSize):
        newCell = {'x':dispWidth/(2*cellSize) - 2, 'y':dispHeight/(2*cellSize) - 1}

    del evilGuy[-1]
    evilCoords.append(newCell['x'])
    evilCoords.append(newCell['y'])
    deadZones.append(evilCoords)
    
    evilGuy.insert(0,newCell)

def drawMy(coords):
    setDisplay.blit(myImg, (coords[0]['x']*cellSize, coords[0]['y']*cellSize))

def drawCell(coords, ccolor):
    setDisplay.blit(rockImg, (coords[0]['x']*cellSize, coords[0]['y']*cellSize))

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
def msgSurface(text, textColor, s):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    if text != 'You win!':
        titleTextSurf, titleTextRect = makeTextObjs(text, largeText, textColor)
        titleTextRect.center = (int(dispWidth/2), int(dispHeight/2))
        setDisplay.blit(titleTextSurf, titleTextRect)

    typeTextSurf, typeTextRect = makeTextObjs('Press key to continue', smallText, purple)
    typeTextRect.center = (int(dispWidth/2 + 25), int(dispHeight/2) + 135)
    setDisplay.blit(typeTextSurf, typeTextRect)

    pygame.display.update()
    fpsTime.tick()

    #if s:
     #   time.sleep(5)
    #finish? check event types
    while whatNext() == None:
        for event in pygame.event.get([QUIT]):
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        fpsTime.tick()

    runGame()

#main loop
while True:
    global fpsTime
    global setDisplay

    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((dispWidth, dispHeight))
    pygame.display.set_caption('controlling')
    runGame()






    
