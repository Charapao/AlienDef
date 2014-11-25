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
        self.color = color
        self.image = pygame.image.load("cannon.png")
        self.original = self.image
        self.pos =pos
        self.rotate(startangle)

    def rot_center(self, angle):
        self.orig_rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.original, angle)
        self.rot_rect = self.orig_rect.copy()
        self.rot_rect.center = self.image.get_rect().center
        self.image = self.image.subsurface(self.rot_rect).copy()
        return self.image

    def rotate(self, angle):
     	self.image = pygame.transform.rotate(self.original, angle)
    
    def render(self,surface):
    	surface.blit(self.image, self.pos)

        


        
