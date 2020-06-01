def innlesing(filnavn):
    dictt = {}
    with open(filnavn) as f:
        for x in f:
            (key, val) = x.split()
            dictt[key] = int(val)
    return dictt


def maanedensSalgsperson(dictt):
    key = next(iter(dictt))
    for k in dictt:
        if dictt[k] > dictt[key]:
            key = k

    print("Ansatt"+" "+ key+" "+ " har solgt mest"+" ", dictt[key])

def totaltAntallSalg(dictt):
    sum = 0
    for k in dictt:
        sum = sum+dictt[k]
    return sum

def gjennomsnittSalg(dictt):
    antall = 0
    for k in dictt:
        antall = antall +1

    return totaltAntallSalg(dictt)/antall



def hovedprogram():
    dict = innlesing("salgstall.txt")
    antall = 0
    for k in dict:
        antall = antall +1
    maanedensSalgsperson(dict)
    print("Aktive selgere denne maaneden = ",antall )
    print("sum =", totaltAntallSalg(dict))
    print("Gjennomsnitt = ", gjennomsnittSalg(dict))

hovedprogram()
