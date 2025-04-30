from  fractions import  Fraction as f

# print(sum([f(1, i**2) for i in range(1, int(input()) + 1)]))

n = int(input())
num = 0
# numbers = []
for i in range(1, n + 1):
    num += f(1, i**2)
    # n = f(1, i**2)
#     numbers.append(n)s
# print(sum(numbers))
print(num)
