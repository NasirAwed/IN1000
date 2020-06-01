class Hund:

    

    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    def hentAlder(self):
        return self._alder

    def hentVekt(self):
        return self._vekt

    def spring(self):
        if self._metthet < 5:
            self._vekt = self._vekt - 1
            self._metthet = self._metthet - 1
        else:
            self._metthet = self._metthet - 1

    def spis(self,tall):
        if self._metthet > 7:
            self._vekt = self._vekt + 1
            self._metthet = self._metthet + tall
        else:
            self._metthet = self._metthet + tall
