import random
import sys
from celle import Celle
import datetime

class Spillebrett(object):
    generasjonsnummer = 0
    def __init__(self, rader, kolonner):
        super(Spillebrett, self).__init__()
        self._rader = rader
        self._kolonner = kolonner
        self._brett = [[Celle() for j in range(kolonner)] for i in range(rader)]
        self._generer()




    def tegnBrett(self):
        for x in self._brett:
             print(' '.join([str(elem.hentStatusTegn()) for elem in x]))

    def oppdatering(self):
        i = 0
        i2 = 0
        #Her går jeg igjennom for å se om noen celler skal bli døde eller levende.
        #Bruker ikke index eller range for å kunne sette objektet til status direkte
        for x in self._brett:
            for e in x:
                temp2 = self.FinnLevendeNabo(i,i2)
                if self._brett[i][i2].hentStatusTegn()=='.' and len(temp2)==3:
                    e.settLevende()
                if len(temp2) > 3 or len(temp2) < 2:
                    e.settDoed()
                if i2 != self._kolonner-1:
                    i2+=1
                else:
                    i2=0
            i+=1
        print(self.tegnBrett())
        Spillebrett.generasjonsnummer+=1


    def finnAntallLevende(self):
        teller = 0
        #går igjennom 2d listen og teller antall levende celler
        for x in self._brett:
            for elem in x:
                if elem.erLevende():
                    teller +=1
        print("antall_levende = ", teller)

        return teller


    def _generer(self):
        #Genererer random levende celler med 30% sjanse per celle
        for x in self._brett:
            [elem.settLevende() for elem in x if random.random() < 0.30  ]



    def FinnLevendeNabo(self, rad, kol):
        liste = []
        #Looper slik at x blir alltid en minus rad og 1 pluss rad. samme for kolonne
        #hvis for eksempel rad er 2 og kolonne er 1 og brett er 3*3
        #første vil x være 2+(-1) = 1 (opp i rad) og kolonne 1+(-1) = 0 (som er en bak)
        #neste iterasjon vil være lik rad og kolonne siden plusser med 0
        # Så i teorien vil den gå i 4 rettninger rundt rad og kolonne.
        for i in range(-1,2):
            for j in range(-1,2):
                #x er naborad til raden og y er nabokolonne til kolonnen
                x = rad + i
                y = kol + j
                if (x == rad and y == kol) is  False:
                    #Sjekker edge cases
                    if (x < 0 or y < 0) is False:
                        if (x > self._rader - 1 or y > self._kolonner - 1) is False:
                            #Legger till da etter hvis levende
                            if self._brett[x][y].erLevende():
                                liste.append((x, y))


        return liste



    def print_Generasjonsnummer(self):
        print("generasjonsnummer", self.generasjonsnummer)
