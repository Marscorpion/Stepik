# n = int(input())
#
# matrix = [[num for num in input().split()] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             matrix[i][j], matrix[n-1-j][j] = matrix[n-1-j][j],matrix[i][j]
#
# for row in matrix:
#     print(*row)

n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for row in matrix:
    print(*row)