#Project euler 1
def compute():
    liste = list(range(1, 1000))
    liste3or5 = [x for x in liste if x % 3 == 0 or x % 5 == 0]
    sum1 = sum(liste3or5)
    return str(sum1)



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
print(compute2())