import pygame
from pygame.locals import *

class Ball(object):

    def __init__(self, radius, color, pos, speed=(100,0)):
        (self.x, self.y) = pos
        (self.vx, self.vy) = speed
        self.radius = radius
        self.color = color


#########################################
class Player(object):

    def __init__(self, pos, color, width=100):
        self.width = width
        self.pos = pos
        self.color = color

        


        
