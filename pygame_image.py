import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ex01/fig/3.png") #練習2
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 5, 1.0), pg.transform.rotozoom(kk_img, 10, 1.0)] #練習3
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-(tmr%3200)*5, 0]) #練習4
        screen.blit(bg_img2, [1600-(tmr%3200)*5, 0])#練習6
        screen.blit(bg_img, [3200-(tmr%3200)*5, 0])
        screen.blit(bg_img2, [4800-(tmr%3200)*5, 0])
        screen.blit(kk_imgs[tmr%3], [300, 200-10*(tmr%3)]) #練習5
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()