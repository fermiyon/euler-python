#Project euler 1
def compute():
    liste = list(range(1, 1000))
    liste3or5 = [x for x in liste if x % 3 == 0 or x % 5 == 0]
    sum1 = sum(liste3or5)
    return str(sum1)

print(compute())