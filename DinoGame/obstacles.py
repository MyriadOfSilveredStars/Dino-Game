import pygame
pygame.init()

class Obstacles:
    def __init__(self, height, width, image, recta):
        self.height = height
        self.width = width
        self.image = image
        self.Rect = recta

class Clouds:
    def __init__(self, width, height, image, recta):
        self.width = width
        self.height = height
        self.image = image
        self.Rect = recta

class Sky:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def skyfade(self):
        self.red -= 1
        self.green -= 1
        self.blue -= 1