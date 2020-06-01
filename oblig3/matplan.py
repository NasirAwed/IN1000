matplan =	{
  "mohammed" :["brødskiver", "coscos", "ris med lam"],
  "ahmed": ["egg", "subway", "ris med kylling"],
  "yousef": ["grøt", "suppe", "ris med fisk"]

}
def diet():
    print("Velg en av disse navna for å se hva de har spist")
    for key in matplan:
        print(key)

    svar =input()
    #Baserer meg på lowercase string
    if svar.lower() in matplan:
        print(matplan.get(svar.lower()))
diet()

"""
a. Brukernavn på alle IN1000 studentene
svar: ville brukt liste, fordi jeh trenger bare navna til studentene.

b. Brukernavn og antall poeng på innlevering 3 for alle studentene på IN1000
svar: ville brukt ordbok, her ttrenger jeg navn og hvor mange poeng en spesifik student fikk

c. Alle vinnere i Lotto siste år (kun navn)
svar: liste, samme som deloppgave A

d. All mat noen gjest i et selskap er allergisk mot (for å planlegge menyen)
svar: ville brukt ordbok med liste som verdi.

"""
