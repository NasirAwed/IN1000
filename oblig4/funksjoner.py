

#Funksjon for addisjon
def adder(tall1, tall2):
    tall3 = tall1 + tall2
    return tall3

print("4+5=", adder(4,5))
print("3+6=", adder(3,6))


tekst = input("Tast inn en streng: ")

bokstav = input("Tast in en bokstav: ")
teller = 0
#Loop som teller antall ord
for x in tekst:
    if bokstav == x:
        teller+=1

print("Bokstaven"+" "+bokstav+" "+"forekommer ", teller,"ganger")

#Teller hvor mye en bokstav forekommer i en streng  
def tellForekomst(minTekst, minBokstav):
    teller = 0
    for x in minTekst:
        if minBokstav == x:
            teller+=1
    print("Bokstaven"+" "+minBokstav+" "+"forekommer ", teller,"ganger")

tekst = input("Tast inn en streng: ")
bokstav = input("Tast in en bokstav: ")

tellForekomst(tekst,bokstav)
