
#Funksjoen som teller bokstaver i ord
def tell_bokstav(ord):
    teller = 0
    for x in ord:
        teller +=1
    return teller

#funksjon for å telle antall ord i en settning
def tell_ord_i_settning(sentning):
    ordbok = {}
    s = sentning.split()
    for x in s:
        if x in ordbok:
            ordbok[x] += 1
        else:
            ordbok[x] = 1
    return ordbok



inp = input("Skriv in en sentning: ")
y = inp.split()

print("Det er ", len(y), "ord i sentningen din")
dictt = tell_ord_i_settning(inp)
for x in y:
    print("ordet " +" "+ x +" forekommer ", dictt[x], "ganger og har ",tell_bokstav(x), " bokstaver i seg" )
