import pygame
pygame.init()

WHITE = (255, 255, 255)

def get_image(sheet, along, down, width, height, scale, colour):
    #okay so this function takes some parameters
    #and uses them to cut down a sprite sheet into little chunks
    #which can then be used as individual frames
    image = pygame.Surface((width, height))
    image.blit(sheet, (0,0), (along*width, down*height, width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey(colour)
    return image

def getcolour(idlesheet, runsheet, ducksheet, jumpsheet, hitsheet):
    #dino animation time!
    idleOne = get_image(idlesheet, 0, 0, 24, 21, 4, WHITE)
    idleTwo = get_image(idlesheet, 1, 0, 24, 21, 4, WHITE)
    idleThree = get_image(idlesheet, 2, 0, 24, 21, 4, WHITE)
    idleFour = get_image(idlesheet, 3, 0, 24, 21, 4, WHITE)
    idleList = [idleOne, idleTwo, idleThree, idleFour]

    runOne = get_image(runsheet, 0, 0, 24, 21, 4, WHITE)
    runTwo = get_image(runsheet, 1, 0, 24, 21, 4, WHITE)
    runThree = get_image(runsheet, 2, 0, 24, 21, 4, WHITE)
    runFour = get_image(runsheet, 3, 0, 24, 21, 4, WHITE)
    runFive = get_image(runsheet, 4, 0, 24, 21, 4, WHITE)
    runSix = get_image(runsheet, 5, 0, 24, 21, 4, WHITE)
    runList = [runOne, runTwo, runThree, runFour, runFive, runSix]

    duckOne = get_image(ducksheet, 0, 0, 24, 21, 4, WHITE)
    duckTwo = get_image(ducksheet, 1, 0, 24, 21, 4, WHITE)
    duckThree = get_image(ducksheet, 2, 0, 24, 21, 4, WHITE)
    duckFour = get_image(ducksheet, 3, 0, 24, 21, 4, WHITE)
    duckFive = get_image(ducksheet, 4, 0, 24, 21, 4, WHITE)
    duckList = [duckOne, duckTwo, duckThree, duckFour, duckFive, duckOne]

    jumpOne = get_image(jumpsheet, 0, 0, 24, 21, 4, WHITE)
    jumpTwo = get_image(jumpsheet, 1, 0, 24, 21, 4, WHITE)
    jumpList = [jumpTwo, jumpTwo, jumpTwo, jumpTwo, jumpTwo, jumpTwo]
    standList = [jumpOne, jumpOne, jumpOne, jumpOne, jumpOne, jumpOne]

    hitOne = get_image(hitsheet, 0, 0, 24, 21, 4, WHITE)
    hitTwo = get_image(hitsheet, 1, 0, 24, 21, 4, WHITE)
    hitThree = get_image(hitsheet, 2, 0, 24, 21, 4, WHITE)
    hitList = [hitOne, hitThree, hitOne, hitThree, hitOne, hitThree]

    aniList = [idleList, runList, duckList, jumpList, standList, hitList]  
    return aniList

