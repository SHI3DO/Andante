def draw(screen, pg, screenx, screeny):
    upbar = pg.Surface((screenx, screeny/12))
    upbar.set_alpha(100)
    upbar.fill((0,0,0))
    screen.blit(upbar, (0, 0))