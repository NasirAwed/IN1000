from motorsykkel import Motorsykkel

def hovedprogram():
    x = Motorsykkel("bugatti", "75n34", 10)
    y = Motorsykkel("ferrari", "95X34", 20)
    z = Motorsykkel("lambo", "85n34", 13)
    z.kjor(10)
    x.skrivUt()
    y.skrivUt()
    z.skrivUt()

hovedprogram()
