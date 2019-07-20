import pygame as pg
import petljapg

prozor = petljapg.open_window(500, 500, "Miš")
x = 150
y = 150

def obradi_dogadjaj(d):
    global x, y
    if d.type == pg.MOUSEBUTTONDOWN:
        x,y = d.pos
        return True
    return False

def crtaj():
    global x ,y
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("blue"), (x, y), 50)

petljapg.event_loop(crtaj, obradi_dogadjaj)
