from settings import *
from sprite import Sprite

class Bullet(Sprite):

    def __init__(self, bilddatei, sprite, speed, lst):
        super().__init__(bilddatei, sprite.x + sprite.width/2, sprite.y + sprite.height/2, lst)
        self.speed = speed
            
    def move(self):
        self.x += self.speed
        if self.x > WIN_WIDTH or self.x +self.width < 0:
            self.lst.remove(self)

        