import pygame as pg
import petljapg

x = 150
y = 150

#Evo kako bismo mogli da pojednostavimo reagovanje na klika miša
for frm in petljapg.frames(30, 500,300):
    platno = frm.surface
    platno.fill(pg.Color("white"))
    if pg.mouse.get_pressed()[0]:
        x, y = pg.mouse.get_pos()
    pg.draw.circle(platno, pg.Color("blue"), (x, y), 50)
    