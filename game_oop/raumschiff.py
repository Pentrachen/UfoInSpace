from settings import *
from sprite import Sprite
from bullet import Bullet
import random
import time

# import pygame
# from pathlib import Path

class Raumschiff(Sprite):

    def __init__(self):
        super().__init__(PFAD_RAUMSCHIFF, WIN_WIDTH, 200, raumschiffe)
        self.set_pos()
        self.last_shot = pygame.time.get_ticks()
    
    def set_pos(self):      # zufällige y-Pos bestimmen
        self.y = random.randint(100, WIN_HEIGHT - 100)

    def move(self):
        self.x -= SPEED_RAUMSCHIFF
        self.schiessen()
        if self.x + self.width < 0:
            self.x = WIN_WIDTH
    
    def schiessen(self):
        now = pygame.time.get_ticks()
        if now >= self.last_shot + DELAY:
            Bullet(PFAD_BULLET_GEGNER, self, -SPEED_BULLET, bullets_gegner)
            self.last_shot = now
