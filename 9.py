#Project euler 9
import itertools
from math import sqrt
import numpy
def compute9():
  list1 = list(range(500 + 1))
  comb = list(itertools.combinations(list1,3))
  list3 = [x for x in comb if x[0]*x[0] + x[1]*x[1] == x[2]*x[2]]
  res = [x for x in list3 if x[0] + x[1] + x[2] == 1000]
  pro = numpy.prod(res.pop())
  return pro
print(compute9())
