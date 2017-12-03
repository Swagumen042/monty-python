def sumc(m,n):
    global sum_c
    sum_c = 0
    sum_aux_i = 0
    sum_aux_j = 0
    global nrop
    nrop = 0
    i=1
    j=1
    while i<=m:
        sum_aux_i = sum_aux_i + i
        nrop = nrop+1
        i = i+1
    while j<=n:
        sum_aux_j = sum_aux_j + 1/j
        nrop = nrop+1
        j = j+1
    sum_c = sum_aux_i * sum_aux_j
    return sum_c, nrop
        
m = input('m: ')
n = input('n: ')
sumc(m,n)
print('Suma este: ' + repr(sum_c))
print('Nr operatii: ' + repr(nrop))
