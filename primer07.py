import pygame as pg
import petljapg

prozor = petljapg.open_window(500, 500, "Mis")
pg.key.set_repeat(10,10)
x = 150
y = 150

def obradi_dogadjaj(d):
    global x, y
    if d.type == pg.MOUSEBUTTONDOWN:
        x,y = d.pos
        return True
    if d.type == pg.KEYDOWN:
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
    return False

def crtaj():
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("blue"), (x, y), 50)

petljapg.event_loop(crtaj, obradi_dogadjaj)
