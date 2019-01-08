from LZWDecoder import LZWDecoder


try:
    # kP - kodirana poruka
    kP = list(filter(lambda s: s != '', input("Unesite kodiranu poruku (simbole odvojite razmakom): \n").split(' ') ))
except:
    print('Doslo je do pogreske prilikom unosa kodirane poruke!')
    exit(1)


try:
    # n - pocetni broj simbola u rjecniku
    n = int(input("\nUnesite broj simbola u rjecniku: "))
except:
    print('Doslo je do pogreske prilikom unosa pocetnog broja simbola u rjecniku! Potrebno je unijeti prirodni broj.')
    exit(2)


print("\nUnesite simbole rjecnika: ")

try:
    # D - rjecnik (dictionary)
    D = {}
    # pocetni indeks simbola rjecnika (zadano u zadatku kao 0 (nula) )
    pocetniIndeks = 0

    for i in range(pocetniIndeks, n+pocetniIndeks):
        # unos podataka u formatu "D[0] = a" etc.
        D[str(i)] = input('D[{}] = '.format(i))
except:
    print('Doslo je do pogreske prilikom unosa simbola rjecnika!')
    exit(3)


try:
    # instanciranje LZW decodera
    decoder = LZWDecoder(n, D, pocetniIndeks)
except:
    print('Doslo je do pogreske prilikom instanciranja objekta LZWDecoder s parametrima: \nn = {}\nD = {}\npocetniIndex = {}\n'.format(n, D, pocetniIndeks))
    exit(4)

try:
    #ispis dekodirane poruke
    print("\nDekodirana poruka glasi: \n" + decoder.decode(kP))
except:
    print('Doslo je do pogreske prilikom dekodiranja kodirane poruke!')
    exit(5)

print('\n')
