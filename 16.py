#Project euler 16
def compute16():
    sayi = pow(2,1000)
    liste= list(str(sayi))
    return sum(list(map(lambda x: int(x), liste)))
print(compute16())