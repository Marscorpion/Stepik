from fractions import Fraction as F

n1, n2 = [input() for _ in 'ab']
a, b = F(n1), F(n2)
operation = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}
for op, res in operation.items():
    print(f'{n1} {op} {n2} = {res}')


# from fractions import Fraction as frc
#
# n = input()
# m = input()
#
# print(f'{n} + {m} = {frc(n) + frc(m)}')
# print(f'{n} - {m} = {frc(n) - frc(m)}')
# print(f'{n} * {m} = {frc(n) * frc(m)}')
# print(f'{n} / {m} = {frc(n) / frc(m)}')