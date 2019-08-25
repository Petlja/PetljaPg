import pygame as pg
import pygamebg

width, height = 500, 300
surface = pygamebg.open_window(width, width, "Increasing and decreasing speed")
pg.key.set_repeat(10,10)

fps = 30
x, y = 150, 150
vx, vy = 0, 0

def update():
    global x,y
    x = (x + vx/fps) % width
    y = (y + vy/fps) % height

    surface.fill(pg.Color("white"))
    color = pg.Color("red")
    pg.draw.circle(surface, color, (int(x), int(y)), 30)

def handle_event(d):
    global vx, vy
    if d.type == pg.KEYDOWN:
        if d.key == pg.K_RIGHT:
            vx += 1
        elif d.key == pg.K_LEFT:
            vx -= 1
        elif d.key == pg.K_DOWN:
            vy += 1
        elif d.key == pg.K_UP:
            vy -= 1

pygamebg.frame_loop(fps, update, handle_event)
