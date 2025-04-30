from fractions import  Fraction

n = int(input())

numbers = []

for i in range(1, n - 1):
    num = Fraction(i, n - i)
    if num.numerator < num.denominator and num.numerator + num.denominator == n:
        numbers.append(num)

print(max(numbers))


# from fractions import Fraction as F
# from math import gcd
#
# n = int(input())
# a = n // 2
# b = n - a
# while gcd(a, b) != 1:
#     a -= 1
#     b += 1
# print(F(a, b))