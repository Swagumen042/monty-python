def sumb(m,n):
    global sum_b
    global nrop
    i = 1
    j = 1
    while i<=m: #inclusiv m
        while j<=n: #inclusiv n
            sum_b = sum_b + j
            nrop = nrop + 1
            j = j+1
        sum_b = sum_b + i*j
        nrop = nrop + 1
        i=i+1
    return sum_b, nrop
sum_b = 0
nrop = 0

m = input('m: ')
n = input('n: ')
sumb(m,n)
print('Suma este: ' + repr(sum_b))
print('Nr. operatii este: ' + repr(nrop))

