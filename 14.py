#Project euler 14
from operator import xor
from sympy import *
def compute14():
    liste = []
    def chainNumber(x):
        i = 1
        sayi = x
        notFound = True
        while notFound:
            if sayi == 1:
                notFound = False
                return i
            elif(sayi %2) == 0:
                sayi = sayi / 2
                i= i + 1
            elif(sayi%2 != 0):
                sayi = sayi*3 + 1
                i = i+ 1
    length = 1000000
    liste = list(map(lambda x: (x,chainNumber(x)),list(range(1,length + 1))))
    enuzun = sorted(liste,key = lambda x: x[1])
    return enuzun.pop()
print(compute14())