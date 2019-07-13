import pygame as pg
import petljapg


x = 150
y = 150
vx = 0
vy = 0

# crtanje možemo lako odvojiti u posebnu funkciju, ali na to
# možemo da pređemo kada nam bude zaista zatrebalo, ne moramo
# od početka

def crtaj(platno):
    platno.fill(pg.Color("white"))
    boja = pg.Color("red")
    pg.draw.circle(platno, boja, (int(x), int(y)), 30)

for frm in petljapg.frames(rate=30, size=(500,300)):
    sirina, visina = frm.surface.get_size()

    vx = vx + frm.key_right_count() - frm.key_left_count()
    x = (x + vx * frm.period) % sirina

    vy = vy + frm.key_down_count() - frm.key_up_count()
    y = (y + vy * frm.period) % visina

    crtaj(frm.surface)
