import pygame as pg
import pygamebg

surface = pygamebg.open_window(500, 500, "Keyboard and mouse events")
pg.key.set_repeat(10,10)

x, y = 150, 150

def handle_event(d):
    global x, y
    if d.type == pg.MOUSEBUTTONDOWN:
        x,y = d.pos
        return True
    if d.type == pg.KEYDOWN:
        if d.key == pg.K_RIGHT:
            x += 1
        elif d.key == pg.K_LEFT:
            x -= 1
        elif d.key == pg.K_DOWN:
            y += 1
        elif d.key == pg.K_UP:
            y -= 1
        else:
            return False
        return True
    return False

def paint():
    surface.fill(pg.Color("white"))
    pg.draw.circle(surface, pg.Color("blue"), (x, y), 50)

pygamebg.event_loop(paint, handle_event)
