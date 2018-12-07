
class LZWDecoder:
    # konstruktor LZW dekodera
    def __init__(self, n, D, startingIndex):
        # n - broj simbola u rjecniku
        self.n = n
        # D - rjecnik
        self.D = D
        # pocetni index rjecnika
        self.startingIndex = startingIndex

    # metoda za dekodiranje kodirane poruke kP koja se predaje kao parametar metode
    def decode(self, kP):
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
