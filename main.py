
kP = input("Unesite kodiranu poruku (simbole odvojite razmakom): \n")
kP = kP.split(' ')

n = int(input("\nUnesite broj simbola u rjecniku: "))

print("\nUnesite simbole rjecnika: ")
D = {}
for i in range(n):
    D[str(i)] = input('D[{}] = '.format(i))

for i in range(len(kP)):
    if kP[i] in D:
        print(D[kP[i]], end=' ')

        if i > 0:
            temp = D[kP[i-1]] + D[kP[i]][0]
            if temp not in D.values():
                D[str(n)] = temp
                n += 1
    else:
        temp = D[kP[i-1]] + D[kP[i-1]][0]
        D[str(n)] = temp
        print(D[str(n)], end=' ')
        n += 1
