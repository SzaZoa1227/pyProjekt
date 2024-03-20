def mpbe(bemenet: list) -> int:
    return bemenet[2] + bemenet[1]*60 + bemenet[0]*60*60
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
kezdetek = []
vegek = []
for adat in nyersadatok:
    kezdetek.append([adat[0],adat[1],adat[2]])
    vegek.append([adat[3],adat[4],adat[5]])