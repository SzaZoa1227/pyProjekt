import pygame
import random
import sys
import os
def dobokocka(ablakMeret):
    os.system('cls' if os.name == 'nt' else 'clear') #oprendszer alapján cleareli le a cli-t
    pygame.init()

    FEHER = (255, 255, 255)
    FEKETE = (0, 0, 0)

    ablak = pygame.display.set_mode((ablakMeret, ablakMeret))
    pygame.display.set_caption("Dobókocka")

    pottySugar = ablakMeret/20
    pottyKoordinatak = {            #dictionaryben a kocka értéke baloldalt és hozzátartozó kirajzolandó pöttyök koordinátája
        1: [(ablakMeret/2, ablakMeret/2)],
        2: [(ablakMeret/4, ablakMeret/4), (ablakMeret*3/4, ablakMeret*3/4)],
        3: [(ablakMeret/4, ablakMeret/4), (ablakMeret/2, ablakMeret/2), (ablakMeret*3/4, ablakMeret*3/4)],
        4: [(ablakMeret/4, ablakMeret/4), (ablakMeret/4, ablakMeret*3/4), (ablakMeret*3/4, ablakMeret/4), (ablakMeret*3/4, ablakMeret*3/4)],
        5: [(ablakMeret/4, ablakMeret/4), (ablakMeret/4, ablakMeret*3/4), (ablakMeret/2, ablakMeret/2), (ablakMeret*3/4, ablakMeret/4), (ablakMeret*3/4, ablakMeret*3/4)],
        6: [(ablakMeret/4, ablakMeret/4), (ablakMeret/4, ablakMeret/2), (ablakMeret/4, ablakMeret*3/4), (ablakMeret*3/4, ablakMeret/4), (ablakMeret*3/4, ablakMeret/2), (ablakMeret*3/4, ablakMeret*3/4)]
    }
    dobasSzam = 0
    kockaErtek = None
    stilus = pygame.font.Font(None, 24) #font({betustilus}, {betumeret})
    szoveg = stilus.render('Nyomd meg a szóközt egy dobáshoz, vagy a "q"-t hogy kilépj', True, FEKETE) #render({szoveg}, {antialiasing (boolean)}, {szin})
    fut = True
    while fut:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #ha x-et nyomsz az ablakon akkor is kilép
                fut = False
            if event.type == pygame.KEYDOWN: #ha egy event tipusa billentyuzet lenyomas
                if event.key == pygame.K_SPACE: #ha ez az event szokoz lenyomas
                    dobasSzam += 1
                    kockaErtek = random.randint(1, 6)
                elif event.key == pygame.K_q: #ha ez az event q betu lenyomasa
                    fut = False

        ablak.fill(FEHER)
        dobasErtekSzoveg = stilus.render(f"Kockád értéke:{kockaErtek}",True,FEKETE)
        dobasSzamSzoveg = stilus.render(f"Dobásaid száma:{dobasSzam}",True,FEKETE)

        if kockaErtek is not None:
            for pottyHelye in pottyKoordinatak[kockaErtek]:
                pygame.draw.circle(ablak, FEKETE, pottyHelye, pottySugar)
                ablak.blit(dobasSzamSzoveg,(50,10))
                ablak.blit(dobasErtekSzoveg, (50,30))
        else:
            ablak.blit(szoveg, (50, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()
