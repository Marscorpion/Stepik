n, m = [int(c) for c in input().split()]
matrixA = [[int(num) for num in input().split()] for _ in range(n)]

input()

m, k = [int(c) for c in input().split()]
matrixB = [[int(num) for num in input().split()] for _ in range(m)]

matrixC = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for o in range(m):
            matrixC[i][j] += matrixA[i][o] * matrixB[o][j]

for row in matrixC:
    print(*row)