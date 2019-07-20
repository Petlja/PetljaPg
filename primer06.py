import pygame as pg
import petljapg


prozor = petljapg.open_window(500, 500, "Mis")
x = 150
y = 150

def obradi_dogadjaj(d):
    global x, y
    if d.type == pg.MOUSEBUTTONDOWN:
        x,y = d.pos

def osvezi_frejm():
    global x ,y
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color("blue"), (x, y), 50)

petljapg.frame_loop(30, osvezi_frejm, obradi_dogadjaj)
