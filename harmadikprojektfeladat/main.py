# Projektfeladat
def mpbe(bemenet:list) -> int:
    return bemenet[2] + bemenet[1]*60 + bemenet[0]*60*60
#változók létrehozása
nyersadatok = []
bejovohivasok = {}
#2. feladat
with open("hivas.txt","rt",encoding="utf-8") as bemenet:
    for sor in bemenet:
        sor = sor.strip().split()
        nyersadatok.append(sor)

#3. feladat
for adat in nyersadatok:
    if adat[0] not in bejovohivasok.keys():
        bejovohivasok[adat[0]] = 1
    else: bejovohivasok[adat[0]] += 1
print("Harmadik feladat:")
for ido, hivasok in bejovohivasok.items():
    print(f"{ido} óra: {hivasok} hívás")
    