import pygame
from pygame.locals import *

import gamelib
from elements import Bullet, Player, Enemy

import math
from random import randint

import time

class SquashGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    UPDATEROTATE = 90
    CHAGNETODEGREE = (180/math.pi)
    
    INITROTATE = 90
    def __init__(self):
        super(SquashGame, self).__init__('Squash', SquashGame.WHITE)
        self.player = Player(pos=(180,490),
                             color=SquashGame.GREEN,startangle=self.INITROTATE)
        self.enemy = Enemy(pos =(200,50),speed = 30)
        self.enemies = []
        self.score = 0
        self.bullets = []
        self.FireNow = []
        self.randomtemp = 0
        self.randomtemp = 0
        print self.randomtemp
        self.start_time = time.time()
        self.end_time = 0
        self.end_time_2 = 0
        self.timetemp = 0
        self.isCreateBullet = False
        self.Current_CountofBullet = 0
        self.CollisionEnemy = False
        self.indexcurrent = 0
        self.enemies.append(Enemy(pos =(40,50),speed = 30))
        for x in range(0,self.Sizeof_Bullet):
            self.FireNow.append(False)

    def init(self):
        super(SquashGame, self).init()
        self.render_score()

    def update(self):
        self.timetemp = self.timetemp + 1
        self.end_time = time.time()
        if self.end_time-self.start_time >= 4.0 :
            self.start_time=self.end_time
            self.randomtemp = randint(20,380)
            self.enemies.append(Enemy(pos =(1*self.randomtemp,-20),speed = 30+(0.1)*self.timetemp))
            self.Sizeof_Enemy = self.Sizeof_Enemy+1
            # print "kuy"
            # self.enemies.pop()
            # print "pop law"
            # self.enemies.append(Enemy(pos =(1*self.randomtemp,-20),speed = 30+(1)*self.timetemp))
        # print self.end_time-self.start_time

        
        # if self.countofbullet == 1:
             # for x in range(self.Sizeof_Enemy):
                # self.enemy = Enemy(pos =(40,50),speed = 30)
                # self.enemies.append(Enemy(pos =(40*self.randomtemp,50*self.randomtemp),speed = 30))
        self.UPDATEROTATE = -self.CHAGNETODEGREE*self.Cal_VectorMouse()
        ### Lock Angle Cannon can rotate
        if self.UPDATEROTATE > -60 and self.UPDATEROTATE < 60 :
           self.player.rot_center(self.UPDATEROTATE)
        ##################################################################
        if self.isCreateBullet == True :
           self.Current_CountofBullet = self.countofbullet 
        if self.countofbullet > 0 or self.countofbullet <  self.Current_CountofBullet :
           for x in range(0,self.Current_CountofBullet):
               # self.bullets[x].update(1./self.fps, self.surface, self.player,self.enemy.enemyrect)
               for i in range(self.Sizeof_Enemy):
                 self.bullets[x].update(1./self.fps, self.surface, self.player,self.enemies[i].enemyrect)

        for x in range(0,self.Current_CountofBullet):
            # self.enemy.update(1./(self.fps*self.Current_CountofBullet),self.bullets[x].bulletrect)
            for j in range(self.Sizeof_Enemy):
                self.enemies[j].update(1./(self.fps*self.Current_CountofBullet),self.bullets[x].bulletrect)

        # self.enemy.update(1./self.fps,self.bullets.bullet)


    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, SquashGame.BLACK)

    def render(self, surface):
        for x in self.bullets :
            x.render(surface)
        self.player.render(surface)
        for x in self.enemies:
            x.render(surface)
        # self.enemy.render(surface)

    def __handle_events(self):
        super(SquashGame, self).init()

    def Cal_VectorMouse(self):
        self.x0 = (200/320.0)
        self.y0 = 0
        self.x1 = (self.Get_Mouse[0]-200.0)
        self.y1 = (520.0-self.Get_Mouse[1])
        self.VECTOR_CHECK_MOUSE = math.asin(((self.x0*self.x1)+(self.y0*self.y1))/
          ((self.x0)*(math.sqrt(math.pow(self.x1,2)+math.pow(self.y1,2)))))
        return self.VECTOR_CHECK_MOUSE

    
def main():
    game = SquashGame()
    game.run()

if __name__ == '__main__':
    main()