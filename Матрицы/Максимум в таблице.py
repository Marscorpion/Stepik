n, m = int(input()), int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]

maximum = matrix[0][0]
# maximum = -float('inf')
ind = (0, 0)

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            ind = (i, j)

print(*ind)
print(maximum)

n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row, col = i, j

print(row, col)



