import copy
n = int(input())

matrixA = [[int(num) for num in input().split()] for _ in range(n)]

m = int(input())

matrixB = copy.deepcopy(matrixA)

for _ in range(m-1):
    matrixC = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for o in range(n):
                matrixC[i][j] += matrixA[i][o] * matrixB[o][j]
    matrixB = copy.deepcopy(matrixC)


for row in matrixC:
    print(*row)