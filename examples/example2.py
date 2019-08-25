import pygame as pg
import pygamebg

surface = pygamebg.open_window(300, 300, "Read keyboard state")

x, y = 150, 150

def update():
    global x, y
    surface.fill(pg.Color("white"))
    pressed = pg.key.get_pressed()
    if pressed[pg.K_RIGHT]:
        x += 1
    if pressed[pg.K_LEFT]:
        x -= 1
    if pressed[pg.K_DOWN]:
        y += 1
    if pressed[pg.K_UP]:
        y -= 1
    pg.draw.circle(surface , pg.Color("red"), (x, y), 30)

pygamebg.frame_loop(30, update)
