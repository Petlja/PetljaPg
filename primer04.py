import pygame as pg
import petljapg


prozor = petljapg.open_window(500, 500, "Mis")
x = 150
y = 150

def osvezi():
    global x ,y
    prozor.fill(pg.Color("white"))
    if pg.mouse.get_pressed()[0]:
        x, y = pg.mouse.get_pos()
    pg.draw.circle(prozor, pg.Color("blue"), (x, y), 50)

petljapg.frame_loop(30, osvezi)
