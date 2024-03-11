# Projektfeladat
def mpbe(bemenet:list) -> int:
    return bemenet[2] + bemenet[1]*60 + bemenet[0]*60*60
#változók létrehozása
nyersadatok = []

#2. feladat
with open("hivas.txt","rt",encoding="utf-8") as bemenet:
    for sor in bemenet:
        sor = sor.strip().split()
        nyersadatok.append(sor)
