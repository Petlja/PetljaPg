import pygame as pg


def open_window(width, height, caption):
    pg.init()
    surface = pg.display.set_mode((width,height))
    pg.display.set_caption(caption)
    return surface

def wait_loop():
    pg.display.update()
    while pg.event.wait().type != pg.QUIT:
        pass
    pg.quit()

def frame_loop(rate, update_frame, handle_event=None):
    clock = pg.time.Clock() 
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if handle_event:
                handle_event(event)
        update_frame()
        pg.display.update()
        clock.tick(rate)

def event_loop(draw, handle_event):
    draw()
    pg.display.update()
    while True:
        treba_crtati = False
        for dogadjaj in [pg.event.wait()] + pg.event.get():
            if dogadjaj.type == pg.QUIT:
                pg.quit()    
                return
            if handle_event(dogadjaj):
                treba_crtati = True
        if treba_crtati:
            draw()
            pg.display.update()
