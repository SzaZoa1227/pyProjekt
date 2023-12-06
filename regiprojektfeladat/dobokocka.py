import pygame
import random
import sys
import os


def dobokocka(ablakMeret):
    # oprendszer alapján cleareli le a cli-t
    os.system('cls' if os.name == 'nt' else 'clear')
    pygame.init()

    FEHER = (255, 255, 255)
    FEKETE = (0, 0, 0)
    ablak = pygame.display.set_mode((ablakMeret, ablakMeret))
    pygame.display.set_caption("Dobókocka")
    pottySugar = ablakMeret/20
    dobasSzam = 0
    kockaErtek = None

    pottyKoordinatak = {  # dictionaryben a kocka értéke baloldalt és hozzátartozó kirajzolandó pöttyök koordinátája
        1: [(ablakMeret/2, ablakMeret/2)],
        2: [(ablakMeret/4, ablakMeret/4), (ablakMeret*3/4, ablakMeret*3/4)],
        3: [(ablakMeret/4, ablakMeret/4), (ablakMeret/2, ablakMeret/2), (ablakMeret*3/4, ablakMeret*3/4)],
        4: [(ablakMeret/4, ablakMeret/4), (ablakMeret/4, ablakMeret*3/4), (ablakMeret*3/4, ablakMeret/4), (ablakMeret*3/4, ablakMeret*3/4)],
        5: [(ablakMeret/4, ablakMeret/4), (ablakMeret/4, ablakMeret*3/4), (ablakMeret/2, ablakMeret/2), (ablakMeret*3/4, ablakMeret/4), (ablakMeret*3/4, ablakMeret*3/4)],
        6: [(ablakMeret/4, ablakMeret/4), (ablakMeret/4, ablakMeret/2), (ablakMeret/4, ablakMeret*3/4), (ablakMeret*3/4, ablakMeret/4), (ablakMeret*3/4, ablakMeret/2), (ablakMeret*3/4, ablakMeret*3/4)]
    }

    stilus = pygame.font.Font(None, 24)  # font({betustilus}, {betumeret})
    # render({szoveg}, {antialiasing (boolean)}, {szin})
    szoveg = stilus.render(
        'Nyomd meg a szóközt egy dobáshoz, vagy a "q"-t hogy kilépj', True, FEKETE)
    dobasErtekek = []
    fut = True
    while fut:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ha x-et nyomsz az ablakon akkor is kilép
                fut = False
            if event.type == pygame.KEYDOWN:  # ha egy event tipusa billentyuzet lenyomas
                if event.key == pygame.K_SPACE:  # ha ez az event szokoz lenyomas
                    dobasSzam += 1
                    kockaErtek = random.randint(1, 6)
                    dobasErtekek.append(kockaErtek)
                elif event.key == pygame.K_q:  # ha ez az event q betu lenyomasa
                    fut = False
    
        ablak.fill(FEHER)
        dobasErtekSzoveg = stilus.render(
            f"Kockád értéke:    {kockaErtek}", True, FEKETE)
        dobasSzamSzoveg = stilus.render(
            f"Dobásaid száma:   {dobasSzam}", True, FEKETE)

        # ha van erteke a dobokockanak(dobott egyet a jatekos es a script generalt ezelott neki erteket, frissitse a kepet, a kocka erteke szerint)
        if kockaErtek is not None:
            ablak.blit(dobasSzamSzoveg, (50, 10))
            ablak.blit(dobasErtekSzoveg, (50, 30))
            for pottyHelye in pottyKoordinatak[kockaErtek]:
                pygame.draw.circle(ablak, FEKETE, pottyHelye, pottySugar)
        else:
            ablak.blit(szoveg, (50, 10))

        pygame.display.flip()
    kiiras(dobasErtekek,dobasSzam)
    pygame.quit()
    sys.exit()

def kiiras(val1,val2):
    osszeg = 0
    for i in val1:
        osszeg += i
    f = open("ertekek.txt","w")
    f.write(osszeg)
    f.close
