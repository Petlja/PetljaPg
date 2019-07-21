import pygame as pg
import petljapg

sirina, visina = 500, 300
prozor = petljapg.open_window(500, 500, "Dodavanje i oduzimanje brzine")
pg.key.set_repeat(10,10)
fps = 30

x = 150
y = 150
vx = 0
vy = 0

def osvezi():
    global x,y
    x = (x + vx/fps) % sirina
    y = (y + vy/fps) % visina

    prozor.fill(pg.Color("white"))
    boja = pg.Color("red")
    pg.draw.circle(prozor, boja, (int(x), int(y)), 30)

def obradi_dogadjaj(d):
    global vx, vy
    if d.type == pg.KEYDOWN:
        if d.key == pg.K_RIGHT:
            vx += 1
        elif d.key == pg.K_LEFT:
            vx -= 1
        elif d.key == pg.K_DOWN:
            vy += 1
        elif d.key == pg.K_UP:
            vy -= 1

petljapg.frame_loop(fps, osvezi, obradi_dogadjaj)
