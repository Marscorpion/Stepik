n, m = [int(c) for c in input().split()]


matrixA = [[int(num) for num in input().split()] for _ in range(n)]

input()

matrixB = [[int(num) for num in input().split()] for _ in range(n)]

matrix_sum = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix_sum[i][j] = matrixA[i][j] + matrixB[i][j]

for row in matrix_sum:
    print(*row)
