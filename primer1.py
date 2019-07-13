import pygame as pg
import petljapg

x = 150
y = 150

for frm in petljapg.frames(rate=30, size=(500,300)):
    platno = frm.surface
    platno.fill(pg.Color("white"))
    x = x + frm.key_right_count() - frm.key_left_count()
    y = y + frm.key_down_count() - frm.key_up_count()
    boja = pg.Color("red")
    pg.draw.circle(platno, boja, (x, y), 30)
    