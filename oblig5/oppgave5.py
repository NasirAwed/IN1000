"""
Skriv et beregningsprogram for skreddere med en funksjon som leser inn en fil (som du lager selv og
leverer sammen med de andre filene)

 der hver linje beskriver et navn på et mål og selve målet i tommer. Formatet vil se slik ut:
       Skulderbredde 4
       Halsvidde 3.2
       Livvidde 10
       
Hint​: du kan bruke funksjonen .​split()​ for å gjøre dette.
La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi og returner ordboken.
Lag deretter en prosedyre som tar imot en liste av mål og benytter seg av ​tommerTilCm​ som du skrev tidligere
for å skrive ut målene i centimeter
"""



fil = open("oppgave5.txt", "r")
dic = {}
for x in fil:
    y =x.split()
    dic[y[0]]=y[1]


def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54

for k in dic:
    print("key= "+" "+k+" value ",tommerTilCm(float(dic.get(k))))
