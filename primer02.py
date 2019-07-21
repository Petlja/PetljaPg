import pygame as pg
import petljapg


prozor = petljapg.open_window(300, 300, "get_pressed()")

x = 150
y = 150
v= 1

def osvezi():
    global x, y
    prozor.fill(pg.Color("white"))
    pritisnuto = pg.key.get_pressed()
    if pritisnuto[pg.K_RIGHT]:
        x += v
    if pritisnuto[pg.K_LEFT]:
        x -= v
    if pritisnuto[pg.K_DOWN]:
        y += v
    if pritisnuto[pg.K_UP]:
        y -= v
    boja = pg.Color("red")
    pg.draw.circle(prozor, boja, (x, y), 30)

petljapg.frame_loop(30, osvezi)
