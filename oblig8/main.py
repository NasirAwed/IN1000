from spillebrett import Spillebrett


print("skriv in dimensjoner")
inp =input(" ")
inp2 = input(" ")
if inp2.isdigit() and inp.isdigit():
    s = Spillebrett(int(inp),int(inp2))
    s.tegnBrett()

else:
    print("invalid input")
    sys.exit()

T=True

while T:

    inp3 = input("Tast (enter) for å forsette , (q) for å avslutte: ")
    inp3.lower()
    if inp3== "":
        s.oppdatering()
        print(s.finnAntallLevende())
        s.print_Generasjonsnummer()
    elif inp3=="q":
        T =False
    if s.finnAntallLevende() == 0:
        print("everybody dead")
        T=False
