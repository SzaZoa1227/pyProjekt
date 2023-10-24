import os
import math
from dobokocka import dobokocka
import threading

megyaprogram = True

def pit():
    a = float(input("Add meg az egyik befogó hosszát!   "))
    b = float(input("Add meg a másik befogó hosszát!   "))
    print(f"{math.sqrt(a**2+b**2)} az átfogó hossza")
    input()

def negyzet():
    hatvanyalap = int(input("Add meg a hatványalapot!   "))
    print(hatvanyalap**2)
    input()

def programleall():
    global megyaprogram
    megyaprogram = False

def alapmuveletek():
    a = int(input("Add meg az első számot amivel elvégezzük a műveleteket:  "))
    b = int(input("Add meg a második számot amivel elvégezzük a műveleteket:    "))
    osszeg = a+b
    kulonbseg = a-b
    szorzat = a*b
    hanyados = a/b
    print(f"Összegük: {osszeg}\nKülönbségük: {kulonbseg}\nSzorzatuk: {szorzat}\nHányadosuk: {hanyados}")
    input()

def main():
    while megyaprogram:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Az irányítások\n0: Kilépés a programból\n1: Négy alapművelet\n2: Megadott szám négyzete\n3: Pitagorasz tétel alkalmazása\n4: Dobókocka")
        kezdes = int(input("Kérlek add meg a választott programot:  "))
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

if __name__ == "__main__": #ha a jelenleg futtatott script nem import akkor folytatja míg 0-t nem nyomunk
    megyaprogram = True
    main()
