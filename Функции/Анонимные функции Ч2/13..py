
from functools import reduce
from operator import add

def evaluate(coefficients, x):
    n = len(coefficients)
    # используем индексы для вычисления степени:
    return reduce(add, map(lambda i: coefficients[i] * x ** (n - i - 1), range(n)))

coefficients = list(map(int, input().split()))
x = int(input())
print(evaluate(coefficients, x))
#
# from functools import reduce
#
# evaluate = lambda coefficients, x: reduce(lambda s, a: s * x + a, coefficients, 0)
#
# print(evaluate([*map(int, input().split())], int(input())))

# from functools import reduce
# from operator import *
#
# def evaluate(coefficients, x):
#     coef = map(lambda y, z: int(y)*(x**z), coefficients, range(len(coefficients))[::-1])
#     total = reduce(add, list(coef), 0)
#     return(total)
#
# print(evaluate(input().split(), int(input())))