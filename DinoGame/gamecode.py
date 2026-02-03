import pygame
pygame.init()
from variables import *
from obstacles import *
import random

def drawgame(animationsList):
    global pointer
    global animationStage
    global whichRect
    global gameOver
    global hovered
    global SKYBLUE

    SCREEN.fill(SKYBLUE)
    pygame.draw.rect(SCREEN, BROWN, groundRect)
    #SCREEN.blit(deadlyLazer, (0, 100))
    for cloud in onscreenClouds:
        SCREEN.blit(cloud.image, (cloud.Rect.x, cloud.Rect.y))

    #pygame.draw.rect(SCREEN, WHITE, Rects[0])
    SCREEN.blit(animationsList[animationStage][pointer], (playerRect.x - 10, playerRect.y))
    SCREEN.blit(scoreText, (100, 500))

    SCREEN.blit(SCORE_FONT.render("( " + str(playerScore) + " )", 1, GREEN), (220, 480))
    SCREEN.blit(SCORE_FONT.render("Previous Score ( " + str(prevScore) + " )", 1, GREEN), (850, 430))
    SCREEN.blit(SCORE_FONT.render("High Score ( " + str(highScore) + " )", 1, GREEN), (890, 490))

    for obstacle in onscreenObstacles:
        pygame.draw.rect(SCREEN, GREEN, obstacle.Rect)

    if gameOver == True:
        SCREEN.blit(gameOvertext, (170, 70))
        if retryRect.collidepoint(pygame.mouse.get_pos()):
            SCREEN.blit(retryHover, (500, 500))
            hovered = True
        else:
            SCREEN.blit(retryText, (500, 500))
            hovered = False

    pygame.display.update()

def pausescreen(animationsList):
    global animationStage
    global pointer
    global SKYBLUE
    animationStage = 0
    pointer = 0

    paused = True

    while paused == True:
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #allows for quitting to occur
                exit() 
        playeridle()
        SCREEN.fill(SKYBLUE)
        pygame.draw.rect(SCREEN, BROWN, groundRect)

        for cloud in onscreenClouds:
            SCREEN.blit(cloud.image, (cloud.Rect.x, cloud.Rect.y))
        for obstacle in onscreenObstacles:
            pygame.draw.rect(SCREEN, GREEN, obstacle.Rect)

        SCREEN.blit(pausedText, (450, 200))
        SCREEN.blit(SCORE_FONT.render("Press U to unpause", 1, GREEN), (420, 480))

        SCREEN.blit(animationsList[animationStage][pointer], (playerRect.x - 10, playerRect.y))
        pygame.display.update()

        if keys_pressed[pygame.K_u]:
            paused = False

def sortoutscores():
    global highScore
    global playerScore
    global prevScore

    prevScore = playerScore
    if playerScore > highScore:
        highScore = playerScore

def makeobstacles():
    global obstacleCountdown
    global playerScore
    randomHeight = random.randint(30,60)
    randomDuckheight = random.randint(280, 320)

    if len(onscreenObstacles) - 1 < maxObstacles and obstacleCountdown == 0:
        random.shuffle(obstacleType)
        if obstacleType[2] == "jump":
            newObstacle = Obstacles(40, 20, 0, pygame.Rect(1200, 400 - randomHeight, 20, randomHeight))
            onscreenObstacles.append(newObstacle)
            obstacleCountdown = random.randint(60,90)
        elif obstacleType[2] == "duck": #and playerScore >= 50:
            newObstacle = Obstacles(20, 40, 0, pygame.Rect(1200, randomDuckheight, 40, 20))
            onscreenObstacles.append(newObstacle)
            obstacleCountdown = random.randint(60,90)
    else:
        obstacleCountdown -= 1

    
def makeclouds():
    global cloudCountdown

    if cloudCountdown == 0:
        random.shuffle(cloudList)
        newCloud = Clouds(100, 100, cloudList[3], pygame.Rect(1200, random.randint(50,320), 10, 10))
        onscreenClouds.append(newCloud)
        cloudCountdown = random.randint(90,140)
    else:
        cloudCountdown -= 1

def moveobstacles():
    global obstacleSpeed
    global cloudSpeed
    for obstacle in onscreenObstacles:
        obstacle.Rect.x -= obstacleSpeed
        if obstacle.Rect.x < 0:
            onscreenObstacles.remove(obstacle)
    
    for cloud in onscreenClouds:
        cloud.Rect.x -= cloudSpeed
        if cloud.Rect.x < -60:
            onscreenClouds.remove(cloud)

