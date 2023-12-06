from random import randint

lista = [randint(-20,50) for _ in range(25)]

def minimum(lista):
    a = lista[0]
    for i in range(1,len(lista)):
        if a > lista[i]:
            index = i
    return index

def maximum(lista):
    a = lista[0]
    index = 0
    for i in range(1,len(lista)):
        if a < lista[i]:
            index = i
    return index

#minkereses,maxkereses, indexuk
print(lista)
print(f"\nA legkissebb szám a listában: {lista[minimum(lista)]}\nIndexe: {minimum(lista)}")
print(f"\nA legnagyobb szám a listában: {lista[maximum(lista)]}\nIndexe: {maximum(lista)}")
