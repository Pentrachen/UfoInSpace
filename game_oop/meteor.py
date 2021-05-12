from settings import *
from sprite import Sprite
import random

class Meteor(Sprite):

    def __init__(self):
        super().__init__(PFAD_METEOR, 200, WIN_HEIGHT, None)
        self.set_pos()
        self.last_shot = pygame.time.get_ticks()
    
    def set_pos(self):      # zufällige y-Pos bestimmen
        self.x = random.randint(100, WIN_WIDTH - 100)

    def move(self):
        self.y += SPEED_METEOR
        self.schiessen()
        if self.y + self.height < 0:
            self.y = WIN_HEIGHT