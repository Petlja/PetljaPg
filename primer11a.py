import random
import pygame as pg
import petljapg

prozor = petljapg.init(400,400)
random.seed()

for frm in petljapg.frames(2):
    tri_boje = [pg.Color("red"), pg.Color("yellow"), pg.Color("green")]
    boja = tri_boje[random.randrange(3)]
    pg.draw.circle(prozor, boja, (200,200), 100)
