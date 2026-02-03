print("Hello world!")

#I am about to make the best chrome dinosaur game
#you have ever seen

import pygame
from variables import *
from gamecode import timetoplay
import random
#importing modules we need

pygame.init() #initialising pygame is always good

def drawthatshit(animationsList):
    global idlePointer
    global hovered
    global colourChosen 

    SCREEN.fill(SKYBLUE)
    pygame.draw.rect(SCREEN, BROWN, groundRect)
    SCREEN.blit(animationsList[0][idlePointer], (500, 320))

    SCREEN.blit(SCORE_FONT.render("UP to jump", 1, GREEN), (70, 440))
    SCREEN.blit(SCORE_FONT.render("DOWN to duck", 1, GREEN), (70, 480))
    SCREEN.blit(SCORE_FONT.render("P to pause", 1, GREEN), (70, 520))
    SCREEN.blit(SCORE_FONT.render("Use the right arrow", 1, GREEN), (850, 460))
    SCREEN.blit(SCORE_FONT.render("to choose another dino", 1, GREEN), (800, 500))

    if hovered == True:
        SCREEN.blit(beginHover, (500, 470))
    if hovered == False:
        SCREEN.blit(beginText, (500, 470))
    
    pygame.display.update()

def playerrun():
    global animationCooldown
    global pointer
    global maxPointer

    if animationCooldown == 0:
        if pointer == maxPointer:
            pointer = 0
        else:
            pointer += 1
        animationCooldown = 15
    else:
        animationCooldown -= 1

def switchcolours():
    global colourChosen
    global animationsList
    from changecolour import getcolour

    colourChosen += 1

    if colourChosen > 3:
        colourChosen = 0

    animationsList = getcolour(colourList[colourChosen][0], colourList[colourChosen][1], colourList[colourChosen][2], colourList[colourChosen][3], colourList[colourChosen][4])
    return animationsList

def runoff(animationsList):
    global pointer
    global colourChosen
    pointer = 0

    while playerRect.x < 1200:
        SCREEN.fill(SKYBLUE)
        pygame.draw.rect(SCREEN, BROWN, groundRect)
        SCREEN.blit(animationsList[1][pointer], (playerRect.x, playerRect.y))

        SCREEN.blit(SCORE_FONT.render("UP to jump", 1, GREEN), (70, 440))
        SCREEN.blit(SCORE_FONT.render("DOWN to duck", 1, GREEN), (70, 480))
        SCREEN.blit(SCORE_FONT.render("P to pause", 1, GREEN), (70, 520))
        SCREEN.blit(SCORE_FONT.render("Use the right arrow", 1, GREEN), (850, 460))
        SCREEN.blit(SCORE_FONT.render("to choose another dino", 1, GREEN), (800, 500))

        
        playerrun()
        playerRect.x += 1
        pygame.display.update()
    
    runon(switchcolours())

def runon(animationsList):
    global pointer
    global colourChosen
    pointer = 0
    playerRect.x = -50

    while playerRect.x != 500:
        SCREEN.fill(SKYBLUE)
        pygame.draw.rect(SCREEN, BROWN, groundRect)
        SCREEN.blit(animationsList[1][pointer], (playerRect.x, playerRect.y))

        SCREEN.blit(SCORE_FONT.render("UP to jump", 1, GREEN), (70, 440))
        SCREEN.blit(SCORE_FONT.render("DOWN to duck", 1, GREEN), (70, 480))
        SCREEN.blit(SCORE_FONT.render("P to pause", 1, GREEN), (70, 520))
        SCREEN.blit(SCORE_FONT.render("Use the right arrow", 1, GREEN), (850, 460))
        SCREEN.blit(SCORE_FONT.render("to choose another dino", 1, GREEN), (800, 500))

        playerrun()
        playerRect.x += 1
        pygame.display.update()
        
def playeranimation():
    global animationCooldown
    global idlePointer

    if animationCooldown == 0:
        if idlePointer == 3:
            idlePointer = 0
        else:
            idlePointer += 1
        animationCooldown = 6
    else:
        animationCooldown -= 1

def runthisshit(): #main function to run le game
    global hovered
    global animationsList
    from changecolour import getcolour

    animationsList = getcolour(colourList[colourChosen][0], colourList[colourChosen][1], colourList[colourChosen][2], colourList[colourChosen][3], colourList[colourChosen][4])

    pygame.display.set_caption("Boing Boing")
    print(3 % 2)
    print(3/2)

    while True:   
        keys_pressed = pygame.key.get_pressed()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #allows for quitting to occur
                exit() 
            if keys_pressed[pygame.K_RIGHT]:
                print("hi")
                runoff(animationsList)
            
            if beginRect.collidepoint(pygame.mouse.get_pos()):
                hovered = True
            else:
                hovered = False

            if hovered == True and event.type == pygame.MOUSEBUTTONDOWN:
                timetoplay(animationsList)
                
        drawthatshit(animationsList)
        playeranimation()

runthisshit()


