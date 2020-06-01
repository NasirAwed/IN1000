class Motorsykkel:
    def __init__(self, merke, registreringsnummer, km):
        self._merke = merke
        self._registreringsnummer = registreringsnummer
        self._km = km

    def kjor(self, km):
        print("Kilometerstand stand var ", self._km)
        print("øker med ", km)
        self._km = self._km+km
        print("ny Kilometerstand ", self._km)

    def hentKilometerstand(self):
        print("Kilometerstand er ", self._km)

    def skrivUt(self):
        print("Kilometerstand stand var ", self._km)
        print("Merke er ", self._merke)
        print("registreringsnummer stand er ", self._registreringsnummer)
