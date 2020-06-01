#oppgave 1

liste = [1,2,3]
print(liste)
liste.append(4)
print(liste)
liste2=[]
print("Skriv inn 4 navn: ")
teller=0

#Lager en loop for input
while teller<4:
    legg_til_navn=input("")
    legg_til_navn.lower()
    liste2.append(legg_til_navn)
    teller+=1
#Sjekker om navnet mitt er i listen
if "nasir" in liste2:
    print("Du husket meg!")
print("Glemt meg?")

#plusser sammen elementene i starteb av listen
produkt=liste[0]*liste[1]
liste3=[produkt]
merge= liste3+liste
print("merged", merge)
merge.pop(-1)
merge.pop(-1)
print("merged", merge)
