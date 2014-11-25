import pygame
from pygame.locals import *

import gamelib
from elements import Ball, Player

class SquashGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    V = 0
    
    def __init__(self):
        super(SquashGame, self).__init__('Squash', SquashGame.BLACK)
        self.ball = Ball(radius=10,
                         color=SquashGame.WHITE,
                         pos=(self.window_size[0]/2,
                              self.window_size[1]/2),
                         speed=(200,50))
        self.player = Player(pos=(180,470),
                             color=SquashGame.GREEN,startangle=90)
        self.score = 0
        # v = 0


    def init(self):
        super(SquashGame, self).init()
        self.render_score()

    def update(self):
        self.V=self.V+1
        if self.V > 70 :
            self.V = -70 
        self.player.rotate(self.V)        

    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, SquashGame.WHITE)

    def render(self, surface):
        self.player.render(surface)
def main():
    game = SquashGame()
    game.run()

if __name__ == '__main__':
    main()