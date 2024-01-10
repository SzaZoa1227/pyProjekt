from random import randint
from IPython.display import clear_output

def input_ellenorzes(szoveg):
    while True:
        try:
            bevitel = int(input(szoveg))
            if 3 <= bevitel <= 10:
                return bevitel
            else:
                print(f"A megadott értéknek 3-10 között kell lennie.")
        except ValueError:
            print("Számot adj meg!")

def parosok_szazaleka(n, m, parosok_szama):
    minden_elem = n * m
    szazalek = parosok_szama / minden_elem * 100
    return szazalek

def transzponalt(matrix):
    sorok_szama = len(matrix)
    oszlopok_szama = len(matrix[0])
    transzponaltMatrix = []
    for oszlop in range(oszlopok_szama):
        ideiglenes_sor = []
        ideiglenes_sor[::-1]
        for sor in range(sorok_szama):
            ideiglenes_sor.append(matrix[sor][oszlop])
        transzponaltMatrix.append(ideiglenes_sor)
    return transzponaltMatrix
n = 0
m = 0

while not (3 <= n <= 10):
    clear_output(wait=True)
    n = input_ellenorzes("Add meg az első dimenzióját a mátrixnak! 3-10")

while not (3 <= m <= 10 and m != n):
    clear_output(wait=True)
    print(f"Az első dimenziója a mátrixnak: {n}")
    m = input_ellenorzes(f"Add meg a második dimenzióját a mátrixnak! Figyelj, nem lehet {n}! 3-10")

elemek_osszege = 0
parosok_szama = 0
matrix = []

for i in range(n):
    sor = []
    for j in range(m):
        elem = randint(0, 10)
        sor.append(elem)
        elemek_osszege += elem
        if elem % 2 == 0:
            parosok_szama+= 1
    matrix.append(sor)

paros_szazalek = parosok_szazaleka(n, m, parosok_szama)
ujmatrix = transzponalt(matrix)
for sor in matrix:
    print(sor)

print(f"A mátrix elemeinek összege: {elemek_osszege}")
print(f"A páros elemek száma a mátrixban: {parosok_szama}, {paros_szazalek}%-a az összes elemnek.")
print("Az eredeti mátrix:")
for i in range(len(matrix)):
    print(matrix[i])

print("A transzponáltja:")
for i in range(len(ujmatrix)):
    print(ujmatrix[i])