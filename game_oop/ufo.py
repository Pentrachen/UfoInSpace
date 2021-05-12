from settings import *
from sprite import Sprite
from bullet import Bullet

class Ufo(Sprite):

    def __init__(self):
        super().__init__(PFAD_UFO, UFO_x, UFO_y, None)
    
    def move_left(self):
        if self.x > 0:
            self.x -= SPEED_SPIELER
    
    def move_right(self):
         if self.x + self.width < WIN_WIDTH:
             self.x += SPEED_SPIELER
    
    def move_up(self):
        if self.y > 0:
            self.y -= SPEED_SPIELER
    
    def move_down(self):
         if self.y + self.height < WIN_HEIGHT:
             self.y += SPEED_SPIELER

    def schiessen(self):
        Bullet(PFAD_BULLET_UFO, self, SPEED_BULLET, bullets_ufo)
        

