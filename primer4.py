import pygame as pg
import petljapg

x = 150
y = 150

#Evo kako bismo mogli da pojednostavimo reagovanje na klika miša
for frm in petljapg.frames(rate=30, size=(500,300)):
    platno = frm.surface
    platno.fill(pg.Color("white"))
    if frm.mouse_left_clicked():
        x, y = frm.mouse_pos
    pg.draw.circle(platno, pg.Color("blue"), (x, y), 50)
    