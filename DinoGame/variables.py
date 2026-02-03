#lets define some fuckin' variables yo
import pygame
pygame.init()
import os

from obstacles import Sky

def get_image(sheet, along, down, width, height, scale, colour):
    #okay so this function takes some parameters
    #and uses them to cut down a sprite sheet into little chunks
    #which can then be used as individual frames
    image = pygame.Surface((width, height))
    image.blit(sheet, (0,0), (along*width, down*height, width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey(colour)
    return image

HEIGHT = 600
WIDTH = 1200
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) 
FPS = 60 #frames per second for the game
clock = pygame.time.Clock()

#some colours for your soul
red = 179
green = 217
blue = 255

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (96, 64, 32)
SKYBLUE = (red, green, blue)
GREEN = (63, 161, 66)

groundRect = pygame.Rect(0, 400, 1200, 300)

#text
beginText = pygame.image.load(os.path.join("Assets", "Text", "begin.png"))
beginHover = pygame.image.load(os.path.join("Assets", "Text", "begin-hover.png"))
beginRect = pygame.Rect(500, 470, 190, 70)
hovered = False
gameOvertext = pygame.image.load(os.path.join("Assets", "Text", "gameover.png"))
scoreText = pygame.image.load(os.path.join("Assets", "Text", "score.png"))
retryText = pygame.image.load(os.path.join("Assets", "Text", "retry.png"))
retryHover = pygame.image.load(os.path.join("Assets", "Text", "retry-hover.png"))
retryRect = pygame.Rect(500, 470, 190, 80)
pausedText = pygame.image.load(os.path.join("Assets", "Text", "paused.png"))

#dino spritesheets:
greenSheetidle = pygame.image.load(os.path.join("Assets", "PlayerDino", "green", "greenidle.png"))
greenSheetrun = pygame.image.load(os.path.join("Assets", "PlayerDino","green", "greenrun.png"))
greenSheetduck = pygame.image.load(os.path.join("Assets", "PlayerDino","green", "greenduck.png"))
greenSheetjump = pygame.image.load(os.path.join("Assets", "PlayerDino","green", "greenjump.png"))
greenSheethit = pygame.image.load(os.path.join("Assets", "PlayerDino","green", "greenhit.png"))
greenSheetlist = [greenSheetidle, greenSheetrun, greenSheetduck, greenSheetjump, greenSheethit]

redSheetidle = pygame.image.load(os.path.join("Assets", "PlayerDino", "red", "redidle.png"))
redSheetrun = pygame.image.load(os.path.join("Assets", "PlayerDino", "red", "redrun.png"))
redSheetduck = pygame.image.load(os.path.join("Assets", "PlayerDino", "red", "redduck.png"))
redSheetjump = pygame.image.load(os.path.join("Assets", "PlayerDino", "red", "redjump.png"))
redSheethit = pygame.image.load(os.path.join("Assets", "PlayerDino", "red", "redhit.png"))
redSheetlist = [redSheetidle, redSheetrun, redSheetduck, redSheetjump, redSheethit]

yellowSheetidle = pygame.image.load(os.path.join("Assets", "PlayerDino", "yellow", "yellowidle.png"))
yellowSheetrun = pygame.image.load(os.path.join("Assets", "PlayerDino", "yellow", "yellowrun.png"))
yellowSheetduck = pygame.image.load(os.path.join("Assets", "PlayerDino", "yellow", "yellowduck.png"))
yellowSheetjump = pygame.image.load(os.path.join("Assets", "PlayerDino", "yellow", "yellowjump.png"))
yellowSheethit = pygame.image.load(os.path.join("Assets", "PlayerDino", "yellow", "yellowhit.png"))
yellowSheetlist = [yellowSheetidle, yellowSheetrun, yellowSheetduck, yellowSheetjump, yellowSheethit]

blueSheetidle = pygame.image.load(os.path.join("Assets", "PlayerDino", "blue", "blueidle.png"))
blueSheetrun = pygame.image.load(os.path.join("Assets", "PlayerDino", "blue", "bluerun.png"))
blueSheetduck = pygame.image.load(os.path.join("Assets", "PlayerDino", "blue", "blueduck.png"))
blueSheetjump = pygame.image.load(os.path.join("Assets", "PlayerDino", "blue", "bluejump.png"))
blueSheethit = pygame.image.load(os.path.join("Assets", "PlayerDino", "blue", "bluehit.png"))
blueSheetlist = [blueSheetidle, blueSheetrun, blueSheetduck, blueSheetjump, blueSheethit]

colourList = [greenSheetlist, redSheetlist, yellowSheetlist, blueSheetlist]
colourChosen = 0

chosenSheets = [redSheetidle, redSheetrun, redSheetduck, redSheetjump, redSheethit]

#animation pointers
animationCooldown = 3
idlePointer = 0
pointer = 0
maxPointer = 5
animationStage = 1

#player variables
PLAYER_HEIGHT = 80
PLAYER_WIDTH = 55
startingX = 450
playerRect = pygame.Rect(450, 320, PLAYER_WIDTH, PLAYER_HEIGHT)
duckRect = pygame.Rect(510, 360, 80, 70)
Rects = []

#jumping variables
jumping = False
goingUp = False

#obstacle stuff
onscreenObstacles = []
obstacleType = ["jump", "duck", "jump", "jump"]
maxObstacles = 4
obstacleCountdown = 60
obstacleSpeed = 6
cloudSpeed = 3

#other important stuff
SCORE_FONT = pygame.font.Font("gamefont.ttf", 35)
gameOver = False
playerScore = 0
prevScore = 0
highScore = 0
scorecooldown = 15

animationsList = []  
     
#time for some background stuff
cloud1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Backgrounds", "Clouds", "cloud1.png")), (100, 50))
cloud2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Backgrounds", "Clouds", "cloud2.png")), (100, 50))
cloud3 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Backgrounds", "Clouds", "cloud3.png")), (100, 50))
cloud4 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Backgrounds", "Clouds", "cloud4.png")), (100, 50))
cloud5 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Backgrounds", "Clouds", "cloud5.png")), (100, 50))
cloud6 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Backgrounds", "Clouds", "cloud6.png")), (100, 50))
cloudList = [cloud1, cloud2, cloud3, cloud4, cloud5, cloud6]

deadlyLazer = pygame.image.load(os.path.join("Assets", "Backgrounds", "elsol.png"))

onscreenClouds = []
cloudCountdown = 20
dayTime = True

#now some SOUNDS
hitNoise = pygame.mixer.Sound(os.path.join("Assets", "Sounds", "hit.wav"))
boingNoise = pygame.mixer.Sound(os.path.join("Assets", "Sounds", "boing.wav"))
boingCountdown = 0
