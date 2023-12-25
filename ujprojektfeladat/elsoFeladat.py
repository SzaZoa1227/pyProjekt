from random import randint

lista = [randint(-20, 50) for _ in range(25)]


def minimum(lista):
    a = lista[0]
    index = 0
    for i in range(1, len(lista)):
        if a > lista[i]:
            index = i
    return index


def maximum(lista):
    a = lista[0]
    index = 0
    for i in range(1, len(lista)):
        if a < lista[i]:
            index = i
    return index


def SzomszedoSzamKulonbseg(lista):
    legnagyobbKulonbseg = (lista[0], lista[1])
    for i in range(1, len(lista)-1):
        if lista[i] - lista[i+1] > legnagyobbKulonbseg[0] - legnagyobbKulonbseg[1]:
            legnagyobbKulonbseg = (lista[i], lista[i+1])
    return legnagyobbKulonbseg


print(lista)
print(
    f"\nA legkissebb szám a listában: {lista[minimum(lista)]}\nIndexe: {minimum(lista)}")
print(
    f"\nA legnagyobb szám a listában: {lista[maximum(lista)]}\nIndexe: {maximum(lista)}")
print("\nA nulla megtalálható a listában" if 0 in lista else "\nA nulla nem található meg a listában")
print(
    f"A legnagyobb különbség két szomszédos elem közt: {SzomszedoSzamKulonbseg(lista)}")
