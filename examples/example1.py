import pygame as pg
import pygamebg

surface = pygamebg.open_window(400, 400, "Blue circle")

pg.draw.circle(surface, pg.Color("blue"), (200,200), 100)

pygamebg.wait_loop()
