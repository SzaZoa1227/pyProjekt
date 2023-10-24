import os
import math
from dobokocka import dobokocka
import threading
from random import randint
megyaprogram = True

def pit():
    nemjo = 1
    while nemjo:
        try:
            a = float(input("\nAdd meg az egyik befogó hosszát!   "))
            nemjo = 0
        except ValueError:
            print("Számot adj meg!")
    nemjo = 1
    while nemjo:
        try:
            b = float(input("Add meg a másik befogó hosszát!   "))
            nemjo = 0
        except ValueError:
            print("Számot adj meg!")
    print(f"{math.sqrt(a**2+b**2)} az átfogó hossza")
    input("\nÜss egy entert ha továbbmehetünk!\t")

def negyzet():
    nemjo = 1
    while nemjo:
        try:
            hatvanyalap = float(input("\nAdd meg a hatványalapot!   "))
        except ValueError:
            print("Számot adj meg!")
    print(hatvanyalap**2)
    input("\nÜss egy entert ha továbbmehetünk!\t")

def programleall():
    global megyaprogram
    megyaprogram = False

def alapmuveletek():
    nemjo = 1
    while nemjo:
        try:
            a = float(input("\nAdd meg az első számot amivel elvégezzük a műveleteket:  "))
            nemjo = 0
        except ValueError:
            print("Számot adj meg!")
    nemjo = 1
    while nemjo:
        try:
            b = int(input("Add meg a második számot amivel elvégezzük a műveleteket:    "))
            nemjo = 0
        except ValueError:
            print("Számot adj meg!")
    osszeg = a+b
    kulonbseg = a-b
    szorzat = a*b
    hanyados = a/b
    print(f"\nÖsszegük: {osszeg}\nKülönbségük: {kulonbseg}\nSzorzatuk: {szorzat}\nHányadosuk: {hanyados}")
    input("\nÜss egy entert ha továbbmehetünk!\t")
def randomSzamok():
    szamok = []
    for i in range(10):
        szamok.append(randint(-500,500))
    print(f"\nA generált számok: {szamok}")
    print(f"Ezek közül a legkissebb: {min(szamok)}")
    input("\nÜss egy entert ha továbbmehetünk!\t")
def main():
    while megyaprogram:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Az irányítások\n0: Kilépés a programból\n1: Négy alapművelet\n2: Megadott szám négyzete\n3: Pitagorasz tétel alkalmazása\n4: Dobókocka\n5: 10 véletlen szám generálása -500 és 500, legkissebb kiválasztása")
        nemjo = 1
        while nemjo:
            try:
                kezdes = int(input("Kérlek add meg a választott programot:  "))
                nemjo = 0
            except ValueError:
                print("A felsorolt lehetőségekből válassz!")
        if kezdes == 0:
            programleall()
        if kezdes == 1:
            alapmuveletek()
        if kezdes == 2:
            negyzet()
        if kezdes == 3:
            pit()
        if kezdes == 4:
            nemjo = True
            while nemjo:
                try:
                    ablakMeret = int(input("Kérlek adj meg egy ablakméretet!    "))
                    nemjo = False
                except ValueError:
                    print("Egész számot adj meg!")
            thread = threading.Thread(target=dobokocka, args=(ablakMeret,)) #NEM TUDJA KEZELNI HA SÍMÁN INT ÉRTÉKET ADOK NEKI, LISTA KELL VAGY TUPLE MI EZ AFÉDJÉFKLJADSFÉLJDASÉFLKDJAFÉLKADSFJÉLKDSAFJÉADS
            thread.start()
            thread.join()
        if kezdes == 5:
            randomSzamok()

if __name__ == "__main__": #ha a jelenleg futtatott script nem import akkor folytatja míg 0-t nem nyomunk
    megyaprogram = True
    main()
