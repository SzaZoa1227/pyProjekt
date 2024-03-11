# Projektfeladat
def mpbe(bemenet:list) -> int:
    return bemenet[2] + bemenet[1]*60 + bemenet[0]*60*60
def legk(hivasokhossza:list) -> int:
    legrovidebb = 0
    for i in range(1,len(hivasokhossza)):
        if hivasokhossza[legrovidebb] > hivasokhossza[i]: legrovidebb = i
    return hivasokhossza[legrovidebb]
#változók létrehozása
nyersadatok = []
hivasokhossza = []
bejovohivasok = {}
#2. feladat
with open("hivas.txt","rt",encoding="utf-8") as bemenet:
    for sor in bemenet:
        sor = sor.strip().split()
        for i in range(len(sor)):
            sor[i] = int(sor[i])
        nyersadatok.append(sor)
#3. feladat
for adat in nyersadatok:
    if adat[0] not in bejovohivasok.keys():
        bejovohivasok[adat[0]] = 1
    else: bejovohivasok[adat[0]] += 1
print("\nHarmadik feladat:\n")
for ido, hivasok in bejovohivasok.items():
    print(f"{ido} óra: {hivasok} hívás")
#4. feladat
for adat in nyersadatok:
    tol = [adat[0],adat[1],adat[2]]
    ig = [adat[3],adat[4],adat[5]]
    hossz = mpbe(ig) - mpbe(tol)
    hivasokhossza.append(hossz)
print("\nNégyes feladat:\n")
print(f"{legk(hivasokhossza)} másodpercig tartott a legröbvidebb hívás.")