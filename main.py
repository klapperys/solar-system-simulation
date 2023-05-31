import dataclasses
import sys
import pygame
from pygame.locals import *

#properties of sun
mass = 10000

#GUI
pygame.init()
pygame.display.init()
window = pygame.display.set_mode((1000, 1000))
red = (255,0,0)
circleX = 500
circleY = 400
radius = 10
sun = pygame.draw.circle(window, red, (circleX, circleY), radius),(mass)
pygame.display.update()
while True:
    pass


