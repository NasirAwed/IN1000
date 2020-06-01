def billetpris():

    billetpris = 0
    #Her kan brukeren putte in ´23 år´, og da vil det systemet se på den som en streng. som gjør if sjekken umulig.
    alder=input("Hvor gammel er du? ")

    if int(alder) <= 17:
        billetpris = 30
    elif int(alder) > 63:
        billetpris = 35
    else:
        billetpris = 50
    print("billetprisen din blir ",billetpris )
billetpris()
billetpris()
billetpris()
billetpris()
