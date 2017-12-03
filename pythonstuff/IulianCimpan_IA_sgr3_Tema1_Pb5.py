from math import sqrt

def gaussavg(a,b,n):
    if n == 0:
        return a, b
    i = 0
    while i<n:
        c = (a+b)/2
        b = sqrt(a*b)
        a = c
        i = i+1
    return a, b


a = input('a = ')
b = input('b = ')
n = input('gasiti termenii cu indicele n = ')

print(gaussavg(a,b,n))
