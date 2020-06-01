# Et program for å legge tall i en liste og gjøre forskjellige oprasjoner på dem
T=True
liste = []
while T:
    tall= int(input("Tast inn et tall (0 for å avslutte): "))
    if tall == 0:
        T = False
    else:
        liste.append(tall)

for i in liste:
    print(i)

minsum=0
for x in liste:
    minsum = minsum + x

print("summen av tall = ", minsum)

mintall=liste[0]
maxtall=liste[0]

for y in liste:
    if mintall > y:
        mintall = y

for r in liste:
    if maxtall < r:
        maxtall = r

print("minste tall =", mintall, "max verdi = ", maxtall)
