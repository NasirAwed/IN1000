mineOrd=[]

def slaaSammen(string1, string2):
    return string1+string2


def skrivUt(lis):
    for x in lis:
        print(x)


t = 1
while t > 0:
    inp = input("Tast in i for å legge sammen to strenger, u for å skrive ut tidligere input eller s for å avlsutte ")
    if inp.lower() == "i":
        inp1 = input("streng 1: ")
        inp2 = input("streng 2: ")
        mineOrd.append(slaaSammen(inp1,inp2))
    if inp.lower() == "u":
        skrivUt(mineOrd)
    if inp.lower() == "s":
        t = 0