def jumpies():
    global jumping

    if playerRect.y < 210:
        jumping = True
    elif playerRect.y > 210:
        playerRect.y -= 6

def down():
    global jumping
    global goingUp
    global animationStage

    if playerRect.y < 320:
        playerRect.y += 6
        animationStage = 4
    elif playerRect.y >= 320:
        jumping = False
        goingUp = False

def boingcountdown():
    global boingCountdown
    if boingCountdown == 0:
        boingNoise.play()
        boingCountdown = 20
    else:
        boingCountdown -= 1

def gottagofast():
    global obstacleSpeed
    global scorecooldown
    global cloudSpeed

    if scorecooldown == 0:
        if obstacleSpeed < 20:
            obstacleSpeed += 1
            cloudSpeed += 0.5
            print(obstacleSpeed)

def gottagodark():
    global scorecooldown
    global red, green, blue
    global SKYBLUE
    global dayTime

    if scorecooldown == 0:
        if red != 0:
            red -= 1
        if green != 0:
            green -= 1
        if blue != 0:
            blue -= 1
        SKYBLUE = (red, green, blue)

        if red == 0 and blue == 0 and green == 0:
            print("daytime mode lads")
            dayTime = False

def gottagetlight():
    global scorecooldown
    global red, green, blue
    global SKYBLUE
    global dayTime

    if scorecooldown == 0:
        if red != 179:
            red += 0.5
        if green != 217:
            green += 0.5
        if blue != 255:
            blue += 0.5
        SKYBLUE = (red, green, blue)

        if red == 179 and blue == 255 and green == 217:
            dayTime == True

def playermovement(animationsList):
    global jumping
    global maxPointer
    global animationStage
    global gameOver
    global goingUp
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_p]:
        pausescreen(animationsList)

    if keys_pressed[pygame.K_DOWN] and keys_pressed[pygame.K_UP] != True and goingUp == False:
        animationStage = 2
        Rects.clear()
        Rects.append(duckRect)
    elif keys_pressed[pygame.K_UP] and jumping == False:
        animationStage = 3
        goingUp = True
        jumpies()
        boingcountdown()
        Rects.clear()
        Rects.append(playerRect)
    else:
        if jumping == True:
            animationStage = 4
        else:
            animationStage = 1
        down()
        Rects.clear()
        Rects.append(playerRect)

    for obstacle in onscreenObstacles:
        if Rects[0].colliderect(obstacle.Rect):
            hitNoise.play()
            gameOver = True

def playeranimation():
    global animationCooldown
    global pointer
    global maxPointer

    if animationCooldown == 0:
        if pointer == maxPointer:
            pointer = 0
        else:
            pointer += 1
        animationCooldown = 4
    else:
        animationCooldown -= 1

def playeridle():
    global animationCooldown
    global pointer

    if animationCooldown == 0:
        if pointer == 3:
            pointer = 0
        else:
            pointer += 1
        animationCooldown = 25
    else:
        animationCooldown -= 1

def scoring():
    global playerScore
    global scorecooldown

    if scorecooldown == 0:
        playerScore += 1
        scorecooldown = 15
    else:
        scorecooldown -= 1

def timetoplay(animationsList):
    global animationStage
    global maxPointer
    global gameOver
    global playerScore
    global hovered
    global obstacleSpeed
    global cloudSpeed
    global red, green, blue
    global dayTime

    playerScore = 0
    onscreenObstacles.clear()
    gameOver = False 
    obstacleSpeed = 6
    cloudSpeed = 3
    red, green, blue = 179, 217, 255

    while True:
        keys_pressed = pygame.key.get_pressed()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #allows for quitting to occur
                exit() 

            if event.type == pygame.MOUSEBUTTONDOWN and hovered == True:
                timetoplay(animationsList)

        playeranimation()
        if keys_pressed[pygame.K_p]:
            pausescreen(animationsList)
        if gameOver == False:
            makeobstacles()
            makeclouds()
            playermovement(animationsList)
            moveobstacles()
            scoring()

            if dayTime == True:
                gottagodark()
            if dayTime == False:
                gottagetlight()
            if playerScore % 50 == 0 and playerScore > 0:
                gottagofast()

        if gameOver == True:
            animationStage = 5
            sortoutscores()
        drawgame(animationsList)