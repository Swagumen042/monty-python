#program care calculeaza suma S(1,n) = i(1+i)

def sumone(n):
    i = 1
    global suma
    global nrop
    while i<=n: #inclusiv n
        suma = suma + (i + i*i)
        nrop = nrop + 1
        i = i + 1
    return suma, nrop

suma = 0
nrop = 0
n = input()
sumone(n)
print('Suma este: ' + repr(suma))
print('Numarul de operatii este: ' + repr(nrop))
