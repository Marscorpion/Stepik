n, m = int(input()), int(input())

matrix = [[i * j  for i in range(n)] for j in range(m)]

for i in range(n):
    for j in range(m):
        print(str(matrix[j][i]).ljust(3), end='')
    print()

# n, m = int(input()), int(input())
# for i in range(n):
#     for j in range(m):
#         print(str(i * j).ljust(3, ' '), end='')
#     print()

# n, m = int(input()), int(input())
# [print(*[str(i*j).ljust(3) for j in range(m)]) for i in range(n)]