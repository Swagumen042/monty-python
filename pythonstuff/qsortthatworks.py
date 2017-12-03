import random
#import antigravity # :)

def rand_list(elements, start, stop):
    #genereaza o lista 'random' cu numar de elemente introdus de la tastatura
    #in intervalul [start, stop]
    i = 0
    lst = [0]
    for i in range(elements):
       lst.insert(i,(random.randint(start,stop)))
    return lst
       
def qsort_that_actually_works(x,l,r):
    if l>=r:
        return
    i = l
    j = r
    pivot = x[random.randint(l,r)]
    while i<=j:
        while x[i] < pivot:
            i = i + 1
        while x[j] > pivot:
            j = j - 1
        if i<=j:
            x[i],x[j] = x[j],x[i]
            i = i+1
            j = j-1
        if l<j:       
            qsort_that_actually_works(x,l,j)
        if i<r:
            qsort_that_actually_works(x,i,r)
    return x,nrop

nrel = input('nr elemente = ')
start = input('start interval = ')
stop = input('stop interval = ')
y = rand_list(nrel, start, stop)
print('Inainte de sortare' + repr(y))
qsort_that_actually_works(y,0,len(y)-1)
print('Dupa sortare' + repr(y))
            

        


        
