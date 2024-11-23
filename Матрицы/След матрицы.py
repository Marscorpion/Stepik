n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

total = 0
for i in range(n):
    total += matrix[i][i]

print(total)