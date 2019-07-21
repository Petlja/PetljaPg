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

def klik(d):
    global x, y, vx, vy
    x, y = d.pos
    vx, vy = 0, 0

def taster(d):
    global vx, vy
    if d.key == pg.K_RIGHT:
        vx += 1
    elif d.key == pg.K_LEFT:
        vx -= 1
    elif d.key == pg.K_DOWN:
        vy += 1
    elif d.key == pg.K_UP:
        vy -= 1

def osvezi():
    global x, y
    x = (x + vx/fps) % sirina
    y = (y + vy/fps) % visina
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("blue"), (x, y), 50)

petljapg.frame_loop(30, osvezi, {pg.MOUSEBUTTONDOWN:klik, pg.KEYDOWN:taster})
