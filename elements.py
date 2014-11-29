import pygame
from pygame.locals import *
import math
from random import randint

class Bullet(object):

    def __init__(self, radius, pos,angleCheckmouse,index, speed=(200,0)):
        (self.x, self.y) = pos
        (self.vx, self.vy) = speed
        self.radius = radius
        self.image = pygame.image.load("bulletcannon.png")
        self.index = index
        self.rect = self.image.get_rect()
        self.angleCheckmouse = angleCheckmouse
        self.bulletrect = pygame.Rect(self.x, self.y, 10, 10)

    def update(self, delta_t, display, player, enemyrect):
        global score, game_over
        self.x += self.vx*delta_t
        self.y += self.vy*delta_t
        self.bulletrect = pygame.Rect(self.x, self.y, 10, 10)
        self.Collision(enemyrect)

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
        pygame.draw.rect(surface, pygame.Color('black'), self.bulletrect, 3)

    def Collision(self, enemyrect):
        if enemyrect.colliderect(self.bulletrect):
           self.CollisionEnemy = True
           self.x = 1000
           self.y = 1000
           # print self.CollisionEnemy
           

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

#########################################
class Enemy(object):

    def __init__(self, pos,speed):
        (self.x, self.y) = pos
        self.speed= speed
        self.image = pygame.image.load("ufo.png")
        self.enemyrect = pygame.Rect(self.x, self.y, 30, 30)
    
    def update(self, delta_t, bulletrect):
        self.y += self.speed*delta_t
        self.enemyrect = pygame.Rect(self.x, self.y, 30, 30)
        self.Collision(bulletrect)
    
    def render(self,surface):
        surface.blit(self.image, (self.x,self.y))
        pygame.draw.rect(surface, pygame.Color('black'), self.enemyrect, 3)

    def Collision(self, bulletrect):
        if bulletrect.colliderect(self.enemyrect):
           self.CollisionEnemy = True
           self.x = 5000
           self.y = 1000
           print self.CollisionEnemy

        


        
