func = lambda c: c[0].lower() == c[-1].lower() == 'a'

# func=lambda x: x[0] in 'aA' and x[-1] in 'aA'

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdb'))
print(func('abcdA'))