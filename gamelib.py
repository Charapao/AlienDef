import pygame
from pygame.locals import *
from elements import *
import math

class SimpleGame(object):

    def __init__(self,
                 title,
                 background_color,
                 window_size=(400,530),
                 fps=60):
        self.title = title
        self.window_size = window_size
        self.fps = fps
        self.background_color = background_color
        self.countofbullet = 0
        self.Sizeof_Bullet = 1000
        self.is_terminated = False

    def __game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)

    def __handle_events(self):
        self.mouse = ((0,0), 0, 0, 0, 0, 0, 0)
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYDOWN:
                self.on_key_down(event.key)
            elif event.type == KEYUP:
                self.on_key_up(event.key)
            elif event.type == pygame.MOUSEMOTION:
                self.Get_Mouse = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.UPDATEROTATE > -60 and self.UPDATEROTATE < 60 :
                    self.isCreateBullet = True
                    # print self.UPDATEROTATE
                    if self.countofbullet< self.Sizeof_Bullet :
                       self.countofbullet = self.countofbullet + 1
                    self.FireNow[self.countofbullet]= True
                    bul = Bullet(radius=10,pos=(195,505),angleCheckmouse=self.UPDATEROTATE,index = len(self.bullets) - 1,speed=(-200*math.sin(math.pi/180*self.UPDATEROTATE),-200*math.cos(math.pi/180*self.UPDATEROTATE)))
                    self.bullets.append(bul)
                      
                
    def terminate(self):
        self.is_terminated = True

    def run(self):
        self.init()
        while not self.is_terminated:
            self.__handle_events()

            self.update()

            self.surface.fill(self.background_color)
            self.render(self.surface)
            pygame.display.update()

            self.clock.tick(self.fps)

    def is_key_pressed(self, key):
        keys_pressed = pygame.key.get_pressed()
        if key < 0 or key >= len(keys_pressed):
            return False
        return (keys_pressed[key])

    def init(self):
        self.__game_init()

    def update(self):
        pass

    def render(self, surface):
        pass

    def on_key_up(self, key):
        pass

    def on_key_down(self, key):
        pass
