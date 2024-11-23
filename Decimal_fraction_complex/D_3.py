from decimal import *
num = Decimal(input())

cyphers = num.as_tuple().digits
print(max(cyphers) + min(cyphers) * (abs(num) >= 1))

# num = Decimal(input())
# num_t = num.as_tuple()
#
# if abs(num_t.exponent) < len(num_t.digits):
#     print(max(num_t.digits) + min(num_t.digits))
# else:
#     print(max(num_t.digits))