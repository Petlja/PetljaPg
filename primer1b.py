import pygame as pg
import petljapg

pg.init()  # inicijalizujemo rad biblioteke PyGame
pg.display.set_caption("Хватање јабука")  # otvaramo prozor
(sirina, visina) = (500, 300)
platno = pg.display.set_mode((sirina, visina))

pg.key.set_repeat(10, 10)  # podešavamo dogadjaje tastature

x = 150
y = 150

# pygame je vec inicijalizovan
for frm in petljapg.frames(rate=30):
    platno.fill(pg.Color("white"))
    x = x + frm.key_right_count() - frm.key_left_count()
    y = y + frm.key_down_count() - frm.key_up_count()
    boja = pg.Color("red")
    pg.draw.circle(platno, boja, (x, y), 30)

# ako se ne managuje init u frames(), ne manageuje se ni quit
pg.quit()
