n, m = map(int, input().split())

board = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            board[i][j] = i * m + j + 1
        else:
            board[i][j] = (i + 1) * m - j

for row in board:
    print(*row)

# n, m = map(int, input().split())
#
# matrix = [[i * m + j + 1 if i % 2 == 0 else (i + 1) * m - j for j in range(m)] for i in range(n)]
#
# for row in matrix:
#     print(*row)

# n, m = map(int, input().split())
# for i in range(n):
#     for j in range(m):
#         print(str(i * m + j + 1).ljust(3) if i % 2 == 0 else str((i + 1) * m - j).ljust(3), end=' ')
#     print()

# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + j + 1
#     if i % 2:
#         matrix[i].reverse()
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()