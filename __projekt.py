import os
import math
from random import randint
import threading
from dobokocka import dobokocka


def pit():  # pitagorasz tetel alkalmazasa
    rossz = True
    while rossz:
        try:
            a = float(input("\nAdd meg az egyik befogó hosszát!\t"))
            rossz = False
        except ValueError:
            print("\nSzámot adj meg!")
            input("\nÜss egy entert ha továbbmehetünk!\t")
    rossz = True
    while rossz:
        try:
            b = float(input("\nAdd meg a második befogó hosszát!\t"))
            rossz = False
        except ValueError:
            print("\nSzámot adj meg!")
            input("\nÜss egy entert ha továbbmehetünk!\t")
    print(f"{math.sqrt(a**2+b**2)} az átfogó hossza")
    input("\nÜss egy entert ha továbbmehetünk!\t")


def negyzet():  # negyzetre emeles
    rossz = True
    while rossz:
        try:
            hatvanyalap = float(input("\nAdd meg a hatványalapot!\t"))
            rossz = False
        except ValueError:
            print("\nSzámot adj meg!")
            input("\nÜss egy entert ha továbbmehetünk!\t")
    print(hatvanyalap**2)
    input("\nÜss egy entert ha továbbmehetünk!\t")


def alapmuveletek():  # alapmuveletek elvegzese
    rossz = True
    while rossz:
        try:
            a = float(input("\nAdd meg az első számot:  "))
            rossz = False
        except ValueError:
            print("\nSzámot adj meg!")
            input("\nÜss egy entert ha továbbmehetünk!\t")
    rossz = True
    while rossz:
        try:
            b = float(input("\nAdd meg a második számot:  "))
            rossz = False
        except ValueError:
            print("\nSzámot adj meg!")
            input("\nÜss egy entert ha továbbmehetünk!\t")
    osszeg = a + b
    kulonbseg = a - b
    szorzat = a * b
    hanyados = a / b
    print(
        f"\nÖsszegük: {osszeg}\nKülönbségük: {kulonbseg}\nSzorzatuk: {szorzat}\nHányadosuk: {hanyados}")
    input("\nÜss egy entert ha továbbmehetünk!\t")


def randomSzamok():  # random szamok generalasa
    # for loop a 10 random szam generalasara
    szamok = [randint(-500, 500) for _ in range(10)]
    print(f"\nA generált számok: {szamok}")
    print(f"Ezek közül a legkissebb: {min(szamok)}")
    input("\nÜss egy entert ha továbbmehetünk!\t")


def dobokockaFx():
    ablakMeret = int(input("Kérlek adj meg egy ablakméretet!    "))
    thread = threading.Thread(target=dobokocka, args=(ablakMeret,))
    thread.start()
    thread.join()


def main():
    funkciok = {1: alapmuveletek,
                2: negyzet,
                3: pit,
                4: dobokockaFx,
                5: randomSzamok}
    megy = True
    while megy:
        # mivel linuxon dolgozom, nekem is kell, hogy mukodjon a clear
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Az irányítások\n0: Kilépés a programból\n1: Négy alapművelet\n2: Megadott szám négyzete\n3: Pitagorasz tétel alkalmazása\n4: Dobókocka\n5: 10 véletlen szám generálása -500 és 500, legkissebb kiválasztása")
        rossz = True
        while rossz:
            try:
                kezdes = int(input("\nVálaszd ki mit szeretnél csinálni!:\t"))
                rossz = False
            except ValueError:
                print("\nA megadott lehetőségek közül válassz!")
                input("\nÜss egy entert ha továbbmehetünk!\t")
        if kezdes == 0:
            megy = False
        elif kezdes in funkciok:
            fuggveny = funkciok[kezdes]
            fuggveny()
        else:
            print("\nA megadott lehetőségek közül válassz!")
            input("\nÜss egy entert ha továbbmehetünk!\t")


if __name__ == "__main__":
    main()
