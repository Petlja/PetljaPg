import pygame as pg
import petljapg

x = 150
y = 150

tri_boje = [pg.Color("red"), pg.Color("yellow"), pg.Color("green")]
izbor_boje = 0

# u elementarnim primerima ne insistiramo na podeli ažuriranja stanja i crtanja
# u nekom trenutku ćemo izvući crtanje u posebnu funkciju
for frm in petljapg.frames(30, 500, 300):
    platno = frm.surface
    platno.fill(pg.Color("black"))
    x = x + frm.key_right_count() - frm.key_left_count()
    y = y + frm.key_down_count() - frm.key_up_count()
    izbor_boje = (izbor_boje + frm.key_space_count()) % 3
    boja = tri_boje[izbor_boje]
    pg.draw.circle(platno, boja, (x, y), 30)
    