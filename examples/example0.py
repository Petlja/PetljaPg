import pygame as pg

pg.init()
surface = pg.display.set_mode((400,400))
pg.display.set_caption("Blue circle")

pg.draw.circle(surface, pg.Color("blue"), (200,200), 100)

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()
