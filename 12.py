#Project euler 12
from sympy import *
def compute12():
    def getTriangleNumber(x):
        liste = []
        for x in range (1, 1 + x):
            liste.append(x)
        return sum(liste)
    i = 1 
    notFound = True
    div = 500
    sayi = 1
    while(notFound):
        trn = getTriangleNumber(i)
        if(len(divisors(trn)) > div):
            sayi = trn
            notFound = False
        else:
            i = i + 1
    return sayi
    
print(compute12())