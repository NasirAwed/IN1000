"""
        Oppgave tekst:
Skriv en klasse Person med en konstruktør som tar imot navn og alder.
I tillegg skal konstruktøren ha en tom liste hobbyer.
Skriv en metode leggTilHobby som tar imot en tekststreng og legger den til i hobbyer-listen.
Skriv også en metode skrivHobbyer.
Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
 Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og alder kaller på metoden skrivHobbyer.
 La brukeren skrive inn navn og alder, og lag et Person-objekt med informasjonen du får.
 Deretter skal brukeren ved hjelp av en løkke få legge til så mange hobbyer de vil.
 Når brukeren ikke lenger ønsker å oppgi hobbyer skal statistikk om brukeren skrives ut.
"""
class Person:
    """docstring for Person."""
    def __init__(self, navn, alder):

        self._navn= navn
        self._alder= alder
        self._hobbyer = []

    def leggTilHobby(self, tekststreng):
        self._hobbyer.append(tekststreng)

    def skrivHobbyer(self):
        for x in self._hobbyer:
            print("Hobby: " +x)

    def skrivUt(self):
        print("Navn:" + self._navn)
        print("Alder: " , self._alder)

        self.skrivHobbyer()

alder = input("Tast inn Alder: ")
navn = input("Tast in et navn: ")
person = Person(alder, navn)
t = True
while t:
    hobby = input("Tast in en hobby (0 for å avslutte): ")
    if hobby == "0":
        t = False
        person.skrivUt()
    else:
        person.leggTilHobby(hobby)
