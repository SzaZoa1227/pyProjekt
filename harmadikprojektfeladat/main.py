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


def rendesbe(masodpercbenIdopont: int) -> list:
    ora = masodpercbenIdopont//3600
    maradek = masodpercbenIdopont % 3600
    perc = maradek//60
    mp = maradek % 60
    return [ora, perc, mp]


def legh(hivasokhossza: list) -> int:
    legh = 0
    for i in range(1, len(hivasokhossza)):
        if hivasokhossza[legh] < hivasokhossza[i]:
            legh = i
    return hivasokhossza[legh], legh


nyersadatok: list = []
hivasokhossza: list = []
bejovohivasok: dict = {}
munkaidonBelul: list = []
munkaidobenHossz: list = []
with open("hivas.txt", "rt", encoding="utf-8") as bemenet:
    for sor in bemenet:
        sor = sor.strip().split()
        for i in range(len(sor)):
            sor[i] = int(sor[i])
        nyersadatok.append(sor)
    bemenet.close()
for adat in nyersadatok:
    if adat[0] not in bejovohivasok.keys():
        bejovohivasok[adat[0]] = 1
    else:
        bejovohivasok[adat[0]] += 1
print("\nHarmadik feladat:\n")
for ido, hivasok in bejovohivasok.items():
    print(f"{ido} óra: {hivasok} hívás")
for adat in nyersadatok:
    tol = [adat[0], adat[1], adat[2]]
    ig = [adat[3], adat[4], adat[5]]
    hossz = mpbe(ig) - mpbe(tol)
    hivasokhossza.append(hossz)
print("\nNégyes feladat:\n")
print(
    f"{legh(hivasokhossza)[0]} másodpercig tartott a leghosszabb hívás, melynek sorszáma: {legh(hivasokhossza)[1]+1}")
for i in range(len(nyersadatok)):
    if nyersadatok[i][0] >= 8 and nyersadatok[i][0] < 12:
        munkaidonBelul.append((nyersadatok[i], i))
for adat in munkaidonBelul:
    tol = [adat[0][0], adat[0][1], adat[0][2]]
    ig = [adat[0][3], adat[0][4], adat[0][5]]
    hossz = mpbe(ig) - mpbe(tol)
    munkaidobenHossz.append(hossz)
print("\nÖtös feladat:\n")
inputOra: int = bekeres("Adj meg egy munkaidőn belüli órát! ",
                        8, 12, "Munkaidőn belüli órát adj meg!")
inputPerc: int = bekeres("Adj meg az órához egy perc értéket! ",
                         0, 59, "0-59 közötti értéket adj meg!")
inputMp: int = bekeres("Adj meg az órához és a perchez egy másodperc értéket! ",
                       0, 59, "0-59 közötti értéket adj meg!")
inputido: int = mpbe([inputOra, inputPerc, inputMp])
inputido2: list = [inputOra, inputPerc, inputMp]
print(f"A választott időpontod: {inputOra}:{inputPerc}:{inputMp}")
valasztottHivasokKorul = []
for i in range(len(nyersadatok)):
    kezdet: list = [nyersadatok[i][0], nyersadatok[i][1], nyersadatok[i][2]]
    veg: list = [nyersadatok[i][3], nyersadatok[i][4], nyersadatok[i][5]]
    kezdet: int = mpbe(kezdet)
    veg: int = mpbe(veg)
    if kezdet < inputido < veg:
        valasztottHivasokKorul.append((nyersadatok[i], i))
print(
    f"A megadott időpontban: {inputOra}:{inputPerc}:{inputMp} {valasztottHivasokKorul[1][1]}. sorszámú telefonáló volt vonalban, ekkkor várt: {len(valasztottHivasokKorul)-1} telefonáló.")
print("nincs hatos feladat")
with open("sikeres.txt", "wt", encoding="utf-8") as ki:
    for i in range(len(munkaidonBelul)):
        szoveg: str = f"{i+1} {munkaidonBelul[i][0][0]} {munkaidonBelul[i][0][1]} {munkaidonBelul[i][0][2]} \
            {munkaidonBelul[i][0][3]} {munkaidonBelul[i][0][4]} {munkaidonBelul[i][0][5]}\n"
        ki.write(szoveg)
