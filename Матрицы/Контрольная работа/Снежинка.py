n = int(input())

matrix = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == n // 2  or j ==  n // 2  or i == j or i + j + 1 == n:
            matrix[i][j] = '*'

for row in matrix:
    print(*row)

# [print(*i) for i in matrix]