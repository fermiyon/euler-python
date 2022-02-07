#Project euler 4
def compute4():
    #Uc haneli sayilar
    threedigits = list(range(100,999 + 1))
    carpimlar = []
    #uc haneli sayilarin carpimi
    for x in threedigits:
        for y in threedigits:
            carpimlar.append(x*y)
            #print(x,y,x*y)
    #Filtreleme ::-1 reverse fonksiyonunun karsiligi
    polindromes = [x for x in carpimlar if str(x) == str(x)[::-1]]
    maks = max(polindromes)
    return maks

print(compute4())

#Project euler 1
def compute():
    liste = list(range(1, 1000))
    liste3or5 = [x for x in liste if x % 3 == 0 or x % 5 == 0]
    sum1 = sum(liste3or5)
    return str(sum1)


#Project euler 2
def compute2():

    def fibonacci_of(n):
        if n in {0,1}:
            return n
        return fibonacci_of(n-1) + fibonacci_of(n-2)
    
    def isPrime(k):
        return len([x for x in range(1,k+1) if k % x == 0]) == 2
    def isEven(k):
        return k % 2 == 0

    maxl = 4000000
    fibSequence = []
    i = 2
    cont = True
    while cont:
        fib = fibonacci_of(i)
        if fib < maxl:
            fibSequence.append(fib)
            print(fib)
            i+=1
        else:
            cont = False
        print(fibSequence)
    #print(fibSequence)
    fibSequenceFiltered = [x for x in fibSequence if isEven(x)]
    print(fibSequenceFiltered)
    ans = sum(fibSequenceFiltered)
    return ans

def compute3():
    #Asal mi
    def isPrime(k):
        return len([x for x in range(1,k+1) if k % x == 0]) == 2
    #Asal bolenler
    def primeFactors(k):
        return [x for x in range(1,k+1) if k % x == 0 and isPrime(x)]
    q = 600851475143
    d = 13195
    largestPrimeFactor = primeFactors(d).pop()
    return largestPrimeFactor