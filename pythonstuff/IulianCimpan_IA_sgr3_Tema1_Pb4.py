from math import sqrt
l = []
def lagrange(n):
    i = 0
    while not i == 4:
       rad = sqrt(n)//1
       n = n - (rad * rad)
       l.append(rad*rad)
       i=i+1
    return l
       

n = input('Introduceti N: ')
print(lagrange(n))

    
