def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c +=1
        b = 10
        b +=a
        print(b)
    return b



def hovedprogram():
    a=42
    b=0
    print(b)
    b=a
    a = minFunksjon()
    print(b)
    print(a)

hovedprogram()

"""
Vi definerer 2 funksjoner. den første heter minFunksjon()
den andre er hovedprogram(). i hovedprogram har vi 2 variabler, a og b.
a = 42 og b = 0. printer ut b ut til terminal. b blir satt til a som er 42 .
a kaller minFunksjon() som har en loop i range av 2 sp den vi kjøre 2 ganger.
c = 2 printer c som er 2. addisjon av c = c+1, c = 3. ny variabel b som er 10.
på linje 8 vil en error komme fram fordi a er ikke definert og programmet vi avlsutte. 



"""
