import pygame
from pygame.locals import *

import gamelib
from elements import Bullet, Player

import math

class SquashGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    UPDATEROTATE = 90
    CHAGNETODEGREE = (180/math.pi)
    
    INITROTATE = 90
    def __init__(self):
        super(SquashGame, self).__init__('Squash', SquashGame.GREEN)
        self.player = Player(pos=(180,490),
                             color=SquashGame.GREEN,startangle=self.INITROTATE)
        self.score = 0
        self.bullets = []
        self.FireNow = []
        self.isCreateBullet = False
        self.counttemp = 0

        for x in range(0,self.Sizeof_Bullet):
            self.FireNow.append(False)

    def init(self):
        super(SquashGame, self).init()
        self.render_score()

    def update(self):
        self.x0 = (200/320.0)
        self.y0 = 0
        self.x1 = (self.Get_Mouse[0]-200.0)
        self.y1 = (520.0-self.Get_Mouse[1])        
        self.VECTOR_CHECK_MOUSE = math.asin(((self.x0*self.x1)+(self.y0*self.y1))/
          ((self.x0)*(math.sqrt(math.pow(self.x1,2)+math.pow(self.y1,2)))))
        self.UPDATEROTATE = -self.CHAGNETODEGREE*self.VECTOR_CHECK_MOUSE
        if self.UPDATEROTATE > -60 and self.UPDATEROTATE < 60 :
           self.player.rot_center(self.UPDATEROTATE)
        if self.isCreateBullet == True :
           self.counttemp = self.count 
        if self.count > 0 or self.count <  self.counttemp :
           for x in range(0,self.counttemp):
               self.bullets[x].update(1./self.fps, self.surface, self.player)
        
   
            
            




    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, SquashGame.WHITE)

    def render(self, surface):
        for x in self.bullets :
            x.render(surface)
        self.player.render(surface)

    def __handle_events(self):
        super(SquashGame, self).init()


def main():
    game = SquashGame()
    game.run()

if __name__ == '__main__':
    main()