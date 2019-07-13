import pygame as pg
import petljapg

tri_boje = [pg.Color("red"), pg.Color("yellow"), pg.Color("green")]

for frm in petljapg.frames(rate=1, size=(400,400)):
    boja = tri_boje[frm.sequence % 3]
    pg.draw.circle(frm.surface, boja, (200,200), 100)
