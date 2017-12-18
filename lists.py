class Node:
    def __init__(self, val = None, urm = None):
        self.info = val
        self.urm = urm
class LinkedList:
    def __init__(self):
        self.inceput = None
        self.aux = None
        
    def adaugaInceput(self,x):
        if self.inceput == None:
            self.inceput=Node(x,None)
        else:
            newNode=Node(x,self.inceput)
            self.inceput=newNode
            
    def stergeInceput(self):
        self.inceput=self.inceput.urm
        
    def adaugaSfarsit(self,x):
        if self.inceput == None:
            self.inceput = Node(x,None)
        else:
            self.aux = self.inceput
            while self.aux.urm != None:
                self.aux = self.aux.urm
            newNode=Node(x,None)
            self.aux.urm=newNode
            
    def adaugareDupaElem(self,x,y):
        self.aux = self.inceput
        while self.aux != None and self.aux.info != x:
            self.aux = self.aux.urm
        if aux != None:
            newNode=Node(y,self.aux.urm)
            self.aux.urm = newNode
        else:
            print("Nu exista nod cu informatia " + repr(x))
            
    def stergeSfarsit(self):
        if self.inceput.urm == None:
            self.inceput = None
        else:
            self.aux = self.inceput
            while self.aux.urm.urm != None:
                self.aux = self.aux.urm
            self.aux.urm = None
            
    def stergereDupaElem(self,x):
        self.aux = self.inceput
        while self.aux != None and self.aux.info != x:
            self.aux = self.aux.urm #se parcurg elementele de la inceput pana se ajunge la cel dorit
        if self.aux != None and self.aux.urm != None:
            self.aux.urm = self.aux.urm.urm
        else:
            print("Nu exista nod cu informatia " + repr(x))
            
    def cautareElement(self,x):
        self.aux = self.inceput
        while(self.aux!=None) and (self.aux.info != x):
            self.aux = self.aux.urm
        return self.aux != None #true daca elem este in lista.
    
    def cautareNodIndex(self,k):
        self.aux=self.inceput
        i = 1
        while (self.aux != None) and (i < k):
            self.aux = self.aux.urm
            i = i + 1
        return self.aux #ofera valoarea elementului, daca indicele este mai mare decat lungimea se va returna None
    
    def parcurge(self):
        ref=self.inceput
        while (ref!=None):
            print(ref.info)
            ref=ref.urm

def auxReuniune(l, r):
    aux = l.inceput
    while aux != None:
        if not r.cautareElement(aux.info):
            r.adaugaInceput(aux.info)
        aux = aux.urm
    return r

def reuniune(l1, l2):
    reun = LinkedList()
    reun = auxReuniune(l1,reun)
    reun = auxReuniune(l2,reun)
    return reun

def split(l):
    aux = l.inceput
    l1 = LinkedList()
    l2 = LinkedList()
    i = 1
    while aux != None:
        if i%2 != 0:
            l1.adaugaInceput(aux.info)
        else:
            l2.adaugaInceput(aux.info)
        aux = aux.urm
        i = i+1
    return l1,l2

L=LinkedList()
L.adaugaInceput(2)
L.adaugaInceput(7)
L.stergeInceput()
L.adaugaInceput(3)
L.adaugaSfarsit(1)
print("---Testare cautari---")
print(L.cautareElement(3))
print(L.cautareNodIndex(7))
L.stergereDupaElem(3)
print("---Testare parcurgere---")
L.parcurge()
R=LinkedList()
R.adaugaInceput(7)
R.adaugaInceput(91)
R.parcurge()
print("---Testare functia reuniune---")
reuniune(L,R).parcurge()
print("---Testare functia split---")
