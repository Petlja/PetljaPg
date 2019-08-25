import pygame as pg
import pygamebg

surface = pygamebg.open_window(500, 500, "Keyboard and mouse events")
pg.key.set_repeat(10,10)

x, y = 150, 150

def clicked(e):
    global x, y
    x,y = e.pos
    return True

def keypressed(e):
    global x,y
    if e.key == pg.K_RIGHT:
        x += 1
    elif e.key == pg.K_LEFT:
        x -= 1
    elif e.key == pg.K_DOWN:
        y += 1
    elif e.key == pg.K_UP:
        y -= 1
    else:
        return False
    return True

def paint():
    surface.fill(pg.Color("white"))
    pg.draw.circle(surface, pg.Color("blue"), (x, y), 50)

pygamebg.event_loop(paint, {pg.MOUSEBUTTONDOWN:clicked, pg.KEYDOWN:keypressed})
