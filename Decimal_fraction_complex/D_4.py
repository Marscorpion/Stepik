from decimal import *

getcontext().prec = 28
d = Decimal(input())

print(d.exp() + d.ln() + d.log10() + d.sqrt())
