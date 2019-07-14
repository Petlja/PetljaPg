import pygame as pg
import petljapg

prozor = petljapg.init(400,400)

boja = pg.Color("red")
pg.draw.circle(prozor, boja, (200,200), 100)

petljapg.run()
