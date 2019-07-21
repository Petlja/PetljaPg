import pygame as pg
import petljapg

prozor = petljapg.open_window(500, 500, "Mis")
pg.key.set_repeat(10,10)
x = 150
y = 150

def klik(d):
    global x, y
    x,y = d.pos
    return True

def taster(d):
    global x,y
    if d.key == pg.K_RIGHT:
        x += 1
    elif d.key == pg.K_LEFT:
        x -= 1
    elif d.key == pg.K_DOWN:
        y += 1
    elif d.key == pg.K_UP:
        y -= 1
    else:
        return False
    return True

def crtaj():
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("blue"), (x, y), 50)

petljapg.frame_loop(30, crtaj, {pg.MOUSEBUTTONDOWN:klik, pg.KEYDOWN:taster})
