import pygame as pg
import petljapg

prozor = petljapg.init(400,400)

def nov_frejm(frm):
    tri_boje = [pg.Color("red"), pg.Color("yellow"), pg.Color("green")]
    boja = tri_boje[frm.sequence %3]
    pg.draw.circle(prozor, boja, (200,200), 100)

petljapg.run(2, nov_frejm)
