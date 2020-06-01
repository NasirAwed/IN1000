def addisjon(tall1,tall2):
    return tall1+tall2


print(addisjon(1,2))


def subtraksjon(tall1,tall2):
    return tall1-tall2

def divide(tall1, tall2):
    return tall1/tall2

#Sjekker om funksjonene fungerer som de skal
assert subtraksjon(2,2) == 0
assert subtraksjon(-10,-2) == -8
assert subtraksjon(0,0) == 0
assert subtraksjon(-10,2) == -12
assert divide(10,5) == 2
assert divide(-10,-2) == 5
assert divide(6,-3) == -2

def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54



print(tommerTilCm(1))

def skrivBeregninger():
    print("Utregninger: ")
    t1 = input("Skriv inn tall 1: ")
    t2 = input("Skriv inn tall 3:  ")
    #Sikrer meg at jeg har int verdier
    try:
        val1 = float(t1)
        val2 = float(t2)
        print("Resultat av summering: ", addisjon(val1,val2))
        print("Resultat av subtraksjon: ",subtraksjon(val1,val2))
        print("Resultat av divisjon: ",divide(val1,val2))
        print("Konvertering fra tommer til cm: ")
        t3 = input("Skriv inn tall: ")
        val3 = float(t3)
        print("Resultat: ",tommerTilCm(val3))
    except ValueError:
        print("Input error")
skrivBeregninger()
