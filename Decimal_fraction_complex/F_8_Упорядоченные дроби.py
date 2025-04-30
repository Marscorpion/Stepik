from fractions import  Fraction

n = int(input())

numbers = set()

for i in range(1, n):
    for j in range(i+1, n + 1):
        num = Fraction(i, j)
        numbers.add(num)

print(*sorted(numbers), sep='\n')