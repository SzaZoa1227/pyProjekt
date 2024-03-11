# Projektfeladat
def bekeres(rizsa: str, minimum: int, maximum: int, hiba: str) -> int:
    while True:
        try:
            bemenet = int(input(rizsa))
            if bemenet < minimum or bemenet > maximum:
                raise ValueError(hiba)
            return bemenet
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print("Valami hiba történt:", e)


def mpbe(bemenet: list) -> int:
    return bemenet[2] + bemenet[1]*60 + bemenet[0]*60*60


def legk(hivasokhossza: list) -> int:
    legrovidebb = 0
    for i in range(1, len(hivasokhossza)):
        if hivasokhossza[legrovidebb] > hivasokhossza[i]:
            legrovidebb = i
    return hivasokhossza[legrovidebb], legrovidebb


# változók létrehozása
nyersadatok = []
hivasokhossza = []
bejovohivasok = {}
munkaidonBelul = []
munkaidobenHossz = []
# 2. feladat
with open("hivas.txt", "rt", encoding="utf-8") as bemenet:
    for sor in bemenet:
        sor = sor.strip().split()
        for i in range(len(sor)):
            sor[i] = int(sor[i])
        nyersadatok.append(sor)
# 3. feladat
for adat in nyersadatok:
    if adat[0] not in bejovohivasok.keys():
        bejovohivasok[adat[0]] = 1
    else:
        bejovohivasok[adat[0]] += 1
print("\nHarmadik feladat:\n")
for ido, hivasok in bejovohivasok.items():
    print(f"{ido} óra: {hivasok} hívás")
# 4. feladat
for adat in nyersadatok:
    tol = [adat[0], adat[1], adat[2]]
    ig = [adat[3], adat[4], adat[5]]
    hossz = mpbe(ig) - mpbe(tol)
    hivasokhossza.append(hossz)
print("\nNégyes feladat:\n")
print(
    f"{legk(hivasokhossza)[0]} másodpercig tartott a legröbvidebb hívás, melynek sorszáma: {legk(hivasokhossza)[1]+1}")
# 5. feladat
for adat in nyersadatok:
    if adat[0] >= 8 and adat[0] < 12:
        munkaidonBelul.append(adat)
for adat in munkaidonBelul:
    tol = [adat[0], adat[1], adat[2]]
    ig = [adat[3], adat[4], adat[5]]
    hossz = mpbe(ig) - mpbe(tol)
    munkaidobenHossz.append(hossz)
print("\nÖtös feladat:\n")
inputOra = bekeres("Adj meg egy munkaidőn belüli órát! ",
                   8, 12, "Munkaidőn belüli órát adj meg!")
inputPerc = bekeres("Adj meg az órához egy perc értéket! ",
                    0, 59, "0-59 közötti értéket adj meg!")
inputMp = bekeres("Adj meg az órához és a perchez egy másodperc értéket! ",
                  0, 59, "0-59 közötti értéket adj meg!")
print(f"A választott időpontod: {inputOra}:{inputPerc}:{inputMp}")
