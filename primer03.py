import pygame as pg
import petljapg

sirina, visina = 500, 300
prozor = petljapg.open_window(500, 500, "Dodavanje i oduzimanje brzine")

x = 150
y = 150
vx = 0
vy = 0

fps = 30

def crtaj_frejm():
    global x,y,vx,vy
    pritisnuto = pg.key.get_pressed()
    if pritisnuto[pg.K_RIGHT]:
        vx += 1
    if pritisnuto[pg.K_LEFT]:
        vx -= 1
    if pritisnuto[pg.K_DOWN]:
        vy += 1
    if pritisnuto[pg.K_UP]:
        vy -= 1

    x = (x + vx/fps) % sirina
    y = (y + vy/fps) % visina

    prozor.fill(pg.Color("white"))
    boja = pg.Color("red")
    pg.draw.circle(prozor, boja, (int(x), int(y)), 30)


petljapg.frame_loop(fps, crtaj_frejm)
