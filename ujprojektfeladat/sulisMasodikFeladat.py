from random import randint
import os
n  = 0
m = 0
matrix = []
while 3 > n or n > 10:
    os.system("cls")
    try: n = int(input("Add meg a mátrix első dimenzióját! (3-10)"))
    except ValueError: 
        print("Számot adj meg!")
        input("Nyomj entert a továbblépéshez.")
        continue
    if n > 10 or n < 3:
        print("A szám 3-10 lehet!")
        input("Nyomj entert a továbblépéshez.")

while 3 > m or m > 10:
    os.system("cls")
    print(f"A mátrix első dimenziója: {n}")
    try: m = int(input("Add meg a mátrix második dimenzióját! Figyelj, nem lehet ugyan az az érték mint az első. (3-10)"))
    except ValueError: 
        print("Számot adj meg!") 
        input("Nyomj entert a továbblépéshez.")
    if m == n:
        print("Nem lehet ugyan az a két érték!")
        m = 0
        input("Nyomj entert a továbblépéshez.")


for i in range(n):
    temp = []
    for j in range(m):
        temp.append(randint(0,10))
    matrix.append(temp)

print(matrix)