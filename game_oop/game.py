from settings import *
from sprite import Sprite
from raumschiff import Raumschiff
from ufo import Ufo
from bullet import Bullet
from meteor import Meteor

pygame.init()      
pygame.display.set_caption("First Game")               

INFO_FONT = pygame.font.SysFont("Arial", 32)
GAME_FONT = pygame.font.SysFont("Arial", 24)

punkte = 0
leben = 3

info_string = 'Zum Starten\ndes Spiels\nbitte Enter drücken'
spiel_lauft = False

def main():
    clock = pygame.time.Clock()      # Bildschirm Aktualisierungen einstellen
    global ufo
    ufo = Ufo()

    while True:                # Schleife Hauptprogramm
        clock.tick(FPS)              # Anzahl der Aktualisierungen pro Sekunde    
        #print(f'bullets: {len(bullets_ufo)}')  
        steuerung()
        if spiel_lauft:
            kollisionen_pruefen()
            bewegung()   
            anzeige()
        else:
            info_anzeigen()

def spiel_starten():
    global spiel_lauft, ufo
    spiel_lauft = True
    init_vars()
    Raumschiff()
    ufo = Ufo()
    Meteor()

def steuerung():   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ufo.schiessen()
            if event.key == pygame.K_RETURN and not spiel_lauft:
                spiel_starten()

    keys_pressed = pygame.key.get_pressed()     # "Dauerfeuer"
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        ufo.move_left() 
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:  # RIGHT
        ufo.move_right()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:     # UP
        ufo.move_up()
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:   # DOWN
        ufo.move_down()

def kollisionen_pruefen():
    global leben, punkte, spiel_lauft, info_string
    if ufo.collides_with(raumschiffe) or ufo.collides_with(bullets_gegner):
        leben -= 1
        spiel_lauft = False
        if leben > 0:
            info_string = f'Sie haben noch {leben} Leben.\nZum Weiterspielen\nbitte Enter drücken'
        else:
            info_string = f'Sie haben leider verloren,\nFür ein neues Spiel\ndrücken Sie bitte Enter'
            punkte, leben = 0, 3
    for raumschiff in raumschiffe:      # Treffer auf Gegner
        if raumschiff.collides_with(bullets_ufo):
            raumschiffe.remove(raumschiff)  # raumschiff entfernen
            punkte += 1     # punkte erhöhen
            Raumschiff()
    for bullet in bullets_ufo:
        if bullet.collides_with(bullets_gegner):
            bullets_ufo.remove(bullet)

def bewegung():
    for sprite in bullets_ufo  + bullets_gegner + raumschiffe:
        sprite.move()

def anzeige():
    WIN.fill(WHITE)
    ufo.draw()
    for sprite in bullets_ufo + bullets_gegner + raumschiffe:
        sprite.draw()

    punkte_anzeige = GAME_FONT.render(f'Punkte: {punkte}', 1, RED)
    leben_anzeige = GAME_FONT.render(f'Leben: {leben}', 1, RED)
    WIN.blit(punkte_anzeige, (5, 5))
    WIN.blit(leben_anzeige, (WIN_WIDTH-85, 5))
    pygame.display.update()

def info_anzeigen():
    WIN.fill(WHITE)
    zeilen = info_string.split('\n')
    n = len(zeilen)                 # Anzahl der Zeilen
    h = INFO_FONT.get_linesize()    # Zeilenhöhe
    y_off = (WIN_HEIGHT - (n-1)*h) / 2
    for i in range(n):
        text = INFO_FONT.render(zeilen[i], 1, RED)
        frame = text.get_rect(center = (WIN_WIDTH / 2, y_off + i * h))
        WIN.blit(text, frame)
    pygame.display.update()

if __name__ == "__main__":
    main()
