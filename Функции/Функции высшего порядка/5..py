def func_apply(function, items):
     return list(map(function, items))

# def func_apply(function, items):
#     return [function(x) for x in items]

def add3(x):
    return x + 3


def mul7(x):
    return x * 7

numbers = [1, 2, 3, 4, 5, 6]

print(func_apply(mul7, numbers))
print(func_apply(add3, numbers))
print(func_apply(str, numbers))