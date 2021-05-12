from settings import *

class Sprite(pygame.Rect):
    def __init__(self, bilddatei, x, y, lst = None):
        self.img = pygame.image.load(Path.joinpath(ICON_PATH, bilddatei))
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        if isinstance(lst, list):
            self.lst = lst
        else:
            self.lst = []
        self.lst.append(self)
   
    def draw(self):
        WIN.blit(self.img, (self))
    
    def collides_with(self, lst):
        for sprite in lst:
            if self.colliderect(sprite):
                lst.remove(sprite)
                return True
        return False
