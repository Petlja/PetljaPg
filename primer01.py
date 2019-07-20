import pygame as pg
import petljapg



prozor = petljapg.open_window(400,400,"Primer 1")

boja = pg.Color("red")
pg.draw.circle(prozor, boja, (200,200), 100)

petljapg.wait_loop()
