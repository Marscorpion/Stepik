
def mean(*args):
    num = []
    for i in args:
        if type(i) is int or type(i) is float:
            num.append(i)
    if num:
         return sum(num) / len(num)
    else:
         return 0


# def mean(*args):
#     args = [x for x in args if type(x) is int or type(x) is float]
#
#     return sum(args) / len(args) if args else 0



print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
