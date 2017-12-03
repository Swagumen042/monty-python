from math import sqrt

def erato(n):
    # functie care genereaza o lista de prime pana la n
    global prime
    auxprime = []
    prime = []
    j=2
    for i in range(0,n):
        auxprime.append(True)
    while j<sqrt(n):
        if auxprime[j] == True:
            for q in range(j*j,n,j):
                auxprime[q]=False
        j=j+1
    p = 2
    while p<n:
        if auxprime[p] == True:
            prime.append(p)
        p=p+1
    return prime


def goldbach(num, prime):

    left=0
    right = len(prime)-1
    sol = []
    while left < right:
        check = prime[left] + prime[right]
        if (check-num) == 0:
            sol.append((prime[left],prime[right]))
            return sol
        if check < num:
            left = left + 1
        if check > num:
            right = right - 1

n = input('Generati lista cu numere prime pana la: ')
prime = erato(n)
print(prime)
num = input('Introduceti numarul par pentru care vreti solutia: ')
while(num%2):
    num = input('Introduceti numarul PAR pentru care vreti solutia: ')
print(goldbach(num, prime))
