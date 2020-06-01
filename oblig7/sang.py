class Sang(object):
    """docstring for Sang."""
    def __init__(self,title,artist):
        super(Sang, self).__init__()
        self._title = title
        self._artist = artist

    def spill(self):
        print("Spiller"+" ''"+self._title+" ''"+"av artist"+" -"+self._artist )

    def sjekkArtist(self,navn):
        a = set(navn.split())
        b = set(self._artist.split())
        c = a.intersection(b)
        if c:
            return True
        return False
        
    def sjekkTittel(self, string):
        s = string.lower()
        return s == self._title.lower()

    def sjekkArtistogTittel(self, artist, title):
        if self.sjekkArtist(artist) and self.sjekkTittel(title):
            print(title)
            return True
        else:
            return False

    def hentArtist(self):

        return self._artist

    def __str__(self):
        return str(self._title)
    __repr__ = __str__
