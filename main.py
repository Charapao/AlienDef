import pygame
from pygame.locals import *

import gamelib
from elements import Ball, Player

import math

class SquashGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    UPDATEROTATE = 90
    INITROTATE = 90
    def __init__(self):
        super(SquashGame, self).__init__('Squash', SquashGame.BLACK)
        self.ball = Ball(radius=10,
                         color=SquashGame.WHITE,
                         pos=(self.window_size[0]/2,
                              self.window_size[1]/2),
                         speed=(200,50))
        self.player = Player(pos=(180,490),
                             color=SquashGame.GREEN,startangle=self.INITROTATE)
        self.score = 0

    def init(self):
        super(SquashGame, self).init()
        self.render_score()

    def update(self):
        self.x0 = (200/320.0)
        self.y0 = 0
        self.x1 = (self.Get_Mouse[0]-200.0)
        self.y1 = (520.0-self.Get_Mouse[1])

        self.UPDATEROTATE = -(180/math.pi)*math.asin(((self.x0*self.x1)+(self.y0*self.y1))/((self.x0)*(math.sqrt(math.pow(self.x1,2)+math.pow(self.y1,2)))))
        if self.UPDATEROTATE > -60 and self.UPDATEROTATE < 60 :
           self.player.rot_center(self.UPDATEROTATE)
        # print "(%d, %d)" % self.Get_Mouse
        print self.UPDATEROTATE


    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, SquashGame.WHITE)

    def render(self, surface):
        self.player.render(surface)

    def __handle_events(self):
        super(SquashGame, self).init()


def main():
    game = SquashGame()
    game.run()

if __name__ == '__main__':
    main()