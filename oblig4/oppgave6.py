"""
        'oppgave tekst'

        Lag et system som holder styr på dine venners bursdager
"""
T = True
print("Skriv inn navnet til vennen din og når hen har bursdage. 0 for å avslutte")
deict = {}
#basic while loop for på legge til navn og bursdags dato i en ordbok.
while T:
    navn = input("Navn: ")
    dato = input("dato: ")
    deict[navn] = dato
    inp = input("Ferdig? (Y/N) ")
    if inp.lower() == "y":
        T = False
for key in deict:
    print("Din venn "+" "+ key +" "+"har bursdag ", deict[key])
