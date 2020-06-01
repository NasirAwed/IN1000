fil = open("tempratur.txt","r")
liste = []
for x in fil:
    #Fjerner whitespace
    x.strip()
    #konverterer til int
    liste.append(int(x))

print(liste[0])
#regner ut gjennomsnitt
def gjennomsnitt(lst):
    return sum(lst) / len(lst)

print("gjennomsnitt= ", gjennomsnitt(liste))
