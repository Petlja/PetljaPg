import pygame as pg
import petljapg


prozor = petljapg.init(500,300,"Loptica")

x = 150
y = 150
v= 1

for frm in petljapg.frames(30):
    prozor.fill(pg.Color("white"))
    pressed = pg.key.get_pressed()
    if pressed[pg.K_RIGHT]: x += v
    if pressed[pg.K_LEFT]: x -= v
    if pressed[pg.K_DOWN]: y += v
    if pressed[pg.K_DOWN]: y += v
    if pressed[pg.K_UP]: y -= v
    boja = pg.Color("red")
    pg.draw.circle(prozor, boja, (x, y), 30)
    