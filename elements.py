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

    def __init__(self, pos, color, startangle, width=100):
        self.width = width
        # (self.x,self.y) = pos
        self.color = color
        self.image = pygame.image.load("cannon.png")
        self.original = self.image
        self.pos =pos
        self.rotate(startangle)

    def rotate(self, angle):
     	self.image = pygame.transform.rotate(self.original, angle)
    
    def render(self,surface):
    	surface.blit(self.image, self.pos)

        


        
