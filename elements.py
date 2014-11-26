import pygame
from pygame.locals import *
import math

class Bullet(object):

    def __init__(self, radius, pos,angleCheckmouse, speed=(200,0)):
        (self.x, self.y) = pos
        (self.vx, self.vy) = speed
        self.radius = radius
        self.image = pygame.image.load("bulletcannon.png")
        self.rect = self.image.get_rect()
        self.angleCheckmouse = angleCheckmouse
        # self.x = self.x*math.cos(angleCheckmouse)
        # self.y = self.y*math.cos(angleCheckmouse)

    def update(self, delta_t, display, player ):
        global score, game_over
        self.x += self.vx*delta_t
        self.y += self.vy*delta_t

        if self.x < self.radius-10:
            self.vx = abs(self.vx)
        # if self.y < self.radius:
        #     self.vy = abs(self.vy)
        if self.x > display.get_width()-self.radius:
            self.vx = -abs(self.vx)
        if self.y > display.get_height()-self.radius:
            self.vy = -abs(self.vy)

    def render(self, surface):
        surface.blit(self.image, (self.x,self.y))


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

        


        
