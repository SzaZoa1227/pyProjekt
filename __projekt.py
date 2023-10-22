import os
import math
megyaprogram = True
def pit():
    a = float(input("Add meg az egyik befogó hosszát!   "))
    b = float(input("Add meg a másik befogó hosszát!   "))
    print(f"{math.sqrt(a**2+b**2)} az átfogó hossza")
    input()
    main()
def negyzet():
    hatvanyalap = int(input("Add meg a hatványalapot!   "))
    print(hatvanyalap**2)
    input()
    main()
def programleall():
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
    main()
def main():
    os.system("cls")
    print(f"Az irányítások\n0: Kilépés a programból\n1: Négy alapművelet\n2: Megadott szám négyzete")
    kezdes = int(input("Kérlek add meg a választott programot:  "))
    if kezdes == 0:
        programleall()
    if kezdes == 1:
        alapmuveletek()
    if kezdes == 2:
        negyzet()
    if kezdes == 3:
        pit()

main()