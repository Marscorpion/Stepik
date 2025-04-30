from math import sin, sqrt

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

functions = {'квадрат': square, 'куб': cube, 'корень': sqrt, 'модуль': abs, 'синус': sin}

n = int(input())
command = input()

print(functions[command](n))

# def myfunc(num, command):
#     mydict = {'квадрат': num ** 2, 'куб': num ** 3, 'корень': num ** (1/2), 'модуль': abs(num), 'синус': sin(num)}
#     return mydict[command]
#
# print(myfunc(int(input()), input()))

# def func(n, name_func):
#   return {'квадрат': n ** 2, 'куб': n ** 3, 'корень': n ** 0.5, 'модуль': abs(n), 'синус': sin(n)}[name_func]
#
# print(func(int(input()), input()))