n, m = input(), input()
n1 = complex(n)
m1 = complex(m)

operations = {'+': n1 + m1, '-': n1 - m1, '*': n1 * m1}

for op, res in operations.items():
    print(f'{n1} {op} {m1} = {res}', sep='\n')

# a, b = complex(input()), complex(input())
#
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')