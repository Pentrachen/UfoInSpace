
import pygame       # Importieren der Pygame-Bibliothek
import pygame.freetype  # Import the freetype module.
from pathlib import Path

WIN_WIDTH = 800
WIN_HEIGHT = 400

PFAD_UFO = 'ufo.png'
PFAD_RAUMSCHIFF = 'raumschiff.png'
PFAD_BULLET_UFO = 'bullet_ufo.png'
PFAD_BULLET_GEGNER = 'bullet_gegner.png'
PFAD_METEOR = 'Meteor.png'

UFO_x = 100
UFO_y = 200

FPS = 60            # Frames per second
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SPEED_SPIELER = 6
SPEED_RAUMSCHIFF = 3
SPEED_BULLET = 13
SPEED_METEOR = 7

DELAY = 1000    # Zeit zwischen zwei Raumschiff-Schüssen [ms]

ICON_PATH = Path.joinpath(Path(__file__).parent, "bilder")
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Fenster öffnen

bullets_ufo = []
bullets_gegner = []
raumschiffe = []

def init_vars():
    bullets_ufo.clear()
    bullets_gegner.clear()
    raumschiffe.clear()

