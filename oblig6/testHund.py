from hund import Hund



def hovedprogram():
    dog = Hund(10, 5)
    print("alder: ",dog.hentAlder())
    print("vekt ", dog.hentVekt())
    dog.spring()
    print("vekt ", dog.hentVekt())
    dog.spring()
    print("vekt ", dog.hentVekt())
    dog.spis(1)
    print("vekt ", dog.hentVekt())
    dog.spis(1)
    print("vekt ", dog.hentVekt())

hovedprogram()
