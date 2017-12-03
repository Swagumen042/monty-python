global nrc_ins
global nrm_ins
global nrc_sel
global nrm_sel
global nrc_bubble
global nrm_bubble


def insertsort(v):
    nrc_ins = 0
    nrm_ins = 0
    for i in range(1,len(v)):
        aux=v[i]
        nrm_ins = nrm_ins + 1
        j=i-1
        while j>=0 and aux < v[j]:
            nrc_ins = nrc_ins + 1
            v[j+1]=v[j]
            nrm_ins = nrm_ins + 1
            j-=1
        nrc_ins = nrc_ins + 1
        v[j+1]=aux
        nrm_ins = nrm_ins + 1
    return v,nrc_ins,nrm_ins

def selectsort(v):
    nrc_sel=0
    nrm_sel=0
    for i in range(len(v)):
        k=i
        for j in range(i,len(v)):
            nrc_sel = nrc_sel + 1
            if(v[j]<v[k]):
                k=j
        if i!=k:
            nrm_sel = nrm_sel + 3
            aux=v[i]
            v[i]=v[k]
            v[k]=aux
    return v,nrc_sel,nrm_sel

def bubblesort(v):
    nrc_bubble = 0
    nrm_bubble = 0
    sort = True
    while sort:
        sort = False
        for i in range(0,len(v)-1):
            nrc_bubble=nrc_bubble+1
            if v[i]>v[i+1]:
                nrm_bubble = nrm_bubble +3
                sort = True
                aux=v[i]
                v[i]=v[i+1]
                v[i+1]=aux
                
    return v,nrc_bubble,nrm_bubble

L_fav=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
L_defav=[100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
L_med=[28, 39, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 63, 17, 45, 58, 20, 21, 54, 61, 24, 25, 26, 34, 27, 30, 49, 32, 33, 40, 35, 73, 37, 67, 82, 99, 89, 42, 43, 64, 72, 46, 86, 48, 1, 50, 51, 52, 53, 38, 57, 56, 55, 19, 59, 60, 78, 62, 16, 44, 65, 66, 22, 68, 69, 70, 71, 18, 36, 74, 75, 80, 77, 23, 79, 76, 81, 31, 83, 84, 85, 47, 87, 88, 41, 95, 91, 92, 93, 94, 90, 96, 97, 98, 29]
print('Pentru insertsort: ')
print(insertsort(L_fav))
print(insertsort(L_defav))
print(insertsort(L_med))
#print('Pentru selectsort: ')
#print(selectsort(L_fav))
#print(selectsort(L_defav))
#print(selectsort(L_med))
#print('Pentru bubblesort: ')
#print(bubblesort(L_fav))
#print(bubblesort(L_defav))
#print(bubblesort(L_med))
