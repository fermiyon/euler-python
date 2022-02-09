#Project euler 10
from sympy import *
def compute10():
    liste = list(range(1,2000000))
    primes = [x for x in liste if isprime(x)]
    return sum(primes)
print(compute10())