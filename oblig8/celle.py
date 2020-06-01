class Celle:
    #Konstrukt
    def __init__(self):
        #0 = dead, 1 = alive
        self._status = 0

    def settDoed(self):
        self._status = 0

    def settLevende(self):
        self._status = 1

    def erLevende(self):
        return self._status == 1

    def hentStatusTegn(self):
        if self.erLevende():
            return 'O'
        else:
            return '.'
