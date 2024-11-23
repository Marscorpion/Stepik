n = int(input())
matrix = [['*'] * n  for _ in range(n)]


for i in range(n):
    for j in range(n):
        for c in range(n):
            if i == j:
                matrix[i][j] = 0
            elif j == i + c or i == j + c:
                matrix[i][j] = c


for row in matrix:
    print(*row)