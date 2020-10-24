import pygame
import time
import random
from collections import deque


def game_loop(win, background, img_dic):
    win.fill((0, 0, 0))
    win.blit(background, (-100, 0))

    orbs = [pygame.image.load('pictures/'+i) for i in [ 'quas_orb.png', 'wex_orb.png', 'exort_orb.png']]
    orbs_queue = deque()
    orbs_dic = {'Q': orbs[0], 'W': orbs[1], 'E': orbs[2]}
    spells_dic = {'QQQ': "cs", 'QQW': "gw", 'QQE': "iw",
                  'QWQ': "gw", 'QWW': "tor", 'QWE': "db",
                  'QEQ': "iw", 'QEW': "db", 'QEE': "fs",
                  'WQQ': "gw", 'WQW': "tor", 'WQE': "db",
                  'WWQ': "tor", 'WWW': "emp", 'WWE': "ala",
                  'WEQ': "db", 'WEW': "ala", 'WEE': "chm",
                  'EQQ': "iw", 'EQW': "db", 'EQE': "fs",
                  'EWQ': "db", 'EWW': "ala", 'EWE': "chm",
                  'EEQ': "fs", 'EEW': "chm", 'EEE': "ss"}
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and len("".join(list(orbs_queue))) >= 3:
                    win.blit(img_dic[spells_dic["".join(list(orbs_queue))]], (550 ,600))
                elif event.key == pygame.K_w:
                    orbs_queue.append('W')
                elif event.key == pygame.K_e:
                    orbs_queue.append('E')
                elif event.key == pygame.K_q:
                    orbs_queue.append('Q')

            if len(orbs_queue) > 3:
                orbs_queue.popleft()
        for i in range(len(orbs_queue)):
            win.blit(orbs_dic[orbs_queue[i]], (i * 100+460, 450))
        pass
        pygame.display.update()
    pass


def setup(win, background, images):
    win.fill((0, 0, 0))
    win.blit(background, (-100, 0))
    for i in range(len(images)):
        win.blit(images[i], (-30 + i * 100, 370))


def main():
    pygame.init()

    width, height = 1240, 800
    pygame.display.set_mode((width, height))

    run = True
    offset = 160

    background = pygame.image.load("pictures/background_invoker.png")
    images_raw = 'ala.png', 'cs.png', 'iw.png', 'fs.png', 'ss.png', 'chm.png', \
             'db.png', 'emp.png', 'gw.png', 'tor.png', 'quas.png', 'exort.png', 'wex.png'
    images = [pygame.image.load('pictures/' + i) for i in images_raw]
    img_dic = {}
    for i in range(len(images)-3):
        img_dic[images_raw[i].split('.')[0]] = images[i]
    strt_btn = pygame.image.load("pictures/strt_btn.png")
    strt_btn_prssd = pygame.image.load("pictures/strt_btn_prssd.png")

    win = pygame.display.get_surface()

    setup(win, background, images)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        play_btn_pos = (620, 560)

        # if cursor is on the play button
        if play_btn_pos[0] + offset > mouse[0] > play_btn_pos[0] - offset \
           and play_btn_pos[1] + offset * 2 > mouse[1] > play_btn_pos[1]:
            win.blit(strt_btn_prssd, (play_btn_pos[0] - offset, play_btn_pos[1]))
            if click[0] == 1:
                game_loop(win, background, img_dic)
                setup(win, background, images)
        else:
            win.blit(strt_btn, (play_btn_pos[0] - offset, play_btn_pos[1]))

        time.sleep(0.05)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
