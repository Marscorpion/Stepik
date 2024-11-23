n = int(input())

matrix = [[num for num in input().split()] for _ in range(n)]

result = 'YES'

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n-j-1][n-i-1]:
            result = 'NO'
            break
print(result)