
#Et program som lager en reiseplanlegger ved hjelp av lister
steder = []
klesplagg = []
avreisedato = []
tall = 5
while tall !=0:
    sted = input("Tast inn en destinasjon: ")
    steder.append(sted)
    plagg = input(" og et klessplagg: ")
    klesplagg.append(plagg)
    dato = input("dato for avreise: ")
    avreisedato.append(dato)
    tall=tall-1
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedato)

for i in reiseplan:
    print(i)

plass = input("Tast in en indeks: ")
plass2 = input("Engang til: ")

if plass.isdigit() and plass2.isdigit():
    if plass == 0 and plass <= 4 and plass2 == 0 and plass2 <= 4:
        liste = reiseplan[plass]
        print(liste[plass2])

else:
    print("ugyldig input")
