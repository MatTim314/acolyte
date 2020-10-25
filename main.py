import pygame
import time
import random
from collections import deque

def load_files():
    try:
        orbs = [pygame.image.load('pictures/'+i) for i in [ 'quas_orb.png', 'wex_orb.png', 'exort_orb.png']]
        background = pygame.image.load("pictures/background_invoker.png")
        images_raw = 'ala', 'cs', 'iw', 'fs', 'ss', 'chm', \
                 'db', 'emp', 'gw', 'tor', 'quas', 'exort', 'wex'
        images = [pygame.image.load('pictures/' + i + ".png") for i in images_raw]

        img_dic = {}
        for i in range(len(images)-3):
            img_dic[images_raw[i]] = images[i]
        strt_btn = pygame.image.load("pictures/strt_btn.png")
        strt_btn_prssd = pygame.image.load("pictures/strt_btn_prssd.png")
        return images, background, img_dic, images_raw, strt_btn, strt_btn_prssd, orbs
    except pygame.error:
        print("Images were not able to load.")
        exit()

def game_loop(win, background, img_dic, images_raw, orbs):
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    for i in range(3):
        pygame.draw.circle(win, (169, 169, 169), (i * 100+460+50, 400+50), 50, 1)
    orbs_queue = deque()
    orbs_dic = {'Q': orbs[0], 'W': orbs[1], 'E': orbs[2]}
    spells_dic = {'QQQ': "cs", 'WWW': "emp", 'EEE': "ss",
                  'QQW': "gw", 'QWQ': "gw", 'WQQ': "gw",
                  'QQE': "iw", 'QEQ': "iw", 'EQQ': "iw",
                  'QWW': "tor", 'WWQ': "tor", 'WQW': "tor",
                  'QWE': "db", 'QEW': "db", 'WQE': "db",
                  'WEQ': "db", 'EQW': "db", 'EWQ': "db",
                  'QEE': "fs", 'EQE': "fs", 'EEQ': "fs",
                  'WWE': "ala", 'WEW': "ala", 'EWW': "ala",
                  'WEE': "chm", 'EWE': "chm", 'EEW': "chm"}

    answered = True
    key = None
    changed = False
    last = None

    while True:

        if answered:
            spells = images_raw[:len(images_raw) - 3]
            key = random.choice(spells)
            while key == last:
                key = random.choice(spells)
            last = key
            win.blit(img_dic[key], (550, 550))
            answered = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    orb_str = "".join(list(orbs_queue))
                    if spells_dic[orb_str] == key and len(orb_str) >= 3:
                        answered = True
                    # win.blit(img_dic[spells_dic["".join(list(orbs_queue))]], (550 ,600))
                elif event.key == pygame.K_w:
                    orbs_queue.append('W')
                elif event.key == pygame.K_e:
                    orbs_queue.append('E')
                elif event.key == pygame.K_q:
                    orbs_queue.append('Q')

            if len(orbs_queue) > 3:
                orbs_queue.popleft()
                changed = True

        if changed or len(orbs_queue) <= 3:
            changed = False
            for i in range(len(orbs_queue)):
                win.blit(orbs_dic[orbs_queue[i]], (i * 100+460, 400))
            pygame.display.update()


def setup(win, background, images):
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    for i in range(len(images)):
        win.blit(images[i], (-30 + i * 100, 370))


def main():
    images, background, img_dic, images_raw, strt_btn, strt_btn_prssd, orbs = load_files()
    pygame.init()
    pygame.display.set_caption("Acolyte")
    pygame.display.set_icon(random.choice(images))
    width, height = 1240, 800
    offset = 160
    pygame.display.set_mode((width, height))
    win = pygame.display.get_surface()

    setup(win, background, images)

    run = True
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
                game_loop(win, background, img_dic, images_raw, orbs)
                setup(win, background, images)
        else:
            win.blit(strt_btn, (play_btn_pos[0] - offset, play_btn_pos[1]))

        time.sleep(0.05)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
