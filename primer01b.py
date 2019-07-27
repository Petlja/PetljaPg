import pygame as pg
import petljapg

pg.init() # i dalje legitimno da se zove odvojeno

font = pg.font.SysFont("Arial", 60)
tekst = "Пример исписивања текста"
slika_teksta = font.render(tekst, True, pg.Color("green"))
w, h = slika_teksta.get_width(), slika_teksta.get_height()

prozor = petljapg.open_window(w, h, "Primer 1")
prozor.fill(pg.Color("black"))
prozor.blit(slika_teksta, (0, 0))

petljapg.wait_loop()
