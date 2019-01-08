"""Modul sadržava razred za dekodiranje korištenjem LZW algoritma.

"""

class LZWDecoder:
    """Razred pruža metodu za dekodiranje poruke LZW algoritmom.
    
    """
    
    def __init__(self, n, D, startingIndex):
        """Konstruktor LZWDecoder razreda.

        :param n: broj simbola u rjecniku
        :type n: int
        :param D: rjecnik (dictionary)
        :type D: rjecnik u formatu  D[0] = 'a' 
        :param startingIndex: pocetni indeks rjecnika
        :type startingIndex: int

        """
        
        self.n = n
        self.D = D
        self.startingIndex = startingIndex

    
    def decode(self, kP):
        """Metoda za dekodiranje kodirane poruke kP koja se predaje kao parametar metode

        :param kP: kodirana poruka
        :type kP: lista simbola
        :returns: dekodirana poruka
        :rtype: str

        """

        # dekodirana poruka
        dP = ''

        # petlja dekodiranja kodirane poruke kP
        for i in range(len(kP)):
            # provjera postoji li simbol u rjecniku
            if kP[i] in self.D:
                #ispis dekodiranog simbola
                dP += self.D[kP[i]]

                if i > 0:
                    # dodavanje novog simbola u rjecnik ukoliko vec ne postoji u rjecniku
                    temp = self.D[kP[i-1]] + self.D[kP[i]][0]
                    if temp not in self.D.values():
                        self.D[str(self.n + self.startingIndex)] = temp
                        self.n += 1
            else:
                # ukoliko simbol dekodiranja ne postoji u rjecniku, konstruira se iz prethodno dekodiranog simbola poruke kP
                self.D[str(self.n + self.startingIndex)] = self.D[kP[i-1]] + self.D[kP[i-1]][0]
                dP += self.D[str(self.n + self.startingIndex)]
                self.n += 1

        return dP
