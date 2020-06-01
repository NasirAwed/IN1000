from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn


    def leggTilSang(self, nysang):
        self._sanger.append(nysang)

    def fjernSang(self, sang):
        for object in self._sanger:
            if sang == object:
                print("Fjerner sang: ", object)
                self._sanger.remove(sang)

    def spillSang(self, sang):
        for object in self._sanger:
            if str(sang) == str(object):
                print("Spiller sang: ", object)

    def spillAlle(self):
        print("Spiller alle sanger")
        for object in self._sanger:
            print(object)

    def finnSang(self,tittel):
        for object in self._sanger:
            if str(tittel) == str(object):
                return object


    def hentArtistUtvalg(self, artistnavn):
        list = []
        for x in self._sanger:
            if x.sjekkArtist(artistnavn):
                list.append(x)

        return list

    def lesFraFil(self, filnavn):
        f = open(filnavn, "r")
        for line in f:
            alldata = line.strip().split(";")
            x = Sang(alldata[0], alldata[1])
            #self._sang.append(x)
            self.leggTilSang(x)


        f.close()
