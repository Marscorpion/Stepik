from  fractions import  Fraction as f
from math import factorial as F


print(sum([f(1, F(i)) for i in range(1, int(input()) + 1)]))